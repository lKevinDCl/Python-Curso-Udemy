import pandas as pd
from django.db import connection

def obtener_series_temporales():
    query = """
        SELECT 
            p.id_modelo,
            m.nombre_modelo,
            m.genero,
            m.precio_base,
            m.year_introduced,
            DATE_FORMAT(p.fecha_pedido, '%Y-%m') AS mes,
            SUM(p.cantidad) AS total_pedidos
        FROM pedidos p
        JOIN modelos m ON p.id_modelo = m.id_modelo
        GROUP BY 
            p.id_modelo, 
            m.nombre_modelo,
            m.genero,
            m.precio_base,
            m.year_introduced,
            mes
        ORDER BY p.id_modelo, mes;
    """

    # Ejecutar el query y cargar en DataFrame
    df = pd.read_sql(query, connection)

    print("Primeras filas del DataFrame sin procesar:")
    print(df.head())

    # Convertir la columna 'mes' en datetime con formato específico
    try:
        df['mes'] = pd.to_datetime(df['mes'], format='%Y-%m')
    except Exception as e:
        print(f"Error al convertir fechas con formato '%Y-%m': {e}")
        print("Intentando conversión forzada con errors='coerce'")
        df['mes'] = pd.to_datetime(df['mes'], errors='coerce')  # Forzar parsing, NaT si no puede

    # Eliminar filas con fechas inválidas
    filas_invalidas = df['mes'].isna().sum()
    if filas_invalidas > 0:
        print(f"Se eliminaron {filas_invalidas} filas con fechas inválidas")

    df = df.dropna(subset=['mes'])

    print(f"DataFrame final listo para usar: {len(df)} filas")
    print("Tipos de datos:\n", df.dtypes)

    return df
