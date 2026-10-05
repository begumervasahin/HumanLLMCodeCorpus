import pandas as pd
from auxiliaryfunctions import haversine_np
df = pd.read_pickle('final_cleaned.df')
cell_size = 0.2
zero_point = [0, -6.61505, 53.07045]
df_final = pd.DataFrame(columns=['TripId', 'Grids'])
for index, row in df.iterrows():
    grid = ''
    trajectory = df.loc[index, 'timestamp_longitude_latitude']
    last_cell = None
    for point in trajectory:
        lon_distance = haversine_np([zero_point[0], point[1], zero_point[2]], zero_point)
        lat_distance = haversine_np([zero_point[0], zero_point[1], point[2]], zero_point)
        grid_lon = int(lon_distance
        grid_lat = int(lat_distance
        current_cell = f"{grid_lat},{grid_lon}"
        if current_cell == last_cell:
            continue
        grid += f'C{current_cell};'
        last_cell = current_cell
    df_final = df_final.append({'TripId': df.loc[index, 'TripId'], 'Grids': grid}, ignore_index=True)
df_final.to_csv('grids.csv', index=False)