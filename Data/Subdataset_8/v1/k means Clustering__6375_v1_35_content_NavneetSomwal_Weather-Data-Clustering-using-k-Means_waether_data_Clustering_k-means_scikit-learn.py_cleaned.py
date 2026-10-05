import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
from itertools import cycle, islice
data = pd.read_csv('./weather/minute_weather.csv')
sampled_df = data[(data['rowID'] % 10) == 0]
sampled_df.drop(['rain_accumulation', 'rain_duration'], axis=1, inplace=True)
sampled_df.dropna(inplace=True)
features = ['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed', 'max_wind_direction',
            'max_wind_speed', 'relative_humidity']
select_df = sampled_df[features]
X = StandardScaler().fit_transform(select_df)
kmeans = KMeans(n_clusters=12)
model = kmeans.fit(X)
centers = model.cluster_centers_
def pd_centers(featuresUsed, centers):
    colNames = list(featuresUsed)
    colNames.append('prediction')
    Z = [np.append(A, index) for index, A in enumerate(centers)]
    P = pd.DataFrame(Z, columns=colNames)
    P['prediction'] = P['prediction'].astype(int)
    return P
def parallel_plot(data):
    my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(data)))
    plt.figure(figsize=(15, 8))
    plt.gca().axes.set_ylim([-3, +3])
    parallel_coordinates(data, 'prediction', color=my_colors, marker='o')
    plt.show()
P = pd_centers(features, centers)
parallel_plot(P[P['relative_humidity'] < -0.5])
parallel_plot(P[P['air_temp'] > 0.5])
parallel_plot(P[(P['relative_humidity'] > 0.5) & (P['air_temp'] < 0.5)])