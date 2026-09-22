import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

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
COM = assets[3:4]  
CON = assets[4:5]
GEA = assets[5:6]
MOT = assets[6:8]
PUM = assets[8:9]
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
less_columns = [9,14,15,16,17,18,19,22,28,34,39,44,46,49,50]
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

### ME concentrare en predecir el manteninmiento en las maquinas de CNC ya que es donde hay 
### mas facilidad de crear el modelo, ya que contiene 2 máquinas con fallas y una 
### completamente bien, lo que me permite tener un dataset más balanceado y con más información
### para entrenar el modelo.

db_cnc_train = next_db_sensors[next_db_sensors['asset_id'].isin(CNC[1:3])].reset_index(drop=True)
db_cnc_test = next_db_sensors[next_db_sensors['asset_id'] == CNC[0]].reset_index(drop=True)

#print(db_cnc_train.info())
#print(db_cnc_test.info())

print(db_cnc_train.head())
print(db_cnc_test.head())

'''
db_features = next_db_sensors.drop(['asset_id','rul_predicted_hours'], axis=1)
db_target = next_db_sensors['rul_predicted_hours']
#db_target2 = new_db_sensors['maintenance_recommendation']

#db_features = pd.get_dummies(db_features, drop_first=True)

features_train, features_test, target_train, target_test = train_test_split(db_features, db_target, test_size=0.2, random_state=42)

modelo_cuanti = RandomForestRegressor(random_state=42)
modelo_cuanti.fit(features_train, target_train)

predicciones = modelo_cuanti.predict(features_test)

#print(new_db_sensors.info())
print(f"MAE (Error Absoluto Medio): {mean_absolute_error(target_test, predicciones):.2f}")
print(f"RMSE (Raíz del Error Cuadrático Medio): {root_mean_squared_error(target_test, predicciones):.2f}")
print(f"R² Score (Coeficiente de Determinación): {r2_score(target_test, predicciones):.2f}")
'''
