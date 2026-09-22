import pandas as pd


def prepare_sensor_data(sensor):

    """
    Prepara el dataset de sensores para el modelo
    de detección de anomalías.

    Entrada:
    sensor -> DataFrame con datos de sensores

    Salida:
    X -> Variables predictoras
    y -> Variable objetivo anomaly_label
    """

    # Copia para no modificar el dataframe original
    df = sensor.copy()


    # Conversión de fecha
    df["observation_timestamp"] = pd.to_datetime(
        df["observation_timestamp"]
    )


    # Variable térmica:
    # diferencia entre temperaturas de rodamientos

    df["bearing_temp_difference"] = (
        df["temp_bearing_drive_end_c"]
        -
        df["temp_bearing_non_drive_end_c"]
    )


    # Carga térmica respecto al ambiente

    df["thermal_load"] = (
        df["temp_bearing_drive_end_c"]
        -
        df["facility_temp_c"]
    )


    # Variables seleccionadas desde el EDA

    features = [
        "temp_bearing_drive_end_c",
        "temp_bearing_non_drive_end_c",
        "temp_motor_winding_c",
        "thermal_gradient_c_per_hr",
        "temp_delta_bearing_c",
        "thermal_load",

        "vib_overall_rms_mm_s",
        "vib_peak_mm_s",
        "vib_crest_factor",
        "vib_kurtosis",

        "vib_bpfo_amplitude",
        "vib_bpfi_amplitude",

        "pressure_differential_bar",
        "pressure_lube_oil_bar",
        "flow_rate_m3_hr",
        "cavitation_index",

        "current_imbalance_pct",
        "power_factor",
        "active_power_kw",
        "motor_load_pct",

        "oil_viscosity_cst",
        "oil_contamination_ntu",
        "hours_since_lubrication",

        "operating_speed_rpm",
        "efficiency_pct"
    ]


    # Variables predictoras

    X = df[features]


    # Etiqueta del modelo

    y = df["anomaly_label"]


    return X, y