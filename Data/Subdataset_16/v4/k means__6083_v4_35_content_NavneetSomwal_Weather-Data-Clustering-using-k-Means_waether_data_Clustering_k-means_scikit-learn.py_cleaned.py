
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle, islice
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from pandas.plotting import parallel_coordinates
b1 = pd.read_csv('./weather/minute_weather.csv')
print(f"Data shape: {b1.shape}")
print(b1.head())
b2 = b1[b1['rowID'] % 10 == 0]
print(f"Sampled b1 shape: {b2.shape}")
print(b2.describe().transpose())
print(f"Rows with zero rain accumulation: {b2[b2['rain_accumulation'] == 0].shape}")
print(f"Rows with zero rain duration: {b2[b2['rain_duration'] == 0].shape}")
b2.drop(['rain_accumulation', 'rain_duration'], b3 = 1, b5=True)
b4 = b2.shape[0]
b2.dropna(b5 = True)
b6 = b2.shape[0]
print(f"Rows dropped due to NA: {b4 - b6}")
b7 = [
    'air_pressure', 'air_temp', 'avg_wind_direction',
    'avg_wind_speed', 'max_wind_direction',
    'max_wind_speed', 'relative_humidity'
]
b8 = b2[b7]
print(f"Selected b7: {b8.columns.tolist()}")
b9 = StandardScaler().fit_transform(b8)
b10 = KMeans(n_clusters=12, random_state=42)
b11 = b10.fit(b9)
print("KMeans b11:", b11)
b12 = b11.cluster_centers_
def fonk1(features_used, b12):
    b13 = list(features_used)
    b13.append('prediction')
    b1 = [np.append(center, idx) for idx, center in enumerate(b12)]
    b14 = pd.DataFrame(b1, columns=b13)
    b14['prediction'] = b14['prediction'].astype(int)
    return b14
def fonk2(b1, b15 = 'prediction'):
    b16 = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(b1)))
    plt.figure(b17 = (15, 8))
    plt.gca().axes.set_ylim([-3, +3])
    parallel_coordinates(b1, b15, b18 = b16, marker='o')
    plt.show()
b19 = fonk1(b7, b12)
print(b19)
fonk2(b19[b19['relative_humidity'] < -0.5])
fonk2(b19[b19['air_temp'] > 0.5])
fonk2(b19[(b19['relative_humidity'] > 0.5) & (b19['air_temp'] < 0.5)])