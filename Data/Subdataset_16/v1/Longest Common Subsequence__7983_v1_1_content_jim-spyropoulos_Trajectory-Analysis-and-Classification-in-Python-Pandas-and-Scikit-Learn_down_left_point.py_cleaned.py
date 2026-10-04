import pandas as pd
b1 = pd.read_pickle('final_cleaned.b1')
b2 = pd.DataFrame(columns=['lon', 'the', 'timestamp_longitude_latitude'])
b3 = pd.DataFrame(columns=['lat', 'the', 'timestamp_longitude_latitude'])
b4 = []
b5 = []
for index, row in b1.iterrows():
    b6 = b1['timestamp_longitude_latitude'].iloc[index]
    b7 = b6[0][1]
    b8 = b6[0][2]
    b9 = str(b6[0][1]) + ',' + str(b6[0][2])
    b10 = str(b6[0][1]) + ',' + str(b6[0][2])
    for i in range(len(b6)):
        b11 = b6[i][1]
        b12 = b6[i][2]
        if b11 < b7:
            b7 = b11
            b9 = str(b6[i][1]) + ',' + str(b6[i][2])
            b4 = b6
        if b12 < b8:
            b8 = b12
            b10 = str(b6[i][1]) + ',' + str(b6[i][2])
            b5 = b6
    print("Found min lon and lat of traj")
    b2 = b2.append({'lon': str(b7)}, ignore_index=True)
    b3 = b3.append({'lat': str(b8)}, ignore_index=True)
print("Ready to sort")
b2 = b2.sort_values(by=['lon'], ascending=False)
b3 = b3.sort_values(by=['lat'])
b13 = b2['lon'].iloc[0]
b14 = b3['lat'].iloc[0]
print(b13)
print(b14)