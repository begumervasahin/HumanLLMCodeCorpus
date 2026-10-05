import pandas as pd
from auxiliaryfunctions import *
b1 = pd.read_pickle('final_cleaned.b1')
b2 = pd.DataFrame(columns=['TripId', 'Grids'])
a1 = 0.2
b3 = [0, -6.61505, 53.07045]
for index, row in b1.iterrows():
    b4 = ''
    b5 = b1['timestamp_longitude_latitude'][index]
    b6 = ' '
    for i in range(0, len(b5)):
        b7 = []
        b8 = []
        b7.append(b3[0])
        b7.append(b5[i][1])
        b7.append(b3[2])
        b9 = haversine_np(b7, b3)
        b10 = int(b9
        b8.append(b3[0])
        b8.append(b3[1])
        b8.append(b5[i][2])
        b11 = haversine_np(b8, b3)
        b12 = int(b11
        b13 = str(b12) + ',' + str(b10)
        if b13 = = b6:
            continue
        b4 = b4 + 'C' + b13 + ';'
        b6 = b13
    b2 = b2.append({'TripId': b1['TripId'][index], 'Grids': b4}, ignore_index=True)
b2.to_csv('grids.csv')