# ============================================================
# pipeline.py
# Pipeline completo de mantenimiento predictivo con IA
# ============================================================


import pandas as pd


from src.predict import predict_anomaly
from src.diagnosis import generate_diagnosis
from src.llm_connector import ask_llm



def analyze_equipment(
    sensor_data,
    equipment="MGG001"
):
    """
    Ejecuta el flujo completo del sistema:

    1. Recibe datos del equipo
    2. Ejecuta modelo Machine Learning
    3. Genera diagnóstico técnico
    4. Consulta knowledge base
    5. Genera informe con LLM Ollama


    Parámetros:

        sensor_data:
            Diccionario o DataFrame con variables del equipo


        equipment:
            Código del equipo


    Retorna:

        Resultado completo del análisis

    """


    # ==========================================
    # PASO 1
    # Normalizar entrada de sensores
    # ==========================================


    if isinstance(sensor_data, dict):

        sensor_data = pd.DataFrame(
            [
                sensor_data
            ]
        )



    # ==========================================
    # PASO 2
    # Predicción Machine Learning
    # ==========================================


    prediction_result = predict_anomaly(

        sensor_data

    )



    # ==========================================
    # PASO 3
    # Diagnóstico técnico enriquecido
    # ==========================================


    diagnosis = generate_diagnosis(

        prediction_result,

        equipment=equipment

    )



    # ==========================================
    # PASO 4
    # Informe generado por Ollama
    # ==========================================


    ai_report = ask_llm(

        diagnosis

    )



    # ==========================================
    # PASO 5
    # Resultado final
    # ==========================================


    result = {


        "equipment":

            equipment,


        "prediction":

            prediction_result,


        "diagnosis":

            diagnosis,


        "ai_report":

            ai_report

    }


    return result





# ============================================================
# Prueba manual
# ============================================================

if __name__ == "__main__":


    sensor_test = {


        "vib_kurtosis":

            0.85,


        "vib_crest_factor":

            4.2,


        "efficiency_pct":

            78,


        "vib_peak_mm_s":

            8.5,


        "vib_overall_rms_mm_s":

            5.6

    }



    result = analyze_equipment(

        sensor_test,

        equipment="MGG001"

    )



    print("\n============================")
    print("PREDICCIÓN MODELO ML")
    print("============================")

    print(

        result["prediction"]

    )



    print("\n============================")
    print("DIAGNÓSTICO")
    print("============================")

    print(

        result["diagnosis"]

    )



    print("\n============================")
    print("INFORME IA")
    print("============================")

    print(

        result["ai_report"]

    )