# ============================================================
# test_predict.py
# Prueba del modelo Machine Learning
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


from src.predict import predict_anomaly



# ============================================================
# Datos de prueba
# ============================================================


def create_sensor_test():


    return {


        "temp_bearing_drive_end_c": 60,

        "temp_bearing_non_drive_end_c": 58,

        "temp_motor_winding_c": 75,

        "thermal_gradient_c_per_hr": 2,

        "temp_delta_bearing_c": 5,

        "thermal_load": 0.8,


        "vib_overall_rms_mm_s": 5.6,

        "vib_peak_mm_s": 8.5,

        "vib_crest_factor": 4.2,

        "vib_kurtosis": 0.85,

        "vib_bpfo_amplitude": 0.35,

        "vib_bpfi_amplitude": 0.30,


        "pressure_differential_bar": 1.5,

        "pressure_lube_oil_bar": 2,

        "flow_rate_m3_hr": 20,


        "cavitation_index": 0.2,


        "current_imbalance_pct": 3,

        "power_factor": 0.85,

        "active_power_kw": 50,

        "motor_load_pct": 75,


        "oil_viscosity_cst": 45,

        "oil_contamination_ntu": 10,

        "hours_since_lubrication": 300,

        "operating_speed_rpm": 1800,


        "efficiency_pct": 78

    }



# ============================================================
# Test modelo ML
# ============================================================


def test_model_prediction():


    sensor_data = create_sensor_test()


    result = predict_anomaly(
        sensor_data
    )


    assert "prediction" in result

    assert "risk_level" in result

    assert "main_factors" in result