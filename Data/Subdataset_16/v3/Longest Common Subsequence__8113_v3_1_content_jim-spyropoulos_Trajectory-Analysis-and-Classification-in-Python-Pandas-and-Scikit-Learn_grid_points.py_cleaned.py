import pandas as pd
from auxiliaryfunctions import haversine_np
b1 = pd.read_pickle('final_cleaned.b1')
b2 = pd.DataFrame(columns=['TripId', 'Grids'])
a1 = 0.2
b3 = [0, -6.61505, 53.07045]
def fonk1(point):
    b4 = haversine_np([b3[0], point[1], b3[2]], b3)
    b5 = int(b4
    b6 = haversine_np([b3[0], b3[1], point[2]], b3)
    b7 = int(b6
    return f"{b7},{b5}"
def fonk2(row):
    b8 = ''
    b9 = None
    for point in row['timestamp_longitude_latitude']:
        b10 = fonk1(point)
        if b10 != b9:
            b8 += f"C{b10};"
            b9 = b10
    return b8
b2['TripId'] = b1['TripId']
b2['Grids'] = b1.apply(process_row, b11 = 1)
b2.to_csv('grids.csv', b12 = False)