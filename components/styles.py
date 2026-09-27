# ============================================================
# styles.py
# Estilos globales MaintAI Copilot
# ============================================================


def load_styles():

    return """

    <style>


    /* ========================================================
       CONFIGURACIÓN GENERAL
    ======================================================== */


    .stApp {

        background-color: #0B1220;

        color: #F8FAFC;

    }



    /* ========================================================
       TÍTULOS
    ======================================================== */


    h1 {

        color: #F8FAFC;

        font-weight: 700;

    }


    h2 {

        color: #E2E8F0;

        font-weight: 600;

    }


    h3 {

        color: #CBD5E1;

        font-weight: 600;

    }



    /* ========================================================
       TARJETAS GENERALES
    ======================================================== */


    .card {


        background-color: #111827;


        border-radius: 18px;


        padding: 20px;


        border: 1px solid #1F2937;


        box-shadow: 0px 4px 15px rgba(0,0,0,0.25);


    }



    /* ========================================================
       TEXTO SECUNDARIO
    ======================================================== */


    .subtitle {


        color: #94A3B8;


        font-size: 14px;


    }



    /* ========================================================
       TARJETAS KPI DASHBOARD
    ======================================================== */


    .metric-card {


        background-color: #111827;


        border-radius: 16px;


        padding: 18px;


        border: 1px solid #1E293B;


    }



    .metric-title {


        color: #94A3B8;


        font-size: 13px;


    }



    .metric-value {


        color: #F8FAFC;


        font-size: 28px;


        font-weight: 700;


    }



    /* ========================================================
       CHAT USUARIO
    ======================================================== */


    .chat-user {


        background-color: #6366F1;


        color: white;


        padding: 14px;


        border-radius: 16px;


        margin: 10px 0;


        text-align: left;


    }



    /* ========================================================
       CHAT ASISTENTE IA
    ======================================================== */


    .chat-ai {


        background-color: #1E293B;


        color: #F8FAFC;


        padding: 14px;


        border-radius: 16px;


        margin: 10px 0;


        border: 1px solid #334155;


    }



    /* ========================================================
       ESTADO NORMAL
    ======================================================== */


    .status-normal {


        color: #22C55E;


        font-weight: 700;


    }



    /* ========================================================
       ESTADO ADVERTENCIA
    ======================================================== */


    .status-warning {


        color: #FACC15;


        font-weight: 700;


    }



    /* ========================================================
       ESTADO CRÍTICO
    ======================================================== */


    .status-critical {


        color: #EF4444;


        font-weight: 700;


    }



    /* ========================================================
       MÉTRICAS NATIVAS STREAMLIT
    ======================================================== */


    [data-testid="stMetric"] {


        background-color: #111827;


        border-radius: 16px;


        padding: 15px;


        border: 1px solid #1F2937;


    }



    /* ========================================================
       INPUTS
    ======================================================== */


    input {


        background-color: #111827 !important;


        color: white !important;


    }



    </style>

    """