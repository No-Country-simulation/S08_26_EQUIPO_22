# ============================================================
# filters.py
# Filtros dashboard
# ============================================================



import streamlit as st




def render_filters():


    st.subheader(

        "🎛️ Filtros"

    )


    col1,col2,col3 = st.columns(3)



    with col1:


        variable = st.selectbox(

            "Variable",

            [

                "Todas",

                "Vibración",

                "Temperatura",

                "Lubricación",

                "Eficiencia",

                "Carga eléctrica"

            ]

        )



    with col2:


        periodo = st.selectbox(

            "Periodo",

            [

                "Actual",

                "24 horas",

                "7 días",

                "30 días"

            ]

        )



    with col3:


        riesgo = st.selectbox(

            "Riesgo",

            [

                "Todos",

                "Bajo",

                "Medio",

                "Alto"

            ]

        )



    return {


        "variable": variable,

        "periodo": periodo,

        "riesgo": riesgo

    }