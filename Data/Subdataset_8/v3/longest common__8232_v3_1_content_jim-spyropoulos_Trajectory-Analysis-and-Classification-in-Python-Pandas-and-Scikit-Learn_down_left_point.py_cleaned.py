import pandas as pd
df = pd.read_pickle('final_cleaned.df')
min_lon_df = pd.DataFrame(columns=['min_lon'])
min_lat_df = pd.DataFrame(columns=['min_lat'])
for index, row in df.iterrows():
    trajectory = df['timestamp_longitude_latitude'].iloc[index]
    min_lon = min(point[1] for point in trajectory)
    min_lat = min(point[2] for point in trajectory)
    min_lon_df = min_lon_df.append({'min_lon': min_lon}, ignore_index=True)
    min_lat_df = min_lat_df.append({'min_lat': min_lat}, ignore_index=True)
print("Found the minimum longitude and latitude for each trajectory.")
sorted_min_lon_df = min_lon_df.sort_values(by=['min_lon'], ascending=False)
sorted_min_lat_df = min_lat_df.sort_values(by=['min_lat'])
lowest_lon = sorted_min_lon_df['min_lon'].iloc[0]
lowest_lat = sorted_min_lat_df['min_lat'].iloc[0]
print("Lowest Longitude:", lowest_lon)
print("Lowest Latitude:", lowest_lat)