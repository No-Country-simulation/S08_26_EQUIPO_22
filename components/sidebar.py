# ============================================================
# sidebar.py
# Barra lateral MaintAI Copilot
# ============================================================


import streamlit as st
from datetime import datetime



def render_sidebar():

    """
    Construye la barra lateral
    y retorna el equipo seleccionado.
    """



    with st.sidebar:


        st.title(
            "⚙️ MaintAI Copilot"
        )


        st.caption(
            "Sistema inteligente de mantenimiento predictivo"
        )


        st.divider()



        # -------------------------------
        # Equipo
        # -------------------------------


        equipment = st.text_input(

            "🏭 Código del equipo",

            value="MGG001"

        )



        st.divider()



        # -------------------------------
        # Estado sistema
        # -------------------------------


        st.subheader(

            "Estado del sistema"

        )



        st.success(

            "🟢 Modelo ML activo"

        )


        st.info(

            "🤖 LLM preparado"

        )



        st.divider()



        # -------------------------------
        # Información técnica
        # -------------------------------


        st.subheader(

            "Información"

        )


        st.write(

            "🌲 Modelo: Random Forest"

        )


        st.write(

            "🧠 Motor IA: Ollama"

        )


        st.write(

            "📅 Sesión: "

            + datetime.now().strftime("%d/%m/%Y %H:%M")

        )



    return equipment