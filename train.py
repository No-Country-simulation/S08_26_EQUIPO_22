import pandas as pd
import numpy as np

sensors = pd.read_csv('datasets/mgg001_sensor_data.csv')
delete_columns = [0,1,2,3,4,5,6,28,50,53,54,55,56,57,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76]

db_features = sensors.drop(sensors.columns[delete_columns], axis=1)
db_target1 = sensors['fault_probability_pct']
db_target2 = sensors['maintanance_recommendation']


print(db_features.info())
