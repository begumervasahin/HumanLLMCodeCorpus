import pandas as pd
from auxiliaryfunctions import haversine_np
b1 = pd.read_pickle('final_cleaned.b1')
a1 = 0.2
b2 = [0, -6.61505, 53.07045]
b3 = pd.DataFrame(columns=['TripId', 'Grids'])
for b12, row in b1.iterrows():
    b4 = ''
    b5 = b1.loc[b12, 'timestamp_longitude_latitude']
    b6 = None
    for point in b5:
        b7 = haversine_np([b2[0], point[1], b2[2]], b2)
        b8 = haversine_np([b2[0], b2[1], point[2]], b2)
        b9 = int(b7
        b10 = int(b8
        b11 = f"{b10},{b9}"
        if b11 = = b6:
            continue
        b4 += f'C{b11};'
        b6 = b11
    b3 = b3.append({'TripId': b1.loc[b12, 'TripId'], 'Grids': b4}, ignore_index=True)
b3.to_csv('grids.csv', b12 = False)