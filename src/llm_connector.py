# ============================================================
# llm_connector.py
# MaintAI Copilot + Ollama
# ============================================================


import json

import streamlit as st

import numpy as np


from langchain_ollama import ChatOllama





# ============================================================
# Conversión datos ML
# ============================================================


def convert_numpy(obj):


    if isinstance(obj, np.generic):

        return obj.item()



    if isinstance(obj, dict):

        return {

            key: convert_numpy(value)

            for key, value in obj.items()

        }




    if isinstance(obj, list):

        return [

            convert_numpy(item)

            for item in obj

        ]



    return obj





# ============================================================
# Crear modelo Ollama
# ============================================================


@st.cache_resource
def create_llm():


    return ChatOllama(


        model="phi3:mini",


        temperature=0.1,


        num_predict=300,


        keep_alive="30m"


    )






# ============================================================
# Consulta IA
# ============================================================


def ask_llm(


    diagnosis,


    question=None,


    history=None


):


    try:


        llm = create_llm()





        # ------------------------------------
        # Normalización datos ML
        # ------------------------------------


        diagnosis = convert_numpy(

            diagnosis

        )




        diagnosis_json = json.dumps(


            diagnosis,


            indent=2,


            ensure_ascii=False


        )





        # ------------------------------------
        # Información prioritaria del modelo ML
        # ------------------------------------


        prediction = diagnosis.get(

            "prediction",

            {}

        )



        ml_summary = {


            "risk_level": prediction.get(

                "risk_level",

                "No disponible"

            ),


            "main_factors": prediction.get(

                "main_factors",

                []

            ),


            "anomaly_probability": prediction.get(

                "anomaly_probability",

                "No disponible"

            )

        }




        ml_summary_json = json.dumps(


            ml_summary,


            indent=2,


            ensure_ascii=False


        )






        # ------------------------------------
        # Historial conversación
        # ------------------------------------


        history_text = ""



        if history:


            history_text = json.dumps(


                history[-4:],


                ensure_ascii=False


            )






        if question is None:


            question = (

                "Realiza un diagnóstico técnico del equipo."

            )







        # ------------------------------------
        # Prompt MaintAI
        # ------------------------------------


        prompt = f"""

Eres MaintAI Copilot.

Actúa como ingeniero especialista en mantenimiento predictivo industrial.



Tu función es interpretar resultados de Machine Learning

para apoyar decisiones técnicas de mantenimiento.



================================

RESULTADO PRIORITARIO DEL MODELO ML

================================


{ml_summary_json}



================================

INFORMACIÓN COMPLETA DEL EQUIPO

================================


{diagnosis_json}



================================

HISTORIAL DE CONVERSACIÓN

================================


{history_text}



================================

PREGUNTA DEL USUARIO

================================


{question}




Genera una respuesta técnica estructurada:



1. Estado actual del equipo.

2. Nivel de riesgo.

3. Variables críticas detectadas.

4. Posibles causas técnicas.

5. Acción recomendada de mantenimiento.





Reglas obligatorias:



- Usa únicamente los datos entregados.

- No inventes mediciones.

- No agregues variables inexistentes.

- Analiza siempre main_factors del modelo ML.

- Si existen factores críticos debes mencionarlos.

- Nunca digas que no existen variables críticas si main_factors contiene información.

- Diferencia entre estado normal del equipo y variables influyentes.

- Responde como ingeniero de mantenimiento industrial.

- No uses HTML.

- No escribas código.

- Sé claro y técnico.







"""






        # ------------------------------------
        # Debug prompt
        # ------------------------------------


        print(

            "\n===== PROMPT ENVIADO A OLLAMA ====="

        )


        print(

            prompt[:4000]

        )


        print(

            "===================================\n"

        )







        # ------------------------------------
        # Ejecución Ollama
        # ------------------------------------


        response = llm.invoke(

            prompt

        )







        # ------------------------------------
        # Debug respuesta
        # ------------------------------------


        print(

            "\n===== RESPUESTA OLLAMA ====="

        )


        print(

            response

        )


        print(

            "============================\n"

        )







        # ------------------------------------
        # Retorno limpio
        # ------------------------------------


        if hasattr(response, "content"):


            answer = str(

                response.content

            ).strip()



            print(

                "===== TEXTO DEVUELTO ====="

            )


            print(

                answer

            )


            print(

                "=========================="

            )



            return answer





        return str(response).strip()







    except Exception as error:



        print(

            "ERROR OLLAMA:",

            error

        )



        return (

            "⚠️ Error conectando con MaintAI: "

            + str(error)

        )