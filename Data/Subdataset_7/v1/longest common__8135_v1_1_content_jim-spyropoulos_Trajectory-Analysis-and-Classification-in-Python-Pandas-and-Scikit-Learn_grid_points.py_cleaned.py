import pandas as pd
from auxiliaryfunctions import haversine_np
b1 = pd.read_pickle('final_cleaned.b1')
b2 = pd.DataFrame(columns=['TripId', 'Grids'])
a1 = 0.2
b3 = [0, -6.61505, 53.07045]
for b14, row in b1.iterrows():
    b4 = ''
    b5 = b1['timestamp_longitude_latitude'][b14]
    b6 = ' '
    for i in range(0, len(b5)):
        b7 = [b3[0], b5[i][1], b3[2]]
        b8 = haversine_np(b7, b3)
        b9 = int(b8
        b10 = [b3[0], b3[1], b5[i][2]]
        b11 = haversine_np(b10, b3)
        b12 = int(b11
        b13 = f"{b12},{b9}"
        if b13 = = b6:
            continue
        b4 += f'C{b13};'
        b6 = b13
    b2 = b2.append({'TripId': b1['TripId'][b14], 'Grids': b4}, ignore_index=True)
b2.to_csv('grids.csv', b14 = False)