# ============================================================
# app.py
# Interfaz Streamlit - Sistema de Mantenimiento Predictivo IA
# ============================================================


import streamlit as st
import sys
import os


# ============================================================
# Ajuste de ruta del proyecto
# ============================================================


sys.path.insert(
    0,
    os.path.abspath(
        os.path.dirname(__file__)
    )
)


from src.pipeline import analyze_equipment



# ============================================================
# Configuración página
# ============================================================


st.set_page_config(

    page_title="Mantenimiento Predictivo IA",

    page_icon="⚙️",

    layout="centered"

)



# ============================================================
# Título
# ============================================================


st.title(
    "⚙️ Sistema de Mantenimiento Predictivo IA"
)


st.write(
    "Análisis inteligente de condición del equipo usando Machine Learning + LLM"
)



# ============================================================
# Equipo
# ============================================================


equipment = st.text_input(

    "Código del equipo",

    value="MGG001"

)



# ============================================================
# Variables sensores
# ============================================================


st.subheader(
    "Datos del equipo"
)


col1, col2 = st.columns(2)



with col1:


    vib_kurtosis = st.number_input(

        "Vibración Kurtosis",

        value=0.85

    )


    vib_crest_factor = st.number_input(

        "Factor Crest Vibración",

        value=4.2

    )


    efficiency_pct = st.number_input(

        "Eficiencia (%)",

        value=78.0

    )



with col2:


    temp_motor = st.number_input(

        "Temperatura motor (°C)",

        value=75.0

    )


    motor_load = st.number_input(

        "Carga motor (%)",

        value=75.0

    )


    operating_speed = st.number_input(

        "Velocidad RPM",

        value=1800

    )



# ============================================================
# Construcción datos sensores
# ============================================================


sensor_data = {


    "temp_bearing_drive_end_c":60,

    "temp_bearing_non_drive_end_c":58,

    "temp_motor_winding_c":temp_motor,

    "thermal_gradient_c_per_hr":2,

    "temp_delta_bearing_c":5,

    "thermal_load":0.8,


    "vib_overall_rms_mm_s":5.6,

    "vib_peak_mm_s":8.5,

    "vib_crest_factor":vib_crest_factor,

    "vib_kurtosis":vib_kurtosis,

    "vib_bpfo_amplitude":0.35,

    "vib_bpfi_amplitude":0.30,


    "pressure_differential_bar":1.5,

    "pressure_lube_oil_bar":2,

    "flow_rate_m3_hr":20,

    "cavitation_index":0.2,


    "current_imbalance_pct":3,

    "power_factor":0.85,

    "active_power_kw":50,

    "motor_load_pct":motor_load,


    "oil_viscosity_cst":45,

    "oil_contamination_ntu":10,

    "hours_since_lubrication":300,

    "operating_speed_rpm":operating_speed,


    "efficiency_pct":efficiency_pct

}



# ============================================================
# Botón análisis
# ============================================================


if st.button(
    "🔍 Analizar equipo"
):


    with st.spinner(
        "Analizando condición del equipo..."
    ):


        result = analyze_equipment(

            sensor_data,

            equipment=equipment

        )



    st.success(
        "Análisis completado"
    )


    st.subheader(
        "Resultado"
    )


    st.json(
        result
    )