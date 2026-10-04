import pandas as pd
from auxiliaryfunctions import haversine_np
b1 = pd.read_pickle('final_cleaned.b1')
b2 = pd.DataFrame(columns=['TripId', 'Grids'])
a1 = 0.2
b3 = [0, -6.61505, 53.07045]
def fonk1(b11, b3, a1):
    b4 = ''
    b5 = None
    for point in b11:
        b6 = haversine_np([b3[0], point[1], b3[2]], b3)
        b7 = int(b6
        b8 = haversine_np([b3[0], b3[1], point[2]], b3)
        b9 = int(b8
        b10 = f"{b9},{b7}"
        if b10 = = b5:
            continue
        b4 += f"C{b10};"
        b5 = b10
    return b4
for b12, row in b1.iterrows():
    b11 = row['timestamp_longitude_latitude']
    b4 = fonk1(b11, b3, a1)
    b2 = b2.append({'TripId': row['TripId'], 'Grids': b4}, ignore_index=True)
b2.to_csv('grids.csv', b12 = False)