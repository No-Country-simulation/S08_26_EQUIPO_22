# ============================================================
# dashboard.py
# Dashboard principal MaintAI Copilot
# ============================================================


import streamlit as st

from pathlib import Path



from components.kpis import render_kpis


from components.filters import render_filters


from components.charts import (

    show_factor_importance,

    show_risk_chart,

    show_sensor_trend

)


from components.chat import render_chat





# ============================================================
# Banner principal animado GIF
# ============================================================


def render_banner():


    gif_path = Path(

        "assets/img3.gif"

    )


    image_path = Path(

        "assets/img2.png"

    )



    # --------------------------------------------------------
    # GIF principal
    # --------------------------------------------------------


    if gif_path.exists():


        st.image(

            str(gif_path),

            use_container_width=True

        )



    # --------------------------------------------------------
    # Imagen respaldo
    # --------------------------------------------------------


    elif image_path.exists():


        st.image(

            str(image_path),

            use_container_width=True

        )



    else:


        st.warning(

            "No se encontró assets/img3.gif ni assets/img2.png"

        )









# ============================================================
# Render Dashboard
# ============================================================


def render_dashboard(result, equipment):


    """
    Interfaz principal MaintAI Copilot
    """



    # ========================================================
    # Guardar diagnóstico en sesión
    # ========================================================


    st.session_state["dashboard_result"] = result


    st.session_state["dashboard_equipment"] = equipment





    # ========================================================
    # Banner principal
    # ========================================================


    render_banner()



    st.divider()





    # ========================================================
    # KPIs
    # ========================================================


    render_kpis(

        result,

        equipment

    )



    st.write("")





    # ========================================================
    # Distribución principal
    # ========================================================


    dashboard_col, chat_col = st.columns(

        [7,5],

        gap="large"

    )





    # ========================================================
    # Dashboard analítico
    # ========================================================


    with dashboard_col:



        st.subheader(

            "📊 Monitor del activo"

        )





        # ----------------------------------------------------
        # Filtros
        # ----------------------------------------------------


        filters = render_filters()





        st.divider()





        # ----------------------------------------------------
        # Tendencia operacional
        # ----------------------------------------------------


        st.subheader(

            "📈 Tendencia operacional"

        )



        show_sensor_trend(

            variable=filters["variable"],

            periodo=filters["periodo"]

        )





        st.write("")





        # ----------------------------------------------------
        # Factores y riesgo
        # ----------------------------------------------------


        col1, col2 = st.columns(2)





        prediction = result.get(

            "prediction",

            {}

        )





        factors = prediction.get(

            "main_factors",

            []

        )





        risk = prediction.get(

            "risk_level",

            "Low"

        )







        with col1:



            st.subheader(

                "🧠 Factores críticos"

            )



            show_factor_importance(

                factors

            )







        with col2:



            st.subheader(

                "⚠️ Estado del riesgo"

            )



            show_risk_chart(

                risk

            )








    # ========================================================
    # Chat IA
    # ========================================================


    with chat_col:



        st.markdown(

            """

            <div class="ai-card">

            """,

            unsafe_allow_html=True

        )



        st.markdown(

            "## 🤖 MaintAI Assistant"

        )



        st.caption(

            f"Copiloto del equipo {equipment}"

        )





        render_chat(

            result,

            equipment

        )





        st.markdown(

            """

            </div>

            """,

            unsafe_allow_html=True

        )