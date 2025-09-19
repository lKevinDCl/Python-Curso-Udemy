USE maquila_costos_ml;

INSERT INTO modelos
(nombre_modelo, genero, tiene_bolsillos, lleva_pretina, lleva_deslavado,
 lleva_planchado, lleva_desgaste_extra, precio_base)
VALUES
('Classic Slim',     'caballero', 1,1,0,1,0, 249.90),
('Straight Fit',     'caballero', 1,1,0,0,0, 259.90),
('Skinny Fit',       'dama',      1,0,1,0,1, 279.90),
('Boyfriend Cut',    'dama',      1,0,1,0,0, 269.90),
('Bootcut Vintage',  'dama',      1,1,1,1,1, 299.90),
('Relaxed Carpenter','caballero', 1,1,0,0,1, 289.90),
('Mom Jeans',        'dama',      1,0,1,0,0, 274.90),
('Cargo Utility',    'caballero', 1,1,0,0,0, 309.90),
('Flare High Rise',  'dama',      1,0,1,1,1, 314.90),
('Tapered Stretch',  'caballero', 1,1,0,1,0, 269.90),
('Wide-Leg Retro',   'dama',      1,0,1,0,1, 324.90),
('Athletic Cut',     'caballero', 1,1,0,0,0, 284.90);



-- Crea 200 nombres y teléfonos simples; personalízalos si lo deseas
INSERT INTO clientes (nombre, telefono, direccion)
SELECT
  CONCAT('Cliente ', LPAD(n,3,'0')),
  CONCAT('555', LPAD(FLOOR(RAND()*9000000)+1000000,7,'0')),
  CONCAT('Calle ', n, ' #', n*3)
FROM (
  SELECT @row := @row+1 AS n
  FROM (SELECT 0 UNION ALL SELECT 1) t1,
       (SELECT 0 UNION ALL SELECT 1) t2,
       (SELECT 0 UNION ALL SELECT 1) t3,
       (SELECT 0 UNION ALL SELECT 1) t4,
       (SELECT 0 UNION ALL SELECT 1) t5,
       (SELECT 0 UNION ALL SELECT 1) t6,
       (SELECT @row:=0) r
) AS nums
WHERE n <= 200;

DELIMITER //

DROP PROCEDURE IF EXISTS poblar_pedidos //
CREATE PROCEDURE poblar_pedidos(IN p_total INT)
BEGIN
  DECLARE i INT DEFAULT 0;        

  /* ---- Lógica ---- */
  IF p_total IS NULL THEN
    SET p_total := 20000;           
  END IF;

  WHILE i < p_total DO
    INSERT INTO pedidos (id_cliente, id_modelo, cantidad, fecha_pedido, total, estado)
    SELECT
      FLOOR(1 + RAND() * 200),                               -- cliente 1-200
      FLOOR(1 + RAND() * 12),                                -- modelo 1-12
      FLOOR(1 + RAND() * 6),                                 -- cantidad 1-6
      DATE_ADD('2024-01-01', INTERVAL FLOOR(RAND()*546) DAY),-- fecha aleatoria
      0,                                                     -- total provisional
      CASE                                                   -- estado ponderado
        WHEN RAND() < 0.60 THEN 'entregado'
        WHEN RAND() < 0.85 THEN 'terminado'
        ELSE 'en_produccion'
      END;

    SET i := i + 1;  -- incrementa el contador
  END WHILE;

  /* Calcula el total = precio_base × cantidad */
  UPDATE pedidos p
  JOIN modelos m ON m.id_modelo = p.id_modelo
  SET p.total = ROUND(m.precio_base * p.cantidad, 2)
  WHERE p.total = 0;
END //
DELIMITER ;