
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
    b2 = b2.drop(['rain_accumulation', 'rain_duration'], axis=1)
    b2 = b2.dropna()
    return b2
def fonk2(df):
    b3 = ['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed', 'max_wind_direction',
                'max_wind_speed', 'relative_humidity']
    return df[b3]
def fonk3(b16, b4 = 12):
    b5 = KMeans(b4=b4)
    b6 = b5.fit(b16)
    return b6
def fonk4(features_used, b18):
    b7 = list(features_used)
    b7.append('prediction')
    b8 = [np.append(A, index) for index, A in enumerate(b18)]
    b9 = pd.DataFrame(b8, columns=b7)
    b9['prediction'] = b9['prediction'].astype(int)
    return b9
def fonk5(b1):
    b10 = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(b1)))
    plt.figure(b11 = (15, 8)).gca().axes.set_ylim([-3, +3])
    parallel_coordinates(b1, 'prediction', b12 = b10, marker='o')
    plt.show()
if b13 = = "__main__":
    b14 = './weather/minute_weather.csv'
    b2 = fonk1(b14)
    b15 = fonk2(b2)
    b16 = StandardScaler().fit_transform(b15)
    b17 = fonk3(b16)
    b18 = b17.cluster_centers_
    b9 = fonk4(b15.columns, b18)
    fonk5(b9[b9['relative_humidity'] < -0.5])
    fonk5(b9[b9['air_temp'] > 0.5])
    fonk5(b9[(b9['relative_humidity'] > 0.5) & (b9['air_temp'] < 0.5)])