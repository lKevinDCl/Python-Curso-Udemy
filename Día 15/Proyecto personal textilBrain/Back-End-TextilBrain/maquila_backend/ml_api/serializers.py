from rest_framework import serializers
from .models import Pedido, Cliente, Modelo
from datetime import datetime, timedelta

# Serializador para Predicción de Demanda
class PrediccionInputSerializer(serializers.Serializer):
    id_modelo = serializers.IntegerField(required=True)
    year = serializers.IntegerField(required=True)
    month = serializers.IntegerField(required=True)
    meses = serializers.IntegerField(
        default=6, 
        min_value=1, 
        max_value=12,
        help_text="Número de meses a predecir (1-12)"
    )

# Serializador para Datos Históricos
class HistoricoDemandaSerializer(serializers.Serializer):
    modelo_id = serializers.IntegerField(
        required=False,
        help_text="ID del modelo para filtrar (opcional)"
    )
    meses = serializers.IntegerField(
        default=12,
        min_value=1,
        max_value=36,
        help_text="Número de meses históricos a consultar (1-36)"
    )

# Serializador para Modelos
"""
class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = [
            'id_modelo', 
            'nombre_modelo', 
            'genero', 
            'precio_base',
            'tiene_bolsillos',
            'lleva_pretina'
        ]
        read_only_fields = ['id_modelo']
"""
class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ['id_modelo', 'nombre_modelo']

        
# Serializador para Pedidos
class PedidoSerializer(serializers.ModelSerializer):
    cliente = serializers.CharField(
        source='id_cliente.nombre', 
        read_only=True,
        help_text="Nombre del cliente"
    )
    modelo = serializers.CharField(
        source='id_modelo.nombre_modelo', 
        read_only=True,
        help_text="Nombre del modelo"
    )
    numero_pedido = serializers.SerializerMethodField(
        read_only=True,
        help_text="Número de pedido formateado"
    )
    
    # Campos para escritura
    id_cliente = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(), 
        write_only=True,
        help_text="ID del cliente asociado"
    )
    id_modelo = serializers.PrimaryKeyRelatedField(
        queryset=Modelo.objects.all(), 
        write_only=True,
        help_text="ID del modelo asociado"
    )

    class Meta:
        model = Pedido
        fields = [
            'id_pedido', 'numero_pedido', 'cliente', 'modelo',
            'id_cliente', 'id_modelo', 'cantidad', 'fecha_pedido',
            'total', 'estado', 'created_at'
        ]
        read_only_fields = ['id_pedido', 'created_at', 'total']

    def get_numero_pedido(self, obj):
        return f"#{obj.id_pedido}"

    def validate_fecha_pedido(self, value):
        """
        Valida que la fecha del pedido no sea en el futuro
        """
        if value > datetime.now().date():
            raise serializers.ValidationError("La fecha del pedido no puede ser en el futuro")
        return value

    def create(self, validated_data):
        # Calcula el total basado en el modelo y cantidad
        modelo = validated_data['id_modelo']
        cantidad = validated_data['cantidad']
        validated_data['total'] = modelo.precio_base * cantidad
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Si cambia el modelo o cantidad, recalcula el total
        if 'id_modelo' in validated_data or 'cantidad' in validated_data:
            modelo = validated_data.get('id_modelo', instance.id_modelo)
            cantidad = validated_data.get('cantidad', instance.cantidad)
            validated_data['total'] = modelo.precio_base * cantidad
        return super().update(instance, validated_data)

# Serializador para Reporte de Ventas
class ReporteVentasSerializer(serializers.Serializer):
    fecha_inicio = serializers.DateField(
        required=True,
        help_text="Fecha de inicio del reporte (YYYY-MM-DD)"
    )
    fecha_fin = serializers.DateField(
        required=True,
        help_text="Fecha de fin del reporte (YYYY-MM-DD)"
    )
    agrupar_por = serializers.ChoiceField(
        choices=[
            ('dia', 'Día'),
            ('semana', 'Semana'),
            ('mes', 'Mes'),
            ('modelo', 'Modelo')
        ],
        default='mes',
        help_text="Criterio para agrupar los resultados"
    )