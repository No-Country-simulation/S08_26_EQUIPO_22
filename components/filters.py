# ============================================================
# filters.py
# Filtros Dashboard MaintAI Copilot
# ============================================================


import streamlit as st




# ============================================================
# Render filtros
# ============================================================


def render_filters():


    st.subheader(

        "🎛️ Filtros de análisis"

    )



    col1, col2, col3 = st.columns(3)



    # --------------------------------------------------------
    # Variable
    # --------------------------------------------------------


    with col1:


        variable = st.selectbox(

            "Variable monitoreada",

            [

                "Todas",

                "Vibración",

                "Temperatura",

                "Lubricación",

                "Eficiencia",

                "Carga eléctrica"

            ],

            key="variable_filter"

        )



    # --------------------------------------------------------
    # Periodo
    # --------------------------------------------------------


    with col2:


        periodo = st.selectbox(

            "Periodo",

            [

                "Actual",

                "Últimas 24 horas",

                "Últimos 7 días",

                "Último mes"

            ],

            key="periodo_filter"

        )



    # --------------------------------------------------------
    # Riesgo
    # --------------------------------------------------------


    with col3:


        riesgo = st.selectbox(

            "Nivel de riesgo",

            [

                "Todos",

                "Bajo",

                "Medio",

                "Alto"

            ],

            key="riesgo_filter"

        )



    # --------------------------------------------------------
    # Retornar filtros
    # --------------------------------------------------------


    return {


        "variable": variable,


        "periodo": periodo,


        "riesgo": riesgo


    }