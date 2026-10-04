import pandas as pd
df = pd.read_pickle('final_cleaned.df')
min_lon_df = pd.DataFrame(columns=['lon'])
min_lat_df = pd.DataFrame(columns=['lat'])
for index, row in df.iterrows():
    coordinates_list = row['timestamp_longitude_latitude']
    min_lon = coordinates_list[0][1]
    min_lat = coordinates_list[0][2]
    for coords in coordinates_list:
        lon, lat = coords[1], coords[2]
        if lon < min_lon:
            min_lon = lon
        if lat < min_lat:
            min_lat = lat
    print("Found min lon and lat of traj")
    min_lon_df = min_lon_df.append({'lon': str(min_lon)}, ignore_index=True)
    min_lat_df = min_lat_df.append({'lat': str(min_lat)}, ignore_index=True)
print("Ready to sort")
sorted_lon_df = min_lon_df.sort_values(by=['lon'], ascending=False)
sorted_lat_df = min_lat_df.sort_values(by=['lat'])
downleft_lon = sorted_lon_df['lon'].iloc[0]
downleft_lat = sorted_lat_df['lat'].iloc[0]
print(f"Down-left most longitude: {downleft_lon}")
print(f"Down-left most latitude: {downleft_lat}")