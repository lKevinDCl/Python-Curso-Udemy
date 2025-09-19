import os
import sys
from pathlib import Path
import random
from datetime import datetime
from faker import Faker
import pandas as pd
from django.db import transaction, connection
from django.db.utils import OperationalError


BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maquila_backend.settings')

import django
django.setup()

from ml_api.models import (Tela, Cierre, Hilo, Boton, Costura, 
                          Modelo, Cliente, Pedido)

fake = Faker('es_MX')

def verify_connection():
    try:
        connection.ensure_connection()
        print(" Conexión a MySQL exitosa")
        return True
    except OperationalError as e:
        print(f" Error de conexión: {e}")
        return False

def generate_seasonal_multiplier(month, genero):
    seasonal = {
        'dama': {
            1: 0.8, 2: 0.7, 3: 1.0, 4: 1.2, 5: 1.1, 
            6: 1.3, 7: 1.4, 8: 1.2, 9: 1.0, 10: 1.1, 11: 1.0, 12: 1.5
        },
        'caballero': {
            1: 0.9, 2: 0.8, 3: 1.1, 4: 1.0, 5: 1.0, 
            6: 1.2, 7: 1.3, 8: 1.1, 9: 0.9, 10: 1.0, 11: 1.2, 12: 1.3
        }
    }
    return seasonal[genero].get(month, 1.0)

def generate_trend_factor(year, year_introduced):
    years_since_launch = year - year_introduced
    if years_since_launch == 0: return 1.2
    elif years_since_launch == 1: return 1.5
    elif years_since_launch == 2: return 1.3
    elif years_since_launch == 3: return 1.0
    else: return max(0.5, 1.0 - (years_since_launch - 3) * 0.1)

def create_materials():
    telas = [
        {'nombre_tela': 'Denim Clásico', 'precio_por_metro': 45.50},
        {'nombre_tela': 'Denim Elástico', 'precio_por_metro': 55.75},
        {'nombre_tela': 'Denim Negro', 'precio_por_metro': 48.30},
        {'nombre_tela': 'Denim Lavado', 'precio_por_metro': 52.00},
        {'nombre_tela': 'Denim Orgánico', 'precio_por_metro': 65.20}
    ]
    for tela in telas:
        Tela.objects.get_or_create(**tela)
    
    cierres = [
        {'tipo_cierre': 'Cremallera Metalica', 'precio': 15.00},
        {'tipo_cierre': 'Cremallera Invisible', 'precio': 18.50},
        {'tipo_cierre': 'Botón Automático', 'precio': 12.00}
    ]
    for cierre in cierres:
        Cierre.objects.get_or_create(**cierre)
    
    hilos = [
        {'tipo_hilo': 'Algodón 30', 'precio': 8.50},
        {'tipo_hilo': 'Poliester 40', 'precio': 7.20}
    ]
    for hilo in hilos:
        Hilo.objects.get_or_create(**hilo)
    
    botones = [
        {'tipo_boton': 'Metalico', 'precio': 2.50},
        {'tipo_boton': 'Plastico', 'precio': 1.20}
    ]
    for boton in botones:
        Boton.objects.get_or_create(**boton)
    
    costuras = [
        {'tipo_costura': 'Recta', 'precio': 5.00},
        {'tipo_costura': 'Overlock', 'precio': 6.50}
    ]
    for costura in costuras:
        Costura.objects.get_or_create(**costura)

def create_jeans_models():
    modelos = [
        {'nombre_modelo': 'Skinny Fit', 'genero': 'dama', 'precio_base': 299.00, 'year_introduced': 2018},
        {'nombre_modelo': 'Straight Leg', 'genero': 'caballero', 'precio_base': 349.00, 'year_introduced': 2019},
        {'nombre_modelo': 'Bootcut', 'genero': 'dama', 'precio_base': 319.00, 'year_introduced': 2020},
        {'nombre_modelo': 'Relaxed Fit', 'genero': 'caballero', 'precio_base': 279.00, 'year_introduced': 2021},
        {'nombre_modelo': 'High Waist', 'genero': 'dama', 'precio_base': 329.00, 'year_introduced': 2022},
    ]
    
    created_models = []
    for modelo in modelos:
        modelo_data = {
            'nombre_modelo': modelo['nombre_modelo'],
            'genero': modelo['genero'],
            'precio_base': modelo['precio_base'],
            'year_introduced': modelo['year_introduced'],
            'tiene_bolsillos': random.random() > 0.3,
            'lleva_pretina': random.random() > 0.5,
            'lleva_deslavado': random.random() > 0.4,
            'lleva_planchado': random.random() > 0.6,
            'lleva_desgaste_extra': random.random() > 0.2,
            'activo': True
        }
        
        created_models.append(Modelo.objects.create(**modelo_data))
    
    return created_models

def generate_historical_orders(modelos, clientes):
    start_date = datetime(2018, 1, 1)
    end_date = datetime(2025, 7, 31)
    date_range = pd.date_range(start_date, end_date, freq='D')
    for single_date in date_range:
        day_of_week = single_date.weekday()
        month = single_date.month
        year = single_date.year
        
        if day_of_week in [5, 6]: 
            num_orders = random.choices([0, 1, 2], weights=[0.7, 0.2, 0.1])[0]
        else:  
            num_orders = random.choices([0, 1, 2, 3, 4], weights=[0.3, 0.3, 0.2, 0.1, 0.1])[0]

        if month in [6, 7, 8]:  
            num_orders = min(num_orders + 1, 4)
        elif month in [1, 2]: 
            num_orders = max(num_orders - 1, 0)
        
        for _ in range(num_orders):
            genero = random.choice(['dama', 'caballero'])
            modelos_filtrados = [m for m in modelos if m.genero == genero]
            modelo = random.choice(modelos_filtrados)
            
            seasonal_mult = generate_seasonal_multiplier(month, genero)
            trend_factor = generate_trend_factor(year, modelo.year_introduced)

            cantidad = random.randint(1, 20)
            precio_unitario = modelo.precio_base * seasonal_mult * trend_factor * random.uniform(0.9, 1.1)
            total = round(precio_unitario * cantidad, 2)
            
            Pedido.objects.create(
                id_cliente=random.choice(clientes),
                id_modelo=modelo,
                cantidad=cantidad,
                fecha_pedido=single_date.date(),
                total=total,
                estado='entregado'
            )




@transaction.atomic
def main():
    print("Generando datos históricos de 2018 a julio 2025...")
    if not verify_connection():
        return
    
    create_materials()
    modelos = create_jeans_models()
    clientes = [Cliente.objects.create(
        nombre=fake.company(),
        telefono=fake.phone_number(),
        direccion=fake.address()
    ) for _ in range(20)]
    
    generate_historical_orders(modelos, clientes)
    
    print("Datos generados exitosamente!")
    print(f"- Modelos creados: {Modelo.objects.count()}")
    print(f"- Pedidos históricos: {Pedido.objects.count()}")
    print(f"- Rango de fechas: {Pedido.objects.earliest('fecha_pedido').fecha_pedido} a {Pedido.objects.latest('fecha_pedido').fecha_pedido}")

if __name__ == '__main__':
    main()