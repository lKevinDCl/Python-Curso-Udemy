# pandas_practicas.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Crear una serie de números y hallar su media
serie_numeros = pd.Series([10, 20, 30, 40, 50])
print("Media:", serie_numeros.mean())

# 2. Suma de los números
print("Suma:", serie_numeros.sum())

# 3. Serie de colores
colores = pd.Series(["Rojo", "Verde", "Azul"])
print("\nSerie de colores:\n", colores)

# 4. Serie de tipos de autos
autos = pd.Series(["Sedán", "SUV", "Pickup"])
print("\nSerie de autos:\n", autos)

# 5. Combinar en un DataFrame
df_autos = pd.DataFrame({"Tipo": autos, "Color": colores})
print("\nDataFrame combinado:\n", df_autos)

# 6. Simulación de carga de CSV (usando datos ficticios)
data = {
    "Fabricante": ["Ford", "Chevrolet", "Toyota", "Ford", "Toyota"],
    "Modelo": ["Fiesta", "Onix", "Corolla", "Focus", "Yaris"],
    "Kilometraje": [120000, 95000, 80000, 150000, 70000],
    "Precio": ["$120,000", "$135,000", "$150,000", "$110,000", "$140,000"],
    "Puertas": [4, 4, 4, 2, 4]
}
df_ventas = pd.DataFrame(data)
print("\nDataFrame de ventas:\n", df_ventas)

# 7. Tipos de datos
print("\nTipos de datos:\n", df_ventas.dtypes)

# 8. Estadística descriptiva
print("\nDescripción estadística:\n", df_ventas.describe())

# 9. Información general
print("\nInfo del DataFrame:")
df_ventas.info()

# 10. Nombres de columnas
print("\nColumnas:", df_ventas.columns.tolist())

# 11. Largo del dataset
print("Cantidad de filas:", len(df_ventas))

# 12. Primeras y últimas filas
print("\nPrimeras 5 filas:\n", df_ventas.head())
print("\nPrimeras 7 filas:\n", df_ventas.head(7))
print("\nÚltimas 5 filas:\n", df_ventas.tail())

# 13. Selección con .loc y .iloc
print("\nFila con índice 3 (.loc):\n", df_ventas.loc[3])
print("\nFilas 3, 7 y 9 (.iloc):\n", df_ventas.iloc[[0, 1, 2]])  # Solo hay 5 filas

# 14. Selección de columna
print("\nColumna Kilometraje:\n", df_ventas["Kilometraje"])

# 15. Media de Kilometraje
print("Media de Kilometraje:", df_ventas["Kilometraje"].mean())

# 16. Filtro por kilometraje > 100,000
print("\nAutos con más de 100,000 km:\n", df_ventas[df_ventas["Kilometraje"] > 100000])

# 17. Tabla cruzada entre Fabricante y Puertas
tabla_cruzada = pd.crosstab(df_ventas["Fabricante"], df_ventas["Puertas"])
print("\nTabla cruzada:\n", tabla_cruzada)

# 18. Agrupación por Fabricante
agrupado = df_ventas.groupby("Fabricante").mean(numeric_only=True)
print("\nPromedios por fabricante:\n", agrupado)

# 19. Gráfico de Kilometraje
plt.figure(figsize=(8, 4))
plt.plot(df_ventas["Kilometraje"], marker='o')
plt.title("Kilometraje por vehículo")
plt.xlabel("Índice")
plt.ylabel("Kilometraje")
plt.grid(True)
plt.show()

# 20. Histograma de Kilometraje
plt.figure(figsize=(8, 4))
plt.hist(df_ventas["Kilometraje"], bins=5, color='skyblue', edgecolor='black')
plt.title("Distribución de Kilometraje")
plt.xlabel("Kilometraje")
plt.ylabel("Frecuencia")
plt.show()

# 21. Conversión de precios a números
df_ventas["Precio"] = df_ventas["Precio"].replace('[\$,]', '', regex=True).astype(float)
print("\nPrecios convertidos:\n", df_ventas["Precio"])

# 22. Gráfico de precios
plt.figure(figsize=(8, 4))
plt.plot(df_ventas["Precio"], marker='s', color='green')
plt.title("Precios de vehículos")
plt.xlabel("Índice")
plt.ylabel("Precio")
plt.grid(True)
plt.show()
