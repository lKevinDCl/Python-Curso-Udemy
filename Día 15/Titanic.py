# titanic_decision_tree.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# 1. Cargar el dataset
df = pd.read_csv("DataSet_Titanic.csv")  # Asegúrate de tener el archivo en el mismo directorio

# 2. Separar variables predictoras (X) y etiqueta (y)
X = df.drop("Sobreviviente", axis=1)
y = df["Sobreviviente"]

# 3. Visualizar X e y
print("X:\n", X.head())
print("\ny:\n", y.head())

# 4. Crear el modelo de árbol de decisión
modelo = DecisionTreeClassifier()

# 5. Entrenar el modelo
modelo.fit(X, y)

# 6. Realizar predicciones
y_pred = modelo.predict(X)

# 7. Evaluar precisión
accuracy = accuracy_score(y, y_pred)
print(f"\nPrecisión del modelo: {accuracy:.4f}")

# 8. Matriz de confusión
matriz = confusion_matrix(y, y_pred)
print("\nMatriz de confusión:\n", matriz)

# 9. Visualizar matriz de confusión
ConfusionMatrixDisplay(confusion_matrix=matriz).plot()
plt.title("Matriz de Confusión")
plt.show()

# 10. Matriz de confusión normalizada
ConfusionMatrixDisplay.from_predictions(y, y_pred, normalize='true')
plt.title("Matriz de Confusión Normalizada")
plt.show()

# 11. Visualizar el árbol de decisión
plt.figure(figsize=(12, 8))
plot_tree(modelo, feature_names=X.columns, class_names=["No", "Sí"], filled=True)
plt.title("Árbol de Decisión - Titanic")
plt.show()

# 12. Importancia de atributos
importancias = modelo.feature_importances_
features = X.columns

plt.figure(figsize=(8, 4))
plt.barh(features, importancias, color="teal")
plt.xlabel("Importancia")
plt.title("Importancia de cada atributo en la predicción")
plt.show()
