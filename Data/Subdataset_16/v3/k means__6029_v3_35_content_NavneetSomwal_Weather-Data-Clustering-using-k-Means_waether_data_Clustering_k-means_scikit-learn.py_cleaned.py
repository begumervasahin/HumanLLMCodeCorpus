import pandas as pd
import numpy as np
from itertools import cycle, islice
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from pandas.plotting import parallel_coordinates
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b2 = b1[b1['rowID'] % 10 == 0]
    b2 = b2.drop(columns=['rain_accumulation', 'rain_duration'])
    b2 = b2.dropna()
    return b2
def fonk2(df):
    b3 = [
        'air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed',
        'max_wind_direction', 'max_wind_speed', 'relative_humidity'
    ]
    return df[b3]
def fonk3(b15, b4 = 12):
    b5 = KMeans(b4=b4, random_state=42)
    return b5.fit(b15)
def fonk4(features_used, b17):
    b6 = features_used + ['prediction']
    b7 = [np.append(center, idx) for idx, center in enumerate(b17)]
    b8 = pd.DataFrame(b7, columns=b6)
    b8['prediction'] = b8['prediction'].astype(int)
    return b8
def fonk5(b1):
    b9 = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(b1)))
    plt.figure(b10 = (15, 8)).gca().set_ylim([-3, 3])
    parallel_coordinates(b1, 'prediction', b11 = b9, marker='o')
    plt.show()
if b12 = = "__main__":
    b13 = './weather/minute_weather.csv'
    b2 = fonk1(b13)
    b14 = fonk2(b2)
    b15 = StandardScaler().fit_transform(b14)
    b16 = fonk3(b15)
    b17 = b16.cluster_centers_
    b8 = fonk4(b14.columns.tolist(), b17)
    fonk5(b8[b8['relative_humidity'] < -0.5])
    fonk5(b8[b8['air_temp'] > 0.5])
    fonk5(b8[(b8['relative_humidity'] > 0.5) & (b8['air_temp'] < 0.5)])