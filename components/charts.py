# ============================================================
# charts.py
# Gráficos industriales MaintAI Copilot
# ============================================================


import plotly.express as px
import pandas as pd
import streamlit as st



# ============================================================
# Gráfico importancia factores
# ============================================================


def show_factor_importance(factors):


    if not factors:

        st.info(

            "No existen variables importantes del modelo."

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

        title="Impacto de variables en el diagnóstico",

        labels={

            "importance_pct":"Importancia (%)",

            "feature":"Variable"

        }

    )



    fig.update_layout(

        height=350,

        template="plotly_dark"

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )





# ============================================================
# Gráfico circular riesgo
# ============================================================


def show_risk_chart(risk):


    if risk == "Low":


        values = [20,80]


    elif risk == "Medium":


        values = [50,50]


    else:


        values = [80,20]



    df = pd.DataFrame(

        {

            "Estado":[

                "Riesgo",

                "Disponible"

            ],


            "Valor":values

        }

    )



    fig = px.pie(

        df,

        names="Estado",

        values="Valor",

        hole=0.55,

        title="Estado de riesgo del activo"

    )



    fig.update_layout(

        template="plotly_dark"

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )





# ============================================================
# Tendencia sensores con filtros
# ============================================================


def show_sensor_trend(filters=None):


    data = pd.DataFrame(

        {


            "Tiempo":[

                1,2,3,4,5,6

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

            ],



            "Eficiencia":[

                92,

                89,

                86,

                82,

                80,

                78

            ]

        }

    )



    # --------------------------------------------------------
    # Aplicar filtro variable
    # --------------------------------------------------------


    variable = "Todas"



    if filters:


        variable = filters.get(

            "variable",

            "Todas"

        )



    if variable == "Vibración":


        columns = [

            "Vibración"

        ]


    elif variable == "Temperatura":


        columns = [

            "Temperatura"

        ]


    elif variable == "Eficiencia":


        columns = [

            "Eficiencia"

        ]


    else:


        columns = [

            "Vibración",

            "Temperatura",

            "Eficiencia"

        ]



    fig = px.line(

        data,

        x="Tiempo",

        y=columns,

        markers=True,

        title=f"Tendencia operacional - {variable}"

    )



    fig.update_layout(

        template="plotly_dark",

        height=400

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )