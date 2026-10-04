import pandas as pd
from auxiliaryfunctions import haversine_np
df = pd.read_pickle('final_cleaned.df')
df_final = pd.DataFrame(columns=['TripId', 'Grids'])
cell_size = 0.2
zero_point = [0, -6.61505, 53.07045]
def calculate_grid(trajectory, zero_point, cell_size):
    grid = ''
    last_cell = None
    for point in trajectory:
        dist_lon = haversine_np([zero_point[0], point[1], zero_point[2]], zero_point)
        grid_lon = int(dist_lon
        dist_lat = haversine_np([zero_point[0], zero_point[1], point[2]], zero_point)
        grid_lat = int(dist_lat
        current_cell = f"{grid_lat},{grid_lon}"
        if current_cell == last_cell:
            continue
        grid += f"C{current_cell};"
        last_cell = current_cell
    return grid
for index, row in df.iterrows():
    trajectory = row['timestamp_longitude_latitude']
    grid = calculate_grid(trajectory, zero_point, cell_size)
    df_final = df_final.append({'TripId': row['TripId'], 'Grids': grid}, ignore_index=True)
df_final.to_csv('grids.csv', index=False)