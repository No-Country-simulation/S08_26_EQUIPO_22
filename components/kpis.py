# ============================================================
# kpis.py
# Tarjetas KPI del activo
# ============================================================


import streamlit as st



def calculate_health(probability):


    if probability is None:

        return "N/A"



    health = (

        1 - probability

    ) * 100



    return f"{health:.1f}%"




def translate_status(status):


    values = {


        "Normal operation":

            "🟢 Normal",


        "Anomaly detected":

            "🔴 Anomalía"

    }


    return values.get(

        status,

        status

    )




def translate_risk(risk):


    values = {


        "Low":

            "🟢 Bajo",


        "Medium":

            "🟡 Medio",


        "High":

            "🔴 Alto"

    }


    return values.get(

        risk,

        risk

    )





def render_kpis(result, equipment):


    prediction = result.get(

        "prediction",

        {}

    )



    status = translate_status(

        prediction.get(

            "status",

            ""

        )

    )



    risk = translate_risk(

        prediction.get(

            "risk_level",

            ""

        )

    )



    probability = prediction.get(

        "anomaly_probability"

    )



    probability_text = (

        f"{probability*100:.1f}%"

        if probability is not None

        else "N/A"

    )



    health = calculate_health(

        probability

    )



    col1,col2,col3,col4 = st.columns(4)



    with col1:


        st.metric(

            "Estado",

            status

        )



    with col2:


        st.metric(

            "Riesgo",

            risk

        )



    with col3:


        st.metric(

            "Probabilidad falla",

            probability_text

        )



    with col4:


        st.metric(

            "Salud activo",

            health

        )