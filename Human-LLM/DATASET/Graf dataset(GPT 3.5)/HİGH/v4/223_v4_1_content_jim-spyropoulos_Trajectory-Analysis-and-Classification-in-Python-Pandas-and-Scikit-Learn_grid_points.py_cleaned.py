import pandas as pd
from auxiliaryfunctions import haversine_np
b1 = pd.read_pickle('final_cleaned.b1')
b2 = pd.DataFrame(columns=['TripId', 'Grids'])
a1 = 0.2
b3 = [0, -6.61505, 53.07045]
for b14, row in b1.iterrows():
    b4 = ''
    b5 = b1['timestamp_longitude_latitude'][b14]
    b6 = None
    for point in b5:
        b7 = [b3[0], point[1], b3[2]]
        b8 = [b3[0], b3[1], point[2]]
        b9 = haversine_np(b7, b3)
        b10 = haversine_np(b8, b3)
        b11 = int(b9
        b12 = int(b10
        b13 = f"{b12},{b11}"
        if b13 = = b6:
            continue
        b4 += f'C{b13};'
        b6 = b13
    b2 = b2.append({'TripId': b1['TripId'][b14], 'Grids': b4}, ignore_index=True)
b2.to_csv('grids.csv', b14 = False)