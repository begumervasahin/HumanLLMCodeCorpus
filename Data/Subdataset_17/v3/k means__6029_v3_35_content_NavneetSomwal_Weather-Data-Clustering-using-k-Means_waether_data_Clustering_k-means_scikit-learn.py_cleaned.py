import pandas as pd
import numpy as np
from itertools import cycle, islice
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from pandas.plotting import parallel_coordinates
def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    sampled_df = data[data['rowID'] % 10 == 0]
    sampled_df = sampled_df.drop(columns=['rain_accumulation', 'rain_duration'])
    sampled_df = sampled_df.dropna()
    return sampled_df
def extract_features(df):
    features = [
        'air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed',
        'max_wind_direction', 'max_wind_speed', 'relative_humidity'
    ]
    return df[features]
def perform_kmeans(X, n_clusters=12):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    return kmeans.fit(X)
def pd_centers(features_used, centers):
    col_names = features_used + ['prediction']
    center_data = [np.append(center, idx) for idx, center in enumerate(centers)]
    center_df = pd.DataFrame(center_data, columns=col_names)
    center_df['prediction'] = center_df['prediction'].astype(int)
    return center_df
def parallel_plot(data):
    colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(data)))
    plt.figure(figsize=(15, 8)).gca().set_ylim([-3, 3])
    parallel_coordinates(data, 'prediction', color=colors, marker='o')
    plt.show()
if __name__ == "__main__":
    data_file = './weather/minute_weather.csv'
    sampled_df = load_and_preprocess_data(data_file)
    features_df = extract_features(sampled_df)
    X = StandardScaler().fit_transform(features_df)
    kmeans_model = perform_kmeans(X)
    centers = kmeans_model.cluster_centers_
    center_df = pd_centers(features_df.columns.tolist(), centers)
    parallel_plot(center_df[center_df['relative_humidity'] < -0.5])
    parallel_plot(center_df[center_df['air_temp'] > 0.5])
    parallel_plot(center_df[(center_df['relative_humidity'] > 0.5) & (center_df['air_temp'] < 0.5)])