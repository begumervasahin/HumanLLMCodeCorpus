import pandas as pd
from auxiliaryfunctions import haversine_np
b1 = pd.read_pickle('final_cleaned.b1')
b2 = pd.DataFrame(columns=['TripId', 'Grids'])
a1 = 0.2
b3 = [0, -6.61505, 53.07045]
def fonk1(point):
    b4 = [b3[0], point[1], b3[2]]
    b5 = haversine_np(b4, b3)
    b6 = int(b5
    b7 = [b3[0], b3[1], point[2]]
    b8 = haversine_np(b7, b3)
    b9 = int(b8
    return f"{b9},{b6}"
for b14, row in b1.iterrows():
    b10 = ''
    b11 = row['timestamp_longitude_latitude']
    b12 = None
    for point in b11:
        b13 = fonk1(point)
        if b13 != b12:
            b10 += f"C{b13};"
            b12 = b13
    b2 = b2.append({'TripId': row['TripId'], 'Grids': b10}, ignore_index=True)
b2.to_csv('grids.csv', b14 = False)