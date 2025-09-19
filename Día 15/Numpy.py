import numpy as np
import pandas as pd

# 1. Crear arrays de distintas dimensiones
array_1d = np.array([1, 2, 3])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_3d = np.array([[[1], [2], [3]], [[4], [5], [6]]])

# 2. Atributos de los arrays
print("Array 1D:", array_1d.shape, array_1d.ndim, array_1d.dtype, array_1d.size, type(array_1d))
print("Array 2D:", array_2d.shape, array_2d.ndim, array_2d.dtype, array_2d.size, type(array_2d))
print("Array 3D:", array_3d.shape, array_3d.ndim, array_3d.dtype, array_3d.size, type(array_3d))

# 3. Convertir array en DataFrame
df = pd.DataFrame(array_2d)
print("\nDataFrame:\n", df)

# 4. Arrays con unos, ceros y rangos
array_ones = np.ones((4, 3))
array_zeros = np.zeros((2, 4, 3))
array_range = np.arange(0, 101, 5)

# 5. Arrays aleatorios
array_randint = np.random.randint(0, 10, (2, 5))
array_randfloat = np.random.rand(3, 5)

# 6. Semilla y reproducibilidad
np.random.seed(27)
array_seeded = np.random.randint(0, 10, (3, 5))

# 7. Indexación y slicing
array_4 = array_seeded
print("\nValores únicos:", np.unique(array_4))
print("Fila 1:", array_4[1])
print("Primeras dos filas:\n", array_4[:2])
print("Primeros dos elementos de las dos primeras filas:\n", array_4[:2, :2])

# 8. Operaciones entre arrays
array_5 = np.random.randint(0, 10, (3, 4))
array_6 = np.ones((3, 4))
array_sum = array_5 + array_6

# 9. Error por forma incompatible (comentado para evitar crash)
array_7 = np.ones((4, 3))
# array_6 + array_7  # Esto da error

# 10. Resta y operaciones matemáticas
array_8 = np.ones((4, 3))
array_sub = array_8 - array_7

array_9 = np.random.randint(1, 6, (3, 3))
array_10 = np.random.randint(1, 6, (3, 3))

array_mul = array_9 * array_10
array_sq = array_9 ** 2
array_sqrt = np.sqrt(array_10)

# 11. Estadísticas
print("\nPromedio:", np.mean(array_9))
print("Máximo:", np.max(array_9))
print("Mínimo:", np.min(array_9))

# 12. Reshape y transposición
array_11 = array_9.reshape(9, 1)
print("\nArray 11:\n", array_11)
print("Transpuesto:\n", array_11.T)

# 13. Comparaciones lógicas
comparison = array_9 > array_10
print("\nComparación array_9 > array_10:\n", comparison)
print("Tipo de datos:", comparison.dtype)

equal_check = array_9 == array_10
greater_equal = array_9 >= array_10
greater_than_2 = array_9 > 2
sorted_array = np.sort(array_9, axis=None)

print("\n¿Algún elemento igual?:\n", equal_check)
print("¿Mayor o igual?:\n", greater_equal)
print("¿Mayor que 2?:\n", greater_than_2)
print("Ordenado:\n", sorted_array)
