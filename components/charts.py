# ============================================================
# charts.py
# Gráficos MaintAI Copilot - Dark AI UI
# ============================================================


import pandas as pd
import plotly.express as px
import streamlit as st



# ============================================================
# Configuración visual Plotly
# ============================================================


def apply_theme(fig):


    fig.update_layout(


        template="plotly_dark",


        paper_bgcolor="rgba(0,0,0,0)",


        plot_bgcolor="rgba(0,0,0,0)",


        font=dict(

            color="#dfe2ef",

            family="Arial"

        ),


        margin=dict(

            l=20,

            r=20,

            t=50,

            b=20

        ),


        legend=dict(

            bgcolor="rgba(0,0,0,0)"

        )


    )


    return fig




# ============================================================
# Importancia variables
# ============================================================


def show_factor_importance(factors):


    if not factors:


        st.info(

            "No hay factores disponibles"

        )

        return



    df = pd.DataFrame(factors)



    df["importance_pct"] = (

        df["importance"] * 100

    )



    fig = px.bar(


        df,


        x="importance_pct",


        y="feature",


        orientation="h",


        title="🧠 Variables influyentes del diagnóstico",


        color="importance_pct",


        color_continuous_scale=[

            "#4cd7f6",

            "#8083ff"

        ]


    )



    fig.update_traces(


        marker_line_width=0


    )



    fig.update_layout(


        height=350,


        coloraxis_showscale=False


    )



    fig = apply_theme(fig)



    st.plotly_chart(

        fig,

        use_container_width=True

    )





# ============================================================
# Riesgo donut
# ============================================================


def show_risk_chart(risk):


    if risk == "Low":

        value = 25


    elif risk == "Medium":

        value = 60


    else:

        value = 90




    df = pd.DataFrame(

        {


            "Estado":[

                "Riesgo",

                "Disponible"

            ],


            "Valor":[

                value,

                100-value

            ]

        }

    )



    fig = px.pie(


        df,


        names="Estado",


        values="Valor",


        hole=.72,


        title="⚠️ Condición del activo"


    )



    fig.update_traces(


        textinfo="none"


    )



    fig.update_layout(


        height=350,


        showlegend=True


    )



    fig = apply_theme(fig)



    st.plotly_chart(

        fig,

        use_container_width=True

    )





# ============================================================
# Tendencia sensores
# ============================================================


def show_sensor_trend():



    data = pd.DataFrame(

        {


            "Tiempo":[

                "00h",

                "04h",

                "08h",

                "12h",

                "16h",

                "20h"

            ],


            "Vibración":[

                3.2,

                3.5,

                3.8,

                4.1,

                4.5,

                5.2

            ],


            "Temperatura":[

                60,

                63,

                66,

                70,

                74,

                78

            ]

        }

    )



    fig = px.line(


        data,


        x="Tiempo",


        y=[

            "Vibración",

            "Temperatura"

        ],


        markers=True,


        title="📈 Tendencia operacional del equipo"


    )



    fig.update_traces(

        line_width=3

    )



    fig.update_layout(

        height=400

    )



    fig = apply_theme(fig)



    st.plotly_chart(

        fig,

        use_container_width=True

    )