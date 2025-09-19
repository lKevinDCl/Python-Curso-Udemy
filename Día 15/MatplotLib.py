# matplotlib_practicas.py

import matplotlib.pyplot as plt
import numpy as np

# 1. Gráfico simple con plt.plot()
plt.plot([1, 2, 3, 4, 5])
plt.title("Gráfico simple")
plt.show()

# 2. Graficar una lista de números
numeros = [10, 20, 30, 40, 50]
plt.plot(numeros)
plt.title("Lista de números")
plt.show()

# 3. Graficar x vs x²
x = list(range(1, 101))
y = [i**2 for i in x]
plt.plot(x, y)
plt.title("x vs x²")
plt.xlabel("x")
plt.ylabel("x²")
plt.grid(True)
plt.show()

# 4. Método orientado a objetos
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Gráfico OO x vs x²")
ax.set_xlabel("x")
ax.set_ylabel("x²")
plt.show()

# 5. Flujo completo con subplots
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Título del gráfico")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
fig.savefig("grafico_guardado.png")
plt.show()

# 6. Gráfico de dispersión con datos aleatorios
x_rand = np.random.rand(100)
y_rand = np.random.rand(100)
plt.scatter(x_rand, y_rand)
plt.title("Gráfico de dispersión")
plt.show()

# 7. Función seno
X = np.linspace(0, 10, 100)
Y = np.sin(X)
plt.plot(X, Y)
plt.title("Función seno")
plt.grid(True)
plt.show()

# 8. Gráfico de barras
precios = {"Pizza": 80, "Hamburguesa": 60, "Ensalada": 40}
plt.bar(precios.keys(), precios.values())
plt.title("Precios de comidas")
plt.xlabel("Comida")
plt.ylabel("Precio")
plt.show()

# 9. Gráfico de barras horizontales
plt.barh(list(precios.keys()), list(precios.values()))
plt.title("Precios de comidas (horizontal)")
plt.xlabel("Precio")
plt.ylabel("Comida")
plt.show()

# 10. Histograma de distribución normal
valores = np.random.randn(1000)
plt.hist(valores, bins=30, color='skyblue', edgecolor='black')
plt.title("Histograma de distribución normal")
plt.show()

# 11. Subplots múltiples
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x[:10], y[:10])
axs[0, 1].scatter(x_rand[:10], y_rand[:10])
axs[1, 0].bar(precios.keys(), precios.values())
axs[1, 1].hist(valores, bins=20)
fig.suptitle("Subplots múltiples")
plt.tight_layout()
plt.show()

# 12. Subplots con tamaño personalizado
x_1 = list(range(10))
y_1 = [i**2 for i in x_1]
x_2 = np.random.rand(10)
y_2 = np.random.rand(10)
valores_hist = np.random.randn(1000)

fig, axs = plt.subplots(2, 2, figsize=(10, 5))
axs[0, 0].plot(x_1, y_1, color="#FF5733")
axs[0, 1].scatter(x_2, y_2, color="#33C1FF")
axs[1, 0].bar(precios.keys(), precios.values(), color="#75FF33")
axs[1, 1].hist(valores_hist, bins=30, color="#FFC300")
fig.suptitle("Subplots con colores personalizados")
plt.tight_layout()
plt.show()

# 13. Ver estilos disponibles
print("Estilos disponibles:", plt.style.available)

# 14. Cambiar estilo a seaborn-whitegrid
plt.style.use("seaborn-whitegrid")
plt.plot(x_1, y_1, color="#FF5733")
plt.title("Estilo seaborn-whitegrid")
plt.show()
