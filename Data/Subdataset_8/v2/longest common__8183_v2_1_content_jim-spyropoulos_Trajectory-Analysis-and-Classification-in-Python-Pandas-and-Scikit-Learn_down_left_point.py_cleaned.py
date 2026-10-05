import pandas as pd
df = pd.read_pickle('final_cleaned.df')
df_lon = pd.DataFrame(columns=['lon'])
df_lat = pd.DataFrame(columns=['lat'])
for index, row in df.iterrows():
    trajectory = df['timestamp_longitude_latitude'].iloc[index]
    min_lon = trajectory[0][1]
    min_lat = trajectory[0][2]
    for point in trajectory:
        temp_lon = point[1]
        temp_lat = point[2]
        if temp_lon < min_lon:
            min_lon = temp_lon
        if temp_lat < min_lat:
            min_lat = temp_lat
    df_lon = df_lon.append({'lon': min_lon}, ignore_index=True)
    df_lat = df_lat.append({'lat': min_lat}, ignore_index=True)
print("Found the minimum longitude and latitude for each trajectory.")
df_lon_sorted = df_lon.sort_values(by=['lon'], ascending=False)
df_lat_sorted = df_lat.sort_values(by=['lat'])
lowest_lon = df_lon_sorted['lon'].iloc[0]
lowest_lat = df_lat_sorted['lat'].iloc[0]
print("Lowest Longitude:", lowest_lon)
print("Lowest Latitude:", lowest_lat)