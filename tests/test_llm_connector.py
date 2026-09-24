# ============================================================
# test_llm_connector.py
# Prueba del conector LLM con Ollama
# ============================================================


import sys
import os


sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)


from src.llm_connector import ask_llm



# ============================================================
# Prueba conexión LLM
# ============================================================


def test_llm_response():


    diagnosis = {

        "equipment": "MGG001",

        "condition": "Anomaly detected",

        "risk_level": "High",

        "confidence": 0.97,

        "main_indicators": [

            "vib_kurtosis",

            "vib_crest_factor"

        ]

    }


    response = ask_llm(
        diagnosis
    )


    assert response is not None

    assert isinstance(
        response,
        str
    )

    assert len(response) > 20