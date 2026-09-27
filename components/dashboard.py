# ============================================================
# dashboard.py
# Dashboard Industrial MaintAI Copilot
# ============================================================


import streamlit as st


# Componentes internos

from components.kpis import render_kpis


from components.filters import render_filters


from components.charts import (

    show_factor_importance,

    show_risk_chart,

    show_sensor_trend

)



# ============================================================
# Render Dashboard
# ============================================================


def render_dashboard(result, equipment):


    """
    Renderiza el dashboard principal
    del sistema de mantenimiento predictivo.
    """



    try:


        # ====================================================
        # Validación
        # ====================================================


        if result is None:


            st.warning(

                "No existen resultados del análisis."

            )


            return



        prediction = result.get(

            "prediction",

            {}

        )



        # ====================================================
        # Encabezado
        # ====================================================


        st.subheader(

            f"📊 Dashboard del equipo {equipment}"

        )



        st.caption(

            "Sistema inteligente de mantenimiento predictivo basado en Machine Learning + IA"

        )



        st.divider()



        # ====================================================
        # KPIs
        # ====================================================


        render_kpis(

            result,

            equipment

        )



        st.divider()



        # ====================================================
        # FILTROS
        # ====================================================


        filters = render_filters()



        st.divider()



        # ====================================================
        # GRÁFICOS
        # ====================================================


        st.subheader(

            "📈 Análisis operacional"

        )



        chart1, chart2 = st.columns(2)



        with chart1:


            show_sensor_trend(

                filters=filters

            )



        with chart2:


            show_risk_chart(

                prediction.get(

                    "risk_level",

                    "Low"

                )

            )



        st.divider()



        # ====================================================
        # VARIABLES CRÍTICAS
        # ====================================================


        st.subheader(

            "🔎 Variables críticas detectadas"

        )



        factors = prediction.get(

            "main_factors",

            []

        )



        show_factor_importance(

            factors

        )



        st.divider()



        # ====================================================
        # INTERPRETACIÓN IA
        # ====================================================


        st.subheader(

            "🤖 Interpretación inteligente"

        )



        ai_report = result.get(

            "ai_report"

        )



        if ai_report:


            st.success(

                ai_report

            )


        else:


            st.info(

                "El asistente IA generará la explicación técnica del diagnóstico."

            )



        st.divider()



        # ====================================================
        # INFORMACIÓN TÉCNICA
        # ====================================================


        with st.expander(

            "⚙️ Información técnica del análisis"

        ):



            col1, col2 = st.columns(2)



            with col1:


                st.write(

                    "**Equipo:**",

                    equipment

                )


                st.write(

                    "**Estado:**",

                    prediction.get(

                        "status",

                        "N/A"

                    )

                )



            with col2:


                st.write(

                    "**Riesgo:**",

                    prediction.get(

                        "risk_level",

                        "N/A"

                    )

                )


                st.write(

                    "**Probabilidad anomalía:**",

                    prediction.get(

                        "anomaly_probability",

                        "N/A"

                    )

                )



    except Exception as e:


        st.error(

            f"Error renderizando dashboard: {e}"

        )