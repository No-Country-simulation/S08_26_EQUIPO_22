# ============================================================
# llm_connector.py
# Conexión entre diagnóstico predictivo y Ollama LLM
# ============================================================


import json

from langchain_ollama import ChatOllama



def create_llm():
    """
    Crea la conexión con el modelo local Ollama.
    """

    llm = ChatOllama(
        model="phi3:mini",
        temperature=0.1,
        num_predict=400
    )

    return llm



def ask_llm(diagnosis):
    """
    Envía un diagnóstico enriquecido al modelo LLM.

    Parámetro:
        diagnosis:
            Diccionario generado por diagnosis.py

    Retorna:
        Respuesta técnica generada por Phi-3
    """


    llm = create_llm()


    # Convertimos el diagnóstico a texto JSON

    diagnosis_json = json.dumps(
        diagnosis,
        indent=4,
        ensure_ascii=False
    )


    prompt = f"""

Eres un ingeniero experto en mantenimiento predictivo industrial.

Analiza el siguiente diagnóstico generado por un modelo de
Machine Learning:

=========================
DIAGNÓSTICO DEL EQUIPO
=========================

{diagnosis_json}


Genera un informe técnico siguiendo exactamente esta estructura:


## 1. Estado del equipo

Indica si existe una condición normal o anómala.


## 2. Nivel de riesgo

Explica la criticidad encontrada.


## 3. Indicadores principales

Explica las variables que generaron la alerta
y qué significa cada una.


## 4. Posibles causas técnicas

Relaciona los indicadores con posibles fallas
mecánicas u operativas.


## 5. Recomendaciones de inspección

Indica qué debería revisar el personal
de mantenimiento.


## 6. Acción prioritaria

Indica la siguiente acción recomendada.


Reglas:

- Usa lenguaje técnico claro.
- No inventes datos.
- Utiliza únicamente la información entregada.
- Responde como un ingeniero de mantenimiento.


"""


    response = llm.invoke(
        prompt
    )


    return response.content



# ============================================================
# Prueba independiente
# ============================================================

if __name__ == "__main__":


    diagnosis_test = {


        "equipment": "MGG001",

        "condition":
            "Anomaly detected",

        "risk_level":
            "High",

        "confidence":
            0.97,


        "indicators": {


            "vib_kurtosis": {


                "meaning":
                    "Indicador estadístico asociado a impactos anormales de vibración.",


                "possible_causes":
                    [
                        "Desgaste de rodamiento",
                        "Holguras mecánicas"
                    ],


                "recommended_actions":
                    [
                        "Inspección de rodamientos",
                        "Análisis espectral de vibración"
                    ]
            }
        }
    }


    result = ask_llm(
        diagnosis_test
    )


    print(result)