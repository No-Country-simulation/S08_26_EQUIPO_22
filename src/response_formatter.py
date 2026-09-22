import json


def format_llm_response(
    diagnosis,
    equipment_id="MGG001"
):
    """
    Convierte el diagnóstico del modelo
    en un formato estructurado para un LLM.
    """


    response = {

        "equipment": equipment_id,

        "condition": diagnosis["condition"],

        "risk_level": diagnosis.get(
            "risk_level",
            "Low"
        ),

        "confidence": diagnosis.get(
            "confidence",
            0
        ),

        "main_indicators": diagnosis.get(
            "main_indicators",
            []
        ),

        "technical_message": diagnosis["message"]

    }


    return response



def response_to_json(response):
    """
    Convierte la respuesta a JSON.
    Útil para APIs o integración con LLM.
    """

    return json.dumps(
        response,
        indent=4,
        ensure_ascii=False
    )