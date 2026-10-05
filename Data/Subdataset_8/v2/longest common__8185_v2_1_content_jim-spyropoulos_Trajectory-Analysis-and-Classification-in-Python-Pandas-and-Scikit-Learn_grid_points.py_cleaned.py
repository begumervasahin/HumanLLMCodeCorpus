import pandas as pd
from auxiliaryfunctions import haversine_np
df = pd.read_pickle('final_cleaned.df')
df_final = pd.DataFrame(columns=['TripId', 'Grids'])
cell_size = 0.2
zero_point = [0, -6.61505, 53.07045]
for index, row in df.iterrows():
    grid = ''
    trajectory = df['timestamp_longitude_latitude'][index]
    last_grid = None
    for point in trajectory:
        lon_distance = haversine_np([zero_point[0], point[1], zero_point[2]], zero_point)
        lat_distance = haversine_np([zero_point[0], zero_point[1], point[2]], zero_point)
        grid_lon = int(lon_distance
        grid_lat = int(lat_distance
        current_grid = f"{grid_lat},{grid_lon}"
        if current_grid == last_grid:
            continue
        grid += f'C{current_grid};'
        last_grid = current_grid
    df_final = df_final.append({'TripId': df['TripId'][index], 'Grids': grid}, ignore_index=True)
df_final.to_csv('grids.csv', index=False)