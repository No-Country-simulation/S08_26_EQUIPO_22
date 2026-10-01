# ============================================================
# chat.py
# Chat IA MaintAI Copilot
# ============================================================


import streamlit as st


from src.llm_connector import ask_llm





# ============================================================
# Render Chat
# ============================================================


def render_chat(diagnosis, equipment):


    """
    Chat inteligente MaintAI Copilot
    """



    # Crear memoria

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []





    # Historial

    for message in st.session_state.chat_history:


        if message["role"] == "user":


            with st.chat_message("user"):

                st.write(

                    message["content"]

                )


        else:


            with st.chat_message("assistant"):

                st.write(

                    message["content"]

                )






    # Entrada usuario


    question = st.chat_input(

        "Pregunte sobre el estado del equipo..."

    )





    if question:



        st.session_state.chat_history.append(

            {

                "role":"user",

                "content":question

            }

        )




        with st.chat_message("user"):

            st.write(question)





        with st.chat_message("assistant"):


            with st.spinner(

                "🤖 MaintAI analizando..."

            ):



                answer = ask_llm(

                    diagnosis,

                    question,

                    st.session_state.chat_history[-4:]

                )



            st.write(answer)




        st.session_state.chat_history.append(

            {

                "role":"assistant",

                "content":answer

            }

        )