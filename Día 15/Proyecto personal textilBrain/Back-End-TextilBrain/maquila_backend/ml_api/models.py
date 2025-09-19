from django.db import models

class Tela(models.Model):
    id_tela = models.AutoField(primary_key=True)
    nombre_tela = models.CharField(max_length=100)
    precio_por_metro = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'telas'
        managed = False

    def __str__(self):
        return self.nombre_tela


class Cierre(models.Model):
    id_cierre = models.AutoField(primary_key=True)
    tipo_cierre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cierres'
        managed = False

class Hilo(models.Model):
    id_hilo = models.AutoField(primary_key=True)
    tipo_hilo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hilos'
        managed = False

class Boton(models.Model):
    id_boton = models.AutoField(primary_key=True)
    tipo_boton = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'botones'
        managed = False

class Costura(models.Model):
    id_costura = models.AutoField(primary_key=True)
    tipo_costura = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'costuras'
        managed = False

class Modelo(models.Model):
    GENERO_CHOICES = [
        ('dama', 'Dama'),
        ('caballero', 'Caballero'),
    ]
    
    id_modelo = models.AutoField(primary_key=True)
    nombre_modelo = models.CharField(max_length=120)
    genero = models.CharField(max_length=9, choices=GENERO_CHOICES)
    tiene_bolsillos = models.BooleanField(default=False)
    lleva_pretina = models.BooleanField(default=False)
    lleva_deslavado = models.BooleanField(default=False)
    lleva_planchado = models.BooleanField(default=False)
    lleva_desgaste_extra = models.BooleanField(default=False)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    year_introduced = models.IntegerField(default=2020)  # AÑADE ESTE CAMPO
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'modelos'
        managed = False

class ProcesoAdicional(models.Model):
    id_proceso = models.AutoField(primary_key=True)
    id_modelo = models.ForeignKey(Modelo, on_delete=models.DO_NOTHING, db_column='id_modelo')
    id_tela = models.ForeignKey(Tela, on_delete=models.DO_NOTHING, db_column='id_tela')
    id_cierre = models.ForeignKey(Cierre, on_delete=models.DO_NOTHING, db_column='id_cierre')
    id_hilo = models.ForeignKey(Hilo, on_delete=models.DO_NOTHING, db_column='id_hilo')
    id_boton = models.ForeignKey(Boton, on_delete=models.DO_NOTHING, db_column='id_boton')
    id_costura = models.ForeignKey(Costura, on_delete=models.DO_NOTHING, db_column='id_costura')
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'procesos_adicionales'
        managed = False

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=25, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clientes'
        managed = False

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('en_produccion', 'En Producción'),
        ('terminado', 'Terminado'),
        ('entregado', 'Entregado'),
    ]
    
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, db_column='id_cliente')
    id_modelo = models.ForeignKey(Modelo, on_delete=models.DO_NOTHING, db_column='id_modelo')
    cantidad = models.IntegerField()
    fecha_pedido = models.DateField()
    total = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='en_produccion')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pedidos'
        managed = False

class Almacen(models.Model):
    TIPO_MATERIAL_CHOICES = [
        ('tela', 'Tela'),
        ('cierre', 'Cierre'),
        ('hilo', 'Hilo'),
        ('boton', 'Botón'),
        ('costura', 'Costura'),
    ]
    
    id_almacen = models.AutoField(primary_key=True)
    tipo_material = models.CharField(max_length=10, choices=TIPO_MATERIAL_CHOICES)
    id_material = models.IntegerField()
    cantidad_disponible = models.DecimalField(max_digits=12, decimal_places=3)
    unidad = models.CharField(max_length=15, default='ud')
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'almacen'
        managed = False

    def get_material(self):
        """Obtiene el objeto material relacionado"""
        model_map = {
            'tela': Tela,
            'cierre': Cierre,
            'hilo': Hilo,
            'boton': Boton,
            'costura': Costura
        }
        return model_map[self.tipo_material].objects.get(pk=self.id_material)