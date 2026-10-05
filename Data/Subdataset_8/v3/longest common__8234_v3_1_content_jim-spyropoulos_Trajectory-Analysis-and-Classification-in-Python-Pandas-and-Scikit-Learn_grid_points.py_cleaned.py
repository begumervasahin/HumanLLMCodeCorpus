import pandas as pd
from auxiliaryfunctions import haversine_np
df = pd.read_pickle('final_cleaned.df')
df_final = pd.DataFrame(columns=['TripId', 'Grids'])
cell_size = 0.2
zero_point = {'longitude': 0, 'latitude': -6.61505, 'longitude_ref': 53.07045}
for index, row in df.iterrows():
    grid = ''
    trajectory = df.loc[index, 'timestamp_longitude_latitude']
    last_grid = None
    for point in trajectory:
        lon_distance = haversine_np([zero_point['longitude'], point[1], zero_point['longitude_ref']], zero_point)
        lat_distance = haversine_np([zero_point['longitude'], zero_point['latitude'], point[2]], zero_point)
        grid_lon = int(lon_distance
        grid_lat = int(lat_distance
        current_grid = f"{grid_lat},{grid_lon}"
        if current_grid == last_grid:
            continue
        grid += f'C{current_grid};'
        last_grid = current_grid
    df_final = df_final.append({'TripId': df.loc[index, 'TripId'], 'Grids': grid}, ignore_index=True)
df_final.to_csv('grids.csv', index=False)