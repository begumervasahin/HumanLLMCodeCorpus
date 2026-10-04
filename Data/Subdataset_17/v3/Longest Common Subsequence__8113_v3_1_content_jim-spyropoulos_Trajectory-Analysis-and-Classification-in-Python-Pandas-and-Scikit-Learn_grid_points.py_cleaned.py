import pandas as pd
from auxiliaryfunctions import haversine_np
df = pd.read_pickle('final_cleaned.df')
df_final = pd.DataFrame(columns=['TripId', 'Grids'])
CELL_SIZE = 0.2
ZERO_POINT = [0, -6.61505, 53.07045]
def calculate_grid_cell(point):
    longitude_distance = haversine_np([ZERO_POINT[0], point[1], ZERO_POINT[2]], ZERO_POINT)
    grid_lon = int(longitude_distance
    latitude_distance = haversine_np([ZERO_POINT[0], ZERO_POINT[1], point[2]], ZERO_POINT)
    grid_lat = int(latitude_distance
    return f"{grid_lat},{grid_lon}"
def process_row(row):
    grid_sequence = ''
    last_cell = None
    for point in row['timestamp_longitude_latitude']:
        current_cell = calculate_grid_cell(point)
        if current_cell != last_cell:
            grid_sequence += f"C{current_cell};"
            last_cell = current_cell
    return grid_sequence
df_final['TripId'] = df['TripId']
df_final['Grids'] = df.apply(process_row, axis=1)
df_final.to_csv('grids.csv', index=False)