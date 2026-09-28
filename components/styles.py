# ============================================================
# styles.py
# Estilos globales MaintAI Copilot
# ============================================================


def load_styles():

    return """

<style>


/* ===============================
   GLOBAL
================================ */


.stApp {

    background:#0f131c;

    color:#dfe2ef;

    font-family:
    "Plus Jakarta Sans",
    sans-serif;

}



/* Ocultar elementos Streamlit */

#MainMenu {

display:none;

}


footer {

display:none;

}


header {

visibility:hidden;

}



/* ===============================
   CONTENEDOR PRINCIPAL
================================ */


.block-container {


padding-top:2rem;

padding-left:2rem;

padding-right:2rem;

max-width:1400px;


}



/* ===============================
   TITULOS
================================ */


h1,h2,h3 {

color:#dfe2ef;

font-weight:700;

}



/* ===============================
   TARJETAS
================================ */


.ai-card {


background:#181b25;


border:

1px solid #31353f;


border-radius:18px;


padding:20px;


box-shadow:

0 8px 25px rgba(0,0,0,.35);


}



/* ===============================
   HEADER
================================ */


.ai-header {


background:#181b25;


border-radius:18px;


padding:20px;


border:

1px solid #31353f;


display:flex;


justify-content:space-between;


align-items:center;


margin-bottom:25px;


}



.ai-status {


background:#163b2f;


color:#4edea3;


padding:8px 14px;


border-radius:20px;


font-size:13px;


}



/* ===============================
   KPI CARDS
================================ */


[data-testid="stMetric"] {


background:#181b25;


border-radius:16px;


padding:18px;


border:

1px solid #31353f;


}



[data-testid="stMetricLabel"] {


color:#8f8fa0;


}



[data-testid="stMetricValue"] {


color:#c0c1ff;


font-size:32px;


font-weight:700;


}



/* ===============================
   INPUTS
================================ */


input {


background:#262a34 !important;


color:white !important;


border-radius:12px !important;


}



.stSelectbox div[data-baseweb="select"] {


background:#262a34;


border-radius:12px;


}



/* ===============================
   BOTONES
================================ */


.stButton button {


background:

linear-gradient(
90deg,
#8083ff,
#4cd7f6
);


color:#0f131c;


border:none;


border-radius:12px;


font-weight:700;


height:42px;


}



.stButton button:hover {


opacity:.85;


}



/* ===============================
   CHAT
================================ */


.chat-box {


background:#181b25;


border-radius:18px;


padding:20px;


height:700px;


overflow-y:auto;


border:

1px solid #31353f;


}



.chat-user {


background:#8083ff;


color:#0f131c;


padding:12px;


border-radius:18px;


margin-bottom:10px;


}



.chat-ai {


background:#262a34;


padding:12px;


border-radius:18px;


margin-bottom:10px;


}




</style>

"""
