import pandas as pd
import joblib
import os

def predecir_demanda(id_modelo, year, month):
    modelo_path = os.path.join("ml_api", "modelo_rf.joblib")
    model = joblib.load(modelo_path)

    df_input = pd.DataFrame([{
        'id_modelo': id_modelo,
        'year': year,
        'month': month
    }])

    # Asegura que las columnas estén en el orden que espera el modelo
    df_input = df_input.reindex(columns=model.feature_names_in_, fill_value=0)

    prediccion = model.predict(df_input)[0]

    return prediccion
