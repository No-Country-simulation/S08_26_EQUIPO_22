# diagnosis.py
# Generación de diagnóstico técnico enriquecido
# usando la base de conocimiento industrial


from src.knowledge_base import MAINTENANCE_KNOWLEDGE



def generate_diagnosis(
    prediction_result,
    equipment="MGG001"
):
    """
    Convierte la salida del modelo ML en un diagnóstico
    técnico enriquecido para el LLM.

    Parámetros:
        prediction_result:
            Resultado generado por predict.py

        equipment:
            Identificador del equipo

    Retorna:
        Diccionario con diagnóstico + conocimiento técnico
    """


    # ==============================
    # Extraer datos de predicción
    # ==============================

    prediction = prediction_result.get(
        "prediction",
        0
    )


    probability = prediction_result.get(
        "anomaly_probability",
        0
    )


    risk_level = prediction_result.get(
        "risk_level",
        "Unknown"
    )


    # ==============================
    # Caso operación normal
    # ==============================

    if prediction == 0:

        return {

            "equipment": equipment,

            "condition":
                "Normal operation",

            "risk_level":
                "Low",

            "confidence":
                round(
                    1 - probability,
                    3
                ),

            "indicators":
                {},

            "technical_message":
                (
                    "El equipo presenta condiciones "
                    "operativas normales según el modelo "
                    "predictivo."
                ),

            "recommendation":
                (
                    "Continuar monitoreo periódico "
                    "de las variables críticas."
                )
        }



    # ==============================
    # Caso anomalía detectada
    # ==============================


    enriched_indicators = {}


    main_factors = prediction_result.get(
        "main_factors",
        []
    )


    for factor in main_factors:

        feature = factor.get(
            "feature"
        )


        importance = factor.get(
            "importance",
            0
        )


        # Buscar conocimiento técnico

        knowledge = MAINTENANCE_KNOWLEDGE.get(
            feature,
            {}
        )


        enriched_indicators[feature] = {

            "importance":
                round(
                    importance,
                    4
                ),

            "meaning":
                knowledge.get(
                    "meaning",
                    "Sin descripción técnica disponible."
                ),


            "possible_causes":
                knowledge.get(
                    "possible_causes",
                    []
                ),


            "recommended_actions":
                knowledge.get(
                    "recommended_actions",
                    []
                )
        }



    # ==============================
    # Construir diagnóstico final
    # ==============================


    diagnosis = {


        "equipment":
            equipment,


        "condition":
            "Anomaly detected",


        "risk_level":
            risk_level,


        "confidence":
            probability,


        "indicators":
            enriched_indicators,


        "technical_message":
            (
                "Se detectó una condición anómala "
                "en el equipo. Los indicadores críticos "
                "fueron enriquecidos con conocimiento "
                "de mantenimiento predictivo."
            ),


        "priority_action":
            (
                "Realizar inspección técnica de los "
                "componentes asociados antes de una "
                "posible falla funcional."
            )

    }


    return diagnosis