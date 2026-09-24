# ============================================================
# test_diagnosis.py
# Prueba del módulo de diagnóstico técnico
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


from src.diagnosis import generate_diagnosis



# ============================================================
# Test diagnóstico
# ============================================================


def test_diagnosis_generation():


    prediction_result = {


        "prediction": 1,


        "anomaly_probability": 0.97,


        "risk_level": "High",


        "main_factors": [

            {

                "feature": "vib_kurtosis",

                "importance": 0.2647

            },

            {

                "feature": "vib_crest_factor",

                "importance": 0.2304

            },

            {

                "feature": "efficiency_pct",

                "importance": 0.1981

            }

        ]

    }



    result = generate_diagnosis(

        prediction_result,

        equipment="MGG001"

    )



    assert "condition" in result

    assert "risk_level" in result

    assert "confidence" in result

    assert "indicators" in result