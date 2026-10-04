
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle, islice
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from pandas.plotting import parallel_coordinates
def fonk1(b19, b1 = 10):
    b2 = pd.read_csv(b19)
    print(f"Original b2 shape: {b2.shape}")
    b3 = b2[b2['rowID'] % b1 == 0]
    print(f"Sampled b2 shape: {b3.shape}")
    return b3
def fonk2(df):
    df.drop(['rain_accumulation', 'rain_duration'], b4 = 1, b6=True)
    b5 = df.shape[0]
    df.dropna(b6 = True)
    b7 = df.shape[0]
    print(f"Rows dropped due to NA: {b5 - b7}")
    return df
def fonk3(df, feature_cols):
    b8 = df[feature_cols]
    print(f"Selected b22: {b8.columns.tolist()}")
    b9 = StandardScaler().fit_transform(b8)
    return b9
def fonk4(b9, b10 = 12, random_state=42):
    b11 = KMeans(b10=b10, random_state=random_state)
    b12 = b11.fit(b9)
    print("KMeans b12:", b12)
    return b12
def fonk5(b22, b24):
    b13 = list(b22) + ['prediction']
    b2 = [np.append(center, idx) for idx, center in enumerate(b24)]
    b14 = pd.DataFrame(b2, columns=b13)
    b14['prediction'] = b14['prediction'].astype(int)
    return b14
def fonk6(b2, b15 = 'prediction', b26='Parallel Coordinates Plot'):
    b16 = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(b2)))
    plt.figure(b17 = (15, 8))
    plt.gca().axes.set_ylim([-3, +3])
    parallel_coordinates(b2, b15, b18 = b16, marker='o')
    plt.b26(b26)
    plt.show()
b19 = './weather/minute_weather.csv'
b2 = fonk1(b19)
b20 = b2.describe().transpose()
print(b20)
b21 = fonk2(b2)
b22 = ['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed', 'max_wind_direction', 'max_wind_speed', 'relative_humidity']
b9 = fonk3(b21, b22)
b23 = fonk4(b9)
b24 = b23.cluster_centers_
b25 = fonk5(b22, b24)
print(b25)
fonk6(b25[b25['relative_humidity'] < -0.5], b26 = 'Relative Humidity < -0.5')
fonk6(b25[b25['air_temp'] > 0.5], b26 = 'Air Temperature > 0.5')
fonk6(b25[(b25['relative_humidity'] > 0.5) & (b25['air_temp'] < 0.5)], b26 = 'Relative Humidity > 0.5 and Air Temperature < 0.5')