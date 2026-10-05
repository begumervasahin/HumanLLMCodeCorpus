import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
from itertools import cycle, islice
b1 = pd.read_csv('./weather/minute_weather.csv')
b2 = b1[b1['rowID'] % 10 == 0]
b2.drop(['rain_accumulation', 'rain_duration'], b3 = 1, b4=True)
b2.dropna(b4 = True)
b5 = [
    'air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed',
    'max_wind_direction', 'max_wind_speed', 'relative_humidity'
]
b6 = b2[b5]
b7 = StandardScaler().fit_transform(b6)
b8 = KMeans(n_clusters=12)
b9 = b8.fit(b7)
b10 = b9.cluster_centers_
def fonk1(features_used, centers):
    b11 = list(features_used) + ['cluster_label']
    b12 = np.column_stack((centers, np.arange(len(centers))))
    b13 = pd.DataFrame(b12, columns=b11)
    b13['cluster_label'] = b13['cluster_label'].astype(int)
    return b13
def fonk2(b13):
    b14 = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(b13)))
    plt.figure(b15 = (15, 8))
    plt.gca().axes.set_ylim([-3, +3])
    parallel_coordinates(b13, 'cluster_label', b16 = b14, marker='o')
    plt.show()
b17 = fonk1(b5, b10)
fonk2(b17[b17['relative_humidity'] < -0.5])
fonk2(b17[b17['air_temp'] > 0.5])
b18 = (b17['relative_humidity'] > 0.5) & (b17['air_temp'] < 0.5)
fonk2(b17[b18])