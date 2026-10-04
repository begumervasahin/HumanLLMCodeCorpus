import pandas as pd
import numpy as np
from itertools import cycle, islice
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from pandas.plotting import parallel_coordinates
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b2 = b1[(b1['rowID'] % 10) == 0]
    b2.drop(['rain_accumulation', 'rain_duration'], b3 = 1, b4=True)
    b2.dropna(b4 = True)
    return b2
def fonk2(df):
    b5 = ['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed',
                'max_wind_direction', 'max_wind_speed', 'relative_humidity']
    return df[b5]
def fonk3(b17, b6 = 12):
    b7 = KMeans(b6=b6, random_state=42)
    return b7.fit(b17)
def fonk4(features_used, b19):
    b8 = list(features_used) + ['prediction']
    b9 = [np.append(center, idx) for idx, center in enumerate(b19)]
    return pd.DataFrame(b9, b10 = b8).astype({'prediction': int})
def fonk5(b1):
    b11 = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(b1)))
    plt.figure(b12 = (15, 8)).gca().set_ylim([-3, 3])
    parallel_coordinates(b1, 'prediction', b13 = b11, marker='o')
    plt.show()
if b14 = = "__main__":
    b15 = './weather/minute_weather.csv'
    b2 = fonk1(b15)
    b16 = fonk2(b2)
    b17 = StandardScaler().fit_transform(b16)
    b18 = fonk3(b17)
    b19 = b18.cluster_centers_
    b20 = fonk4(b16.b10, b19)
    fonk5(b20[b20['relative_humidity'] < -0.5])
    fonk5(b20[b20['air_temp'] > 0.5])
    fonk5(b20[(b20['relative_humidity'] > 0.5) & (b20['air_temp'] < 0.5)])