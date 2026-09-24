# ============================================================
# test_pipeline.py
# Pruebas del pipeline de mantenimiento predictivo
# ============================================================

import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)


from src.pipeline import analyze_equipment



def create_sensor_test():

    """
    Datos simulados de un motor con condición anómala
    """

    return {

        "temp_bearing_drive_end_c": 80,

        "temp_bearing_non_drive_end_c": 78,

        "temp_motor_winding_c": 95,

        "thermal_gradient_c_per_hr": 4,

        "temp_delta_bearing_c": 8,

        "thermal_load": 0.95,


        "vib_overall_rms_mm_s": 8,

        "vib_peak_mm_s": 12,

        "vib_crest_factor": 5,

        "vib_kurtosis": 2.5,

        "vib_bpfo_amplitude": 0.8,

        "vib_bpfi_amplitude": 0.7,


        "pressure_differential_bar": 1.2,

        "pressure_lube_oil_bar": 1.5,

        "flow_rate_m3_hr": 15,

        "cavitation_index": 0.7,


        "current_imbalance_pct": 8,

        "power_factor": 0.75,

        "active_power_kw": 70,

        "motor_load_pct": 95,


        "oil_viscosity_cst": 55,

        "oil_contamination_ntu": 40,

        "hours_since_lubrication": 900,

        "operating_speed_rpm": 1800,

        "efficiency_pct": 70

    }



def test_pipeline_returns_result():


    sensor_data = create_sensor_test()


    result = analyze_equipment(

        sensor_data,

        equipment="MGG001"

    )


    assert "prediction" in result

    assert "diagnosis" in result

    assert "ai_report" in result



def test_diagnosis_exists():


    sensor_data = create_sensor_test()


    result = analyze_equipment(

        sensor_data

    )


    diagnosis = result["diagnosis"]


    assert "condition" in diagnosis

    assert "risk_level" in diagnosis

    assert "confidence" in diagnosis