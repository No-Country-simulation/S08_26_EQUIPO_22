import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

# Cargo el dataset de sensores.
db_sensors = pd.read_csv('datasets/mgg001_sensor_data.csv')

# Identifico cada tipo de máquinas que hay en el dataset.
assets = db_sensors['asset_id'].sort_values(ascending=True).unique()
#print(f"Máquinas en el dataset: {assets}")

# Revision de las máquinas con mayor probabilidad de falla
'''
for i in assets:
    plt.figure(figsize=(6,4))
    plt.hist(db_sensors[db_sensors['asset_id'] == i]['maintenance_recommendation'], bins=20)
    plt.title(i)
    plt.xlabel('Fault Probability (%)')
    plt.ylabel('Recommendations')
    plt.show()
'''

# Separo las máquinas que tienen fallas para concentrarme en ellas.
bad_assets = db_sensors[db_sensors['fault_probability_pct'] >= 10]['asset_id'].unique()

# Divido el dataset en cadat tipo de máquina para poder analizarlo por separado.
CNC = assets[:3]
COM = assets[3]  
CON = assets[4]
GEA = assets[5]
MOT = assets[6:8]
PUM = assets[8:]
#print(PUM)

#db_sensors_correct_assets = db_sensors[db_sensors['asset_id'].isin(bad_assets)]
#print(db_sensors_correct_assets['asset_id'].value_counts())

# Elimino columnas que no aportan información relevante para el análisis.
delete_columns = [1,2,3,4,6,7,28,50,53,54,55,56,57,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76]
new_db_sensors = db_sensors.drop(db_sensors.columns[delete_columns], axis=1)

# Cambio el tipo de dato a datetime para la columna 'timesobservation_timestamptamp' y la establezco como índice del DataFrame.
new_db_sensors['observation_timestamp'] = pd.to_datetime(new_db_sensors['observation_timestamp'])
new_db_sensors = new_db_sensors.sort_values(by=['asset_id', 'observation_timestamp']).reset_index(drop=True)
#print(new_db_sensors.info())

# Reviso la relación entre las variables numéricas.
'''
df_numerico = new_db_sensors.select_dtypes(include=[np.number])
matriz_corr = df_numerico.corr()

variable_objetivo = 'rul_predicted_hours' 
#print("--- Correlación con la variable objetivo ---")
#print(matriz_corr[variable_objetivo].sort_values(ascending=False))

plt.figure(figsize=(10, 10))
sns.heatmap(matriz_corr, cmap='coolwarm', linewidths=0.5)
plt.title('Mapa de Calor de Correlación')
plt.show()
'''

# Con la información de correlación, puedo eliminar algunas columnas que no aportan información relevante para el análisis.
#less_columns = [9,14,15,16,17,18,19,22,28,34,39,44,46,49,50]
less_columns = [16,17,18,19]
next_db_sensors = new_db_sensors.drop(new_db_sensors.columns[less_columns], axis=1)

# Se confirma una nueva matriz de correlación con las columnas restantes.
'''
df_numerico = next_db_sensors.select_dtypes(include=[np.number])
matriz_corr = df_numerico.corr()

variable_objetivo = 'rul_predicted_hours' 
#print("--- Nueva correlación con la variable objetivo ---")
#print(matriz_corr[variable_objetivo].sort_values(ascending=False))

plt.figure(figsize=(10, 10))
sns.heatmap(matriz_corr, cmap='coolwarm', linewidths=0.5)
plt.title('Mapa de Calor de Correlación')
plt.show()
'''

### Para poder hacer que el modelo realice buenas predicciones, necesito que el dataset sea
### sea mas grande, por lo que opte en concatenar el dataset original (quitando las maquinas
### para el entrenamiento) y unirlo con las maquinas que tienen fallas para resaltar la
### información de estas últimas.


db_good_assets = next_db_sensors[~next_db_sensors['asset_id'].isin(assets[:8])].reset_index(drop=True)
db_bad_assets = next_db_sensors[next_db_sensors['asset_id'].isin(bad_assets[:-1])].reset_index(drop=True)

#db_cnc_train = next_db_sensors[next_db_sensors['asset_id'].isin(assets[:8])].reset_index(drop=True)
db_cnc_train = pd.concat([db_good_assets,db_good_assets, db_bad_assets], ignore_index=True)
db_cnc_test = next_db_sensors[next_db_sensors['asset_id'].isin([assets[11]])].reset_index(drop=True)

#print(db_cnc_train.info())
#print(db_cnc_test.info())
#print(db_cnc_train.head())
#print(db_cnc_test.head())


cnc_features_train = db_cnc_train.drop(['asset_id','observation_timestamp','rul_predicted_hours'], axis=1)
cnc_target_train = db_cnc_train['rul_predicted_hours']

cnc_features_test = db_cnc_test.drop(['asset_id','observation_timestamp','rul_predicted_hours'], axis=1)
cnc_target_test = db_cnc_test['rul_predicted_hours']

# Escalo los datos para que el modelo pueda aprender mejor.
scaler = StandardScaler()
sc_cnc_features_train = scaler.fit_transform(cnc_features_train)
sc_cnc_features_test = scaler.transform(cnc_features_test)

modelo_cuanti = RandomForestRegressor(random_state=42,n_estimators=100, max_depth=10, min_samples_split=2, min_samples_leaf=1)
modelo_cuanti.fit(sc_cnc_features_train, cnc_target_train)

predicciones = modelo_cuanti.predict(sc_cnc_features_test)


print(f"MAE (Error Absoluto Medio): {mean_absolute_error(cnc_target_test, predicciones):.2f}")
print(f"RMSE (Raíz del Error Cuadrático Medio): {root_mean_squared_error(cnc_target_test, predicciones):.2f}")
print(f"R² Score (Coeficiente de Determinación): {r2_score(cnc_target_test, predicciones):.2f}")

nombre_modelo = 'modelos/modelo_cnc.pkl'
#joblib.dump(modelo_cuanti, nombre_modelo)
#print(f"Modelo guardado en: {nombre_modelo}")