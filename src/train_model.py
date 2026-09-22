import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def train_anomaly_model(data_path):

    """
    Entrena un modelo para detectar anomalías
    en equipos industriales.

    Entrada:
    data_path -> ruta del dataset parquet

    Salida:
    model -> modelo entrenado
    """


    # Cargar dataset procesado
    df = pd.read_parquet(data_path)


    # Separar variables predictoras y objetivo

    X = df.drop(
        columns=["anomaly_label"]
    )

    y = df["anomaly_label"]


    # División entrenamiento / prueba

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )


    # Modelo inicial

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced"
    )


    # Entrenamiento

    model.fit(
        X_train,
        y_train
    )


    # Predicción

    y_pred = model.predict(
        X_test
    )


    # Evaluación

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


    return model