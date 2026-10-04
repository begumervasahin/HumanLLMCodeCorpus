import pandas as pd
from auxiliaryfunctions import haversine_np
df = pd.read_pickle('final_cleaned.df')
df_final = pd.DataFrame(columns=['TripId', 'Grids'])
cell_size = 0.2
zero_point = [0, -6.61505, 53.07045]
for index, row in df.iterrows():
    grid = ''
    trajectory = row['timestamp_longitude_latitude']
    last = ' '
    for point in trajectory:
        on_longitute_axis = [zero_point[0], point[1], zero_point[2]]
        dist_of_longitute_axis = haversine_np(on_longitute_axis, zero_point)
        grid_lon = int(dist_of_longitute_axis
        on_latitute_axis = [zero_point[0], zero_point[1], point[2]]
        dist_of_latitute_axis = haversine_np(on_latitute_axis, zero_point)
        grid_lat = int(dist_of_latitute_axis
        current_cell = f"{grid_lat},{grid_lon}"
        if current_cell == last:
            continue
        grid += f"C{current_cell};"
        last = current_cell
    df_final = df_final.append({'TripId': row['TripId'], 'Grids': grid}, ignore_index=True)
df_final.to_csv('grids.csv', index=False)