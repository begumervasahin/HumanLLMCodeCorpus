import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
from itertools import cycle, islice
weather_data = pd.read_csv('./weather/minute_weather.csv')
sampled_data = weather_data[weather_data['rowID'] % 10 == 0]
sampled_data.drop(['rain_accumulation', 'rain_duration'], axis=1, inplace=True)
sampled_data.dropna(inplace=True)
selected_features = [
    'air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed',
    'max_wind_direction', 'max_wind_speed', 'relative_humidity'
]
selected_data = sampled_data[selected_features]
scaled_features = StandardScaler().fit_transform(selected_data)
kmeans_model = KMeans(n_clusters=12)
cluster_model = kmeans_model.fit(scaled_features)
cluster_centers = cluster_model.cluster_centers_
def create_cluster_dataframe(features_used, centers):
    column_names = list(features_used) + ['cluster_label']
    clustered_data = np.column_stack((centers, np.arange(len(centers))))
    dataframe = pd.DataFrame(clustered_data, columns=column_names)
    dataframe['cluster_label'] = dataframe['cluster_label'].astype(int)
    return dataframe
def plot_parallel_coordinates(dataframe):
    colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(dataframe)))
    plt.figure(figsize=(15, 8))
    plt.gca().axes.set_ylim([-3, +3])
    parallel_coordinates(dataframe, 'cluster_label', color=colors, marker='o')
    plt.show()
cluster_dataframe = create_cluster_dataframe(selected_features, cluster_centers)
plot_parallel_coordinates(cluster_dataframe[cluster_dataframe['relative_humidity'] < -0.5])
plot_parallel_coordinates(cluster_dataframe[cluster_dataframe['air_temp'] > 0.5])
condition = (cluster_dataframe['relative_humidity'] > 0.5) & (cluster_dataframe['air_temp'] < 0.5)
plot_parallel_coordinates(cluster_dataframe[condition])