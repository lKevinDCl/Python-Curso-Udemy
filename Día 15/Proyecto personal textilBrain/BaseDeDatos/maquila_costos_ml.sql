CREATE DATABASE maquila_costos_ml
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE maquila_costos_ml;

CREATE TABLE telas (
  id_tela          INT AUTO_INCREMENT PRIMARY KEY,
  nombre_tela      VARCHAR(100)      NOT NULL,
  precio_por_metro DECIMAL(10,2)     NOT NULL,
  created_at       TIMESTAMP         DEFAULT CURRENT_TIMESTAMP,
  updated_at       TIMESTAMP         DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE cierres (
  id_cierre  INT AUTO_INCREMENT PRIMARY KEY,
  tipo_cierre VARCHAR(100)  NOT NULL,
  precio      DECIMAL(10,2) NOT NULL,
  created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE hilos (
  id_hilo   INT AUTO_INCREMENT PRIMARY KEY,
  tipo_hilo VARCHAR(100)  NOT NULL,
  precio    DECIMAL(10,2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE botones (
  id_boton   INT AUTO_INCREMENT PRIMARY KEY,
  tipo_boton VARCHAR(100)  NOT NULL,
  precio     DECIMAL(10,2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE costuras (
  id_costura   INT AUTO_INCREMENT PRIMARY KEY,
  tipo_costura VARCHAR(50)  NOT NULL,    
  precio       DECIMAL(10,2) NOT NULL,
  created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE modelos (
  id_modelo             INT AUTO_INCREMENT PRIMARY KEY,
  nombre_modelo         VARCHAR(120) NOT NULL,
  genero                ENUM('dama','caballero') NOT NULL,
  tiene_bolsillos       TINYINT(1)  NOT NULL DEFAULT 0,
  lleva_pretina         TINYINT(1)  NOT NULL DEFAULT 0,
  lleva_deslavado       TINYINT(1)  NOT NULL DEFAULT 0,
  lleva_planchado       TINYINT(1)  NOT NULL DEFAULT 0,
  lleva_desgaste_extra  TINYINT(1)  NOT NULL DEFAULT 0,
  precio_base           DECIMAL(10,2) NOT NULL,
  activo                TINYINT(1)  NOT NULL DEFAULT 1,     
  created_at            TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
  updated_at            TIMESTAMP    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE procesos_adicionales (
  id_proceso   INT AUTO_INCREMENT PRIMARY KEY,
  id_modelo    INT NOT NULL,
  id_tela      INT NOT NULL,
  id_cierre    INT NOT NULL,
  id_hilo      INT NOT NULL,
  id_boton     INT NOT NULL,
  id_costura   INT NOT NULL,
  precio_final DECIMAL(10,2) NOT NULL,  
  created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_proc_modelo  FOREIGN KEY (id_modelo) REFERENCES modelos(id_modelo),
  CONSTRAINT fk_proc_tela    FOREIGN KEY (id_tela)    REFERENCES telas(id_tela),
  CONSTRAINT fk_proc_cierre  FOREIGN KEY (id_cierre)  REFERENCES cierres(id_cierre),
  CONSTRAINT fk_proc_hilo    FOREIGN KEY (id_hilo)    REFERENCES hilos(id_hilo),
  CONSTRAINT fk_proc_boton   FOREIGN KEY (id_boton)   REFERENCES botones(id_boton),
  CONSTRAINT fk_proc_costura FOREIGN KEY (id_costura) REFERENCES costuras(id_costura)
);

CREATE TABLE clientes (
  id_cliente  INT AUTO_INCREMENT PRIMARY KEY,
  nombre      VARCHAR(120) NOT NULL,
  telefono    VARCHAR(25),
  direccion   VARCHAR(255),
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pedidos (
  id_pedido    INT AUTO_INCREMENT PRIMARY KEY,
  id_cliente   INT NOT NULL,
  id_modelo    INT NOT NULL,
  cantidad     INT NOT NULL,
  fecha_pedido DATE NOT NULL,
  total        DECIMAL(12,2) NOT NULL,
  estado       ENUM('en_produccion','terminado','entregado') DEFAULT 'en_produccion',
  created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_pedido_cliente FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
  CONSTRAINT fk_pedido_modelo  FOREIGN KEY(id_modelo)  REFERENCES modelos(id_modelo)
);

CREATE TABLE almacen (
  id_almacen          INT AUTO_INCREMENT PRIMARY KEY,
  tipo_material       ENUM('tela','cierre','hilo','boton','costura') NOT NULL,
  id_material         INT       NOT NULL,
  cantidad_disponible DECIMAL(12,3) NOT NULL,
  unidad              VARCHAR(15) DEFAULT 'ud', 
  fecha_actualizacion TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_material_tipo (tipo_material, id_material)
);
