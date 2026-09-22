import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)


def train_anomaly_model(data_path):

    """
    Entrena un modelo Random Forest para detectar anomalías
    en equipos industriales.

    Entrada:
    data_path -> ruta del dataset parquet

    Salida:
    model -> modelo entrenado
    """


    # ==========================
    # Cargar dataset procesado
    # ==========================

    df = pd.read_parquet(data_path)


    # ==========================
    # Separar variables
    # ==========================

    X = df.drop(
        columns=["anomaly_label"]
    )

    y = df["anomaly_label"]


    # Guardamos nombres de variables
    # para futuras predicciones

    feature_names = X.columns.tolist()


    # ==========================
    # División entrenamiento/prueba
    # ==========================

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )


    # ==========================
    # Crear modelo
    # ==========================

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced"
    )


    # ==========================
    # Entrenamiento
    # ==========================

    model.fit(
        X_train,
        y_train
    )


    # ==========================
    # Predicción
    # ==========================

    y_pred = model.predict(
        X_test
    )


    # ==========================
    # Evaluación
    # ==========================

    print("Accuracy:")
    print(
        accuracy_score(
            y_test,
            y_pred
        )
    )


    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred
        )
    )


    print("\nConfusion Matrix:")
    print(
        confusion_matrix(
            y_test,
            y_pred
        )
    )


    # ==========================
    # Guardar modelo
    # ==========================

    os.makedirs(
        "../models",
        exist_ok=True
    )


    model_package = {
        "model": model,
        "features": feature_names
    }


    joblib.dump(
        model_package,
        "../models/anomaly_detector.pkl"
    )


    print(
        "\nModelo guardado correctamente:"
        " ../models/anomaly_detector.pkl"
    )


    return model