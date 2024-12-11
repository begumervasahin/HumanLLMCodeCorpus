import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from itertools import cycle, islice
b1 = pd.read_csv('./weather/minute_weather.csv')
b2 = b1[b1['rowID'] % 10 == 0]
b2 = b2.drop(['rain_accumulation', 'rain_duration'], axis=1).dropna()
b3 = ['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed',
            'max_wind_direction', 'max_wind_speed', 'relative_humidity']
b4 = b2[b3]
b5 = StandardScaler().fit_transform(b4)
b6 = KMeans(n_clusters=12)
b7 = b6.fit(b5)
b8 = b7.cluster_centers_
def fonk1(features_used, centers):
    b9 = list(features_used) + ['prediction']
    b10 = [np.append(center, index) for index, center in enumerate(centers)]
    b11 = pd.DataFrame(b10, columns=b9)
    b11['prediction'] = b11['prediction'].astype(int)
    return b11
def fonk2(data):
    b12 = cycle(['b', 'r', 'g', 'y', 'k'])
    fig, b13 = plt.subplots(figsize=(15, 8))
    b13.set_ylim([-3, +3])
    pd.plotting.parallel_coordinates(data, 'prediction', b14 = list(islice(b12, None, len(data))), marker='o', b13=b13)
    plt.show()
b15 = fonk1(b3, b8)
fonk2(b15[b15['relative_humidity'] < -0.5])
fonk2(b15[b15['air_temp'] > 0.5])
fonk2(b15[(b15['relative_humidity'] > 0.5) &
                                              (b15['air_temp'] < 0.5)])