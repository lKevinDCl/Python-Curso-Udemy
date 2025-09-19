import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from .utils.data_extraction import obtener_series_temporales

def entrenar_y_validar_modelo_demanda_nuevo():
    df = obtener_series_temporales()

    print("\nPrimeras filas del DataFrame sin procesar:")
    print(df.head())

    df['year'] = df['mes'].dt.year
    df['month'] = df['mes'].dt.month

    # Solo usamos los campos simplificados
    features = ['id_modelo', 'year', 'month']

    X = df[features]
    y = df['total_pedidos']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluación del modelo
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"\nEvaluación del modelo:")
    print(f" MSE (Error Cuadrático Medio): {mse:.2f}")
    print(f" MAE (Error Absoluto Medio): {mae:.2f}")
    print(f" R2 Score (Coeficiente de determinación): {r2:.2f}")

    # Guardar modelo
    path_modelo = os.path.join("ml_api", "modelo_rf.joblib")
    joblib.dump(model, path_modelo)
    print(f"\n Modelo entrenado y guardado en: {path_modelo}")