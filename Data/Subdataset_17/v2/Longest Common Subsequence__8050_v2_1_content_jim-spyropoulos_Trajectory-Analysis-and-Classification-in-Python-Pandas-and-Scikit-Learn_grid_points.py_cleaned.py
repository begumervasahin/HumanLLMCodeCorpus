import pandas as pd
from auxiliaryfunctions import haversine_np
df = pd.read_pickle('final_cleaned.df')
df_final = pd.DataFrame(columns=['TripId', 'Grids'])
CELL_SIZE = 0.2
ZERO_POINT = [0, -6.61505, 53.07045]
def calculate_grid_cell(point):
    on_longitude_axis = [ZERO_POINT[0], point[1], ZERO_POINT[2]]
    dist_of_longitude_axis = haversine_np(on_longitude_axis, ZERO_POINT)
    grid_lon = int(dist_of_longitude_axis
    on_latitude_axis = [ZERO_POINT[0], ZERO_POINT[1], point[2]]
    dist_of_latitude_axis = haversine_np(on_latitude_axis, ZERO_POINT)
    grid_lat = int(dist_of_latitude_axis
    return f"{grid_lat},{grid_lon}"
for index, row in df.iterrows():
    grid_sequence = ''
    trajectory = row['timestamp_longitude_latitude']
    last_cell = None
    for point in trajectory:
        current_cell = calculate_grid_cell(point)
        if current_cell != last_cell:
            grid_sequence += f"C{current_cell};"
            last_cell = current_cell
    df_final = df_final.append({'TripId': row['TripId'], 'Grids': grid_sequence}, ignore_index=True)
df_final.to_csv('grids.csv', index=False)