import os
import sys
from pathlib import Path
from django.db import connection
from django.db.utils import OperationalError
from django.core.management.color import no_style
from django.db import connections

# Configuración inicial
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maquila_backend.settings')

import django
django.setup()

from ml_api.models import Tela

def verify_connection():
    """Verifica la conexión a la base de datos"""
    try:
        connection.ensure_connection()
        print("✅ Conexión a MySQL exitosa")
        return True
    except OperationalError as e:
        print(f"❌ Error de conexión: {e}")
        return False

def test_tela_insertion():
    """Prueba de inserción en la tabla telas"""
    print("\n=== PRUEBA DE INSERCIÓN EN TABLA TELAS ===")
    
    # Datos de prueba
    test_data = {
        'nombre_tela': 'Denim de Prueba',
        'precio_por_metro': 99.99
    }
    
    try:
        print("\n1. Insertando registro de prueba...")
        tela = Tela.objects.create(**test_data)
        print(f"✅ Registro insertado - ID: {tela.id_tela}")
        
        print("\n2. Verificando inserción...")
        tela_db = Tela.objects.get(id_tela=tela.id_tela)
        print(f"Registro obtenido de DB: {tela_db.nombre_tela} - ${tela_db.precio_por_metro}")
        
        print("\n3. Verificando consistencia...")
        assert tela_db.nombre_tela == test_data['nombre_tela']
        assert float(tela_db.precio_por_metro) == test_data['precio_por_metro']
        print("✅ Todos los valores coinciden")
        
        print("\n4. Registros actuales en la tabla:")
        for t in Tela.objects.all():
            print(f"ID: {t.id_tela} | {t.nombre_tela} | ${t.precio_por_metro}")
            
    except Exception as e:
        print(f"❌ Error durante la prueba: {str(e)}")
        raise
    finally:
        print("\n5. Limpiando datos de prueba...")
        Tela.objects.filter(nombre_tela=test_data['nombre_tela']).delete()
        remaining = Tela.objects.filter(nombre_tela=test_data['nombre_tela']).count()
        print(f"Registros eliminados. Verificación: {remaining} registros coincidentes encontrados")

def main():
    """Función principal"""
    print("Iniciando prueba de inserción...")
    
    if not verify_connection():
        return
    
    test_tela_insertion()
    
    print("\n✔ Prueba completada exitosamente")

if __name__ == '__main__':
    main()