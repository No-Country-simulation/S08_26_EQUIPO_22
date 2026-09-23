# ============================================================
# knowledge_base.py
# Base de conocimiento técnico para mantenimiento predictivo
# ============================================================


MAINTENANCE_KNOWLEDGE = {


    # ========================================================
    # VARIABLES TÉRMICAS
    # ========================================================


    "temp_bearing_drive_end_c": {

        "meaning":
            "Temperatura del rodamiento lado acople del equipo. "
            "Un incremento puede indicar fricción, desgaste o problemas de lubricación.",


        "possible_causes":
            [
                "Desgaste del rodamiento",
                "Falta o degradación de lubricante",
                "Carga mecánica excesiva",
                "Desalineación del eje"
            ],


        "recommended_actions":
            [
                "Verificar temperatura contra tendencia histórica",
                "Inspeccionar condición del rodamiento",
                "Revisar lubricación"
            ]
    },


    "temp_bearing_non_drive_end_c": {

        "meaning":
            "Temperatura del rodamiento lado opuesto al acople. "
            "Permite detectar anomalías térmicas en el soporte mecánico.",


        "possible_causes":
            [
                "Daño de rodamiento",
                "Problemas de alineación",
                "Fricción interna"
            ],


        "recommended_actions":
            [
                "Comparar temperatura entre ambos rodamientos",
                "Realizar inspección mecánica"
            ]
    },


    "temp_motor_winding_c": {

        "meaning":
            "Temperatura del devanado del motor eléctrico. "
            "Un aumento puede afectar la vida útil del aislamiento.",


        "possible_causes":
            [
                "Sobrecarga eléctrica",
                "Falta de ventilación",
                "Desequilibrio de corriente",
                "Degradación del aislamiento"
            ],


        "recommended_actions":
            [
                "Verificar carga del motor",
                "Inspeccionar sistema de refrigeración",
                "Medir corriente por fase"
            ]
    },


    "thermal_gradient_c_per_hr": {

        "meaning":
            "Velocidad de incremento térmico del equipo.",


        "possible_causes":
            [
                "Aumento progresivo de fricción",
                "Condición de sobrecarga",
                "Falla en sistema de enfriamiento"
            ],


        "recommended_actions":
            [
                "Revisar tendencia térmica",
                "Analizar evolución de temperatura"
            ]
    },


    "temp_delta_bearing_c": {

        "meaning":
            "Diferencia de temperatura entre puntos de medición del rodamiento.",


        "possible_causes":
            [
                "Distribución irregular de carga",
                "Problemas de lubricación",
                "Desgaste localizado"
            ],


        "recommended_actions":
            [
                "Comparar temperaturas entre puntos",
                "Inspeccionar rodamientos"
            ]
    },


    "thermal_load": {

        "meaning":
            "Nivel de carga térmica del sistema.",


        "possible_causes":
            [
                "Operación cercana al límite",
                "Sobrecarga del equipo"
            ],


        "recommended_actions":
            [
                "Revisar condiciones operativas"
            ]
    },



    # ========================================================
    # VARIABLES DE VIBRACIÓN
    # ========================================================


    "vib_overall_rms_mm_s": {

        "meaning":
            "Nivel global RMS de vibración del equipo.",


        "possible_causes":
            [
                "Desbalance",
                "Desalineación",
                "Desgaste mecánico"
            ],


        "recommended_actions":
            [
                "Realizar análisis vibracional",
                "Comparar con límites históricos"
            ]
    },


    "vib_peak_mm_s": {

        "meaning":
            "Valor máximo de vibración detectado.",


        "possible_causes":
            [
                "Impactos mecánicos",
                "Fallas localizadas"
            ],


        "recommended_actions":
            [
                "Analizar eventos impulsivos"
            ]
    },


    "vib_crest_factor": {

        "meaning":
            "Relación entre valor pico y RMS de vibración.",


        "possible_causes":
            [
                "Golpes internos",
                "Falla temprana de rodamiento",
                "Defectos localizados"
            ],


        "recommended_actions":
            [
                "Revisar evolución del indicador",
                "Inspeccionar elementos rotativos"
            ]
    },


    "vib_kurtosis": {

        "meaning":
            "Indicador estadístico asociado a impactos anormales "
            "y eventos impulsivos en vibración.",


        "possible_causes":
            [
                "Desgaste o daño en rodamientos",
                "Holguras mecánicas",
                "Problemas de lubricación",
                "Daño interno"
            ],


        "recommended_actions":
            [
                "Realizar análisis espectral",
                "Inspeccionar rodamientos",
                "Verificar lubricación"
            ]
    },


    "vib_bpfo_amplitude": {

        "meaning":
            "Amplitud asociada a frecuencia característica de falla externa del rodamiento.",


        "possible_causes":
            [
                "Daño en pista externa del rodamiento"
            ],


        "recommended_actions":
            [
                "Realizar análisis de frecuencia de vibración"
            ]
    },


    "vib_bpfi_amplitude": {

        "meaning":
            "Amplitud asociada a frecuencia característica de falla interna del rodamiento.",


        "possible_causes":
            [
                "Daño en pista interna del rodamiento"
            ],


        "recommended_actions":
            [
                "Inspección detallada del rodamiento"
            ]
    },



    # ========================================================
    # VARIABLES HIDRÁULICAS Y LUBRICACIÓN
    # ========================================================


    "pressure_differential_bar": {

        "meaning":
            "Diferencia de presión del sistema.",


        "possible_causes":
            [
                "Restricción de flujo",
                "Problemas hidráulicos"
            ],


        "recommended_actions":
            [
                "Revisar sistema hidráulico"
            ]
    },


    "pressure_lube_oil_bar": {

        "meaning":
            "Presión del aceite de lubricación.",


        "possible_causes":
            [
                "Baja lubricación",
                "Falla de bomba de aceite"
            ],


        "recommended_actions":
            [
                "Verificar presión de aceite",
                "Inspeccionar sistema de lubricación"
            ]
    },


    "flow_rate_m3_hr": {

        "meaning":
            "Caudal del sistema.",


        "possible_causes":
            [
                "Obstrucción",
                "Problema de suministro"
            ],


        "recommended_actions":
            [
                "Revisar flujo operativo"
            ]
    },


    "cavitation_index": {

        "meaning":
            "Indicador de presencia de cavitación.",


        "possible_causes":
            [
                "Entrada de aire",
                "Condiciones hidráulicas inadecuadas"
            ],


        "recommended_actions":
            [
                "Inspeccionar bomba y condiciones hidráulicas"
            ]
    },



    # ========================================================
    # VARIABLES ELÉCTRICAS
    # ========================================================


    "current_imbalance_pct": {

        "meaning":
            "Desequilibrio porcentual de corriente entre fases.",


        "possible_causes":
            [
                "Problemas eléctricos",
                "Desbalance de alimentación",
                "Daño en devanados"
            ],


        "recommended_actions":
            [
                "Medir corriente por fase",
                "Revisar alimentación eléctrica"
            ]
    },


    "power_factor": {

        "meaning":
            "Factor de potencia del motor.",


        "possible_causes":
            [
                "Operación ineficiente",
                "Problemas de carga"
            ],


        "recommended_actions":
            [
                "Analizar consumo eléctrico"
            ]
    },


    "active_power_kw": {

        "meaning":
            "Potencia activa consumida por el equipo.",


        "possible_causes":
            [
                "Sobrecarga",
                "Cambios de operación"
            ],


        "recommended_actions":
            [
                "Comparar consumo histórico"
            ]
    },


    "motor_load_pct": {

        "meaning":
            "Porcentaje de carga del motor.",


        "possible_causes":
            [
                "Sobrecarga",
                "Operación fuera del punto óptimo"
            ],


        "recommended_actions":
            [
                "Verificar condiciones operativas"
            ]
    },



    # ========================================================
    # ACEITE Y EFICIENCIA
    # ========================================================


    "oil_viscosity_cst": {

        "meaning":
            "Viscosidad del lubricante.",


        "possible_causes":
            [
                "Degradación del aceite",
                "Temperatura elevada"
            ],


        "recommended_actions":
            [
                "Analizar condición del lubricante"
            ]
    },


    "oil_contamination_ntu": {

        "meaning":
            "Nivel de contaminación del aceite.",


        "possible_causes":
            [
                "Ingreso de partículas",
                "Desgaste interno"
            ],


        "recommended_actions":
            [
                "Realizar análisis de aceite"
            ]
    },


    "hours_since_lubrication": {

        "meaning":
            "Tiempo transcurrido desde la última lubricación.",


        "possible_causes":
            [
                "Mantenimiento atrasado"
            ],


        "recommended_actions":
            [
                "Programar lubricación preventiva"
            ]
    },


    "operating_speed_rpm": {

        "meaning":
            "Velocidad de operación del equipo.",


        "possible_causes":
            [
                "Operación fuera de rango",
                "Cambios de proceso"
            ],


        "recommended_actions":
            [
                "Validar condiciones nominales"
            ]
    },


    "efficiency_pct": {

        "meaning":
            "Porcentaje de eficiencia operacional del equipo.",


        "possible_causes":
            [
                "Desgaste interno",
                "Pérdida de capacidad",
                "Operación ineficiente"
            ],


        "recommended_actions":
            [
                "Comparar con histórico",
                "Evaluar desempeño del equipo"
            ]
    }

}