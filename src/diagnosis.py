def generate_diagnosis(prediction_result):
    """
    Genera una interpretación técnica
    basada en la predicción del modelo.
    """

    if prediction_result["prediction"] == 0:

        diagnosis = {
            "condition": "Normal",
            "message": (
                "El equipo opera dentro de condiciones normales "
                "según los patrones aprendidos por el modelo."
            )
        }

    else:

        factors = [
            item["feature"]
            for item in prediction_result["main_factors"]
        ]

        diagnosis = {
            "condition": "Anomaly detected",

            "risk_level": prediction_result["risk_level"],

            "confidence": prediction_result[
                "anomaly_probability"
            ],

            "main_indicators": factors,

            "message": (
                "Se detectó una condición anómala. "
                "Los principales indicadores asociados "
                "corresponden a variables de vibración "
                "y desempeño del equipo."
            )
        }


    return diagnosis