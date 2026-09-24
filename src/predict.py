# ============================================================
# predict.py
# Predicción de anomalías del equipo
# ============================================================


import os
import joblib
import pandas as pd



# ============================================================
# Ruta absoluta del modelo
# ============================================================


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


DEFAULT_MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "anomaly_detector.pkl"
)



# ============================================================
# Cargar modelo
# ============================================================


def load_model(
    model_path=DEFAULT_MODEL_PATH
):

    """
    Carga el modelo entrenado y las features utilizadas.

    Retorna:
        model
        features
    """


    package = joblib.load(
        model_path
    )


    # El modelo fue guardado como diccionario
    # con modelo y lista de variables

    if isinstance(package, dict):

        model = package["model"]

        features = package["features"]


    else:

        # compatibilidad si se guardó solamente el modelo

        model = package

        features = None



    return model, features




# ============================================================
# Predicción de anomalía
# ============================================================


def predict_anomaly(
    sensor_data,
    model_path=DEFAULT_MODEL_PATH
):

    """
    Ejecuta la predicción del modelo ML.

    Entrada:

        sensor_data:
            DataFrame con variables del equipo


    Salida:

        Diccionario con resultado
    """



    # -------------------------------------
    # Convertir entrada si viene como dict
    # -------------------------------------

    if isinstance(
        sensor_data,
        dict
    ):


        sensor_data = pd.DataFrame(
            [
                sensor_data
            ]
        )



    # -------------------------------------
    # Cargar modelo
    # -------------------------------------


    model, features = load_model(
        model_path
    )



    # -------------------------------------
    # Validar variables
    # -------------------------------------


    missing_features = [

        feature

        for feature in features

        if feature not in sensor_data.columns

    ]



    if missing_features:


        raise ValueError(

            f"Faltan variables requeridas por el modelo: "
            f"{missing_features}"

        )



    # -------------------------------------
    # Preparar datos
    # -------------------------------------


    X = sensor_data[
        features
    ]



    # -------------------------------------
    # Predicción
    # -------------------------------------


    prediction = model.predict(
        X
    )[0]



    # -------------------------------------
    # Probabilidad
    # -------------------------------------


    if hasattr(
        model,
        "predict_proba"
    ):


        probabilities = model.predict_proba(
            X
        )[0]


        anomaly_probability = round(
            float(probabilities[1]),
            3
        )


    else:


        anomaly_probability = None



    # -------------------------------------
    # Nivel de riesgo
    # -------------------------------------


    if prediction == 1:


        if anomaly_probability >= 0.8:

            risk_level = "High"


        elif anomaly_probability >= 0.5:

            risk_level = "Medium"


        else:

            risk_level = "Low"



    else:

        risk_level = "Low"



    # -------------------------------------
    # Factores principales
    # -------------------------------------

    main_factors = []


    if hasattr(
        model,
        "feature_importances_"
    ):


        importances = model.feature_importances_



        ranked = sorted(

            zip(
                features,
                importances
            ),

            key=lambda x:x[1],

            reverse=True

        )



        for feature, importance in ranked[:5]:


            main_factors.append(

                {

                    "feature": feature,

                    "importance": round(

                        float(importance),

                        4

                    )

                }

            )



    # -------------------------------------
    # Resultado
    # -------------------------------------


    result = {


        "prediction":

            int(prediction),


        "status":

            (
                "Anomaly detected"

                if prediction == 1

                else

                "Normal operation"
            ),


        "anomaly_probability":

            anomaly_probability,


        "risk_level":

            risk_level,


        "main_factors":

            main_factors

    }



    return result




# ============================================================
# Prueba manual
# ============================================================


if __name__ == "__main__":


    test_sensor = {


        "vib_kurtosis":0.85,

        "vib_crest_factor":4.2,

        "efficiency_pct":78

    }


    print(

        predict_anomaly(
            test_sensor
        )

    )