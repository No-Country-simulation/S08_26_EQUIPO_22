# ============================================================
# charts.py
# Gráficos MaintAI Copilot
# Dashboard analítico con filtros
# ============================================================


import pandas as pd

import plotly.express as px

import streamlit as st





# ============================================================
# Tema visual Plotly
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
# Factores críticos
# ============================================================


def show_factor_importance(factors):


    if not factors:


        st.info(

            "No hay factores críticos disponibles"

        )

        return





    df = pd.DataFrame(factors)



    if "importance" not in df.columns:


        st.warning(

            "Formato de factores no válido"

        )

        return





    df["importance_pct"] = (

        df["importance"] * 100

    )





    fig = px.bar(


        df,


        x="importance_pct",


        y="feature",


        orientation="h",


        title="🧠 Variables influyentes del diagnóstico"


    )





    fig.update_layout(

        height=350,

        xaxis_title="Importancia (%)",

        yaxis_title="Variable"

    )



    fig = apply_theme(fig)



    st.plotly_chart(

        fig,

        use_container_width=True

    )









# ============================================================
# Estado de riesgo
# ============================================================


def show_risk_chart(risk):


    risk_text = str(risk).lower()



    if risk_text in [

        "low",

        "bajo"

    ]:


        value = 25



    elif risk_text in [

        "medium",

        "medio"

    ]:


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


        hole=0.7,


        title="⚠️ Condición del activo"


    )





    fig.update_traces(

        textinfo="none"

    )





    fig.update_layout(

        height=350

    )





    fig = apply_theme(fig)





    st.plotly_chart(

        fig,

        use_container_width=True

    )









# ============================================================
# Tendencia operacional con filtros
# ============================================================


def show_sensor_trend(

    variable="Todas",

    periodo="Actual"

):


    """
    Gráfico dinámico según filtros seleccionados
    """



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






    # --------------------------------------------------------
    # Aplicación filtros
    # --------------------------------------------------------


    if variable == "Vibración":



        fig = px.line(


            data,


            x="Tiempo",


            y="Vibración",


            markers=True,


            title=f"📈 Vibración - {periodo}"


        )






    elif variable == "Temperatura":



        fig = px.line(


            data,


            x="Tiempo",


            y="Temperatura",


            markers=True,


            title=f"🌡️ Temperatura - {periodo}"


        )






    elif variable == "Eficiencia":



        eficiencia = pd.DataFrame(

            {


                "Tiempo":data["Tiempo"],


                "Eficiencia":[

                    95,

                    92,

                    90,

                    88,

                    85,

                    82

                ]

            }

        )




        fig = px.line(


            eficiencia,


            x="Tiempo",


            y="Eficiencia",


            markers=True,


            title=f"⚡ Eficiencia - {periodo}"


        )






    else:




        fig = px.line(


            data,


            x="Tiempo",


            y=[

                "Vibración",

                "Temperatura"

            ],


            markers=True,


            title=f"📈 Tendencia operacional - {periodo}"


        )







    fig.update_traces(

        line_width=3

    )





    fig.update_layout(


        height=400,


        xaxis_title="Tiempo",


        yaxis_title="Valor"

    )





    fig = apply_theme(fig)





    st.plotly_chart(

        fig,

        use_container_width=True

    )