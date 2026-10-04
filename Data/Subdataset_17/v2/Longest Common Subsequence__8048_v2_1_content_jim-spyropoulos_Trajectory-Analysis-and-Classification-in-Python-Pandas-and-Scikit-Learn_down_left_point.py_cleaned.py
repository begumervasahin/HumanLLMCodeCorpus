import pandas as pd
df = pd.read_pickle('final_cleaned.df')
df_2 = pd.DataFrame(columns=['lon', 'the', 'timestamp_longitude_latitude'])
df_3 = pd.DataFrame(columns=['lat', 'the', 'timestamp_longitude_latitude'])
for index, row in df.iterrows():
    coordinates_list = row['timestamp_longitude_latitude']
    min_lon = coordinates_list[0][1]
    min_lat = coordinates_list[0][2]
    the_lon = f"{coordinates_list[0][1]},{coordinates_list[0][2]}"
    the_lat = f"{coordinates_list[0][1]},{coordinates_list[0][2]}"
    for coords in coordinates_list:
        lon, lat = coords[1], coords[2]
        if lon < min_lon:
            min_lon = lon
            the_lon = f"{lon},{lat}"
        if lat < min_lat:
            min_lat = lat
            the_lat = f"{lon},{lat}"
    print("Found min lon and lat of traj")
    df_2 = df_2.append({'lon': str(min_lon)}, ignore_index=True)
    df_3 = df_3.append({'lat': str(min_lat)}, ignore_index=True)
print("Ready to sort")
df_2_sorted = df_2.sort_values(by=['lon'], ascending=False)
df_3_sorted = df_3.sort_values(by=['lat'])
downleft_lon = df_2_sorted['lon'].iloc[0]
downleft_lat = df_3_sorted['lat'].iloc[0]
print(downleft_lon)
print(downleft_lat)