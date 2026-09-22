import joblib
import pandas as pd


def load_model(
    model_path="../models/anomaly_detector.pkl"
):
    """
    Carga el modelo entrenado y sus variables.
    """

    model_package = joblib.load(
        model_path
    )

    model = model_package["model"]
    features = model_package["features"]

    return model, features



def get_feature_importance(
    model,
    features,
    top_n=5
):
    """
    Obtiene las variables más importantes
    utilizadas por el modelo.
    """

    importance = pd.DataFrame(
        {
            "feature": features,
            "importance": model.feature_importances_
        }
    )


    importance = importance.sort_values(
        by="importance",
        ascending=False
    )


    return importance.head(top_n)



def predict_anomaly(
    sensor_data,
    model_path="../models/anomaly_detector.pkl"
):
    """
    Predice anomalías y genera una respuesta
    estructurada para aplicaciones y LLM.

    Entrada:
    sensor_data -> DataFrame con variables del sensor

    Salida:
    diccionario con información de diagnóstico
    """


    # ==========================
    # Cargar modelo
    # ==========================

    model, features = load_model(
        model_path
    )


    # ==========================
    # Preparar datos
    # ==========================

    X = sensor_data[features]


    # ==========================
    # Predicción
    # ==========================

    prediction = model.predict(
        X
    )[0]


    probability = model.predict_proba(
        X
    )[0]


    anomaly_probability = float(
        probability[1]
    )


    # ==========================
    # Nivel de riesgo
    # ==========================

    if anomaly_probability >= 0.8:
        risk_level = "High"

    elif anomaly_probability >= 0.5:
        risk_level = "Medium"

    else:
        risk_level = "Low"



    # ==========================
    # Factores principales
    # ==========================

    important_features = get_feature_importance(
        model,
        features,
        top_n=5
    )


    main_factors = (
        important_features
        .to_dict(
            orient="records"
        )
    )


    # ==========================
    # Resultado final
    # ==========================

    result = {

        "prediction": int(prediction),

        "status": (
            "Anomaly detected"
            if prediction == 1
            else "Normal operation"
        ),

        "anomaly_probability": round(
            anomaly_probability,
            4
        ),

        "risk_level": risk_level,

        "main_factors": main_factors
    }


    return result