
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from itertools import cycle, islice
weather_data = pd.read_csv('./weather/minute_weather.csv')
sampled_weather_data = weather_data[weather_data['rowID'] % 10 == 0]
sampled_weather_data = sampled_weather_data.drop(['rain_accumulation', 'rain_duration'], axis=1).dropna()
features = ['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed',
            'max_wind_direction', 'max_wind_speed', 'relative_humidity']
selected_features = sampled_weather_data[features]
scaled_features = StandardScaler().fit_transform(selected_features)
kmeans = KMeans(n_clusters=12)
kmeans_model = kmeans.fit(scaled_features)
cluster_centers = kmeans_model.cluster_centers_
def cluster_centers_dataframe(features_used, centers):
    col_names = list(features_used) + ['prediction']
    centers_with_prediction = [np.append(center, index) for index, center in enumerate(centers)]
    centers_df = pd.DataFrame(centers_with_prediction, columns=col_names)
    centers_df['prediction'] = centers_df['prediction'].astype(int)
    return centers_df
def plot_parallel_coordinates(data):
    my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(data)))
    plt.figure(figsize=(15, 8))
    plt.gca().axes.set_ylim([-3, +3])
    pd.plotting.parallel_coordinates(data, 'prediction', color=my_colors, marker='o')
    plt.show()
cluster_centers_df = cluster_centers_dataframe(features, cluster_centers)
plot_parallel_coordinates(cluster_centers_df[cluster_centers_df['relative_humidity'] < -0.5])
plot_parallel_coordinates(cluster_centers_df[cluster_centers_df['air_temp'] > 0.5])
plot_parallel_coordinates(cluster_centers_df[(cluster_centers_df['relative_humidity'] > 0.5) &
                                              (cluster_centers_df['air_temp'] < 0.5)])