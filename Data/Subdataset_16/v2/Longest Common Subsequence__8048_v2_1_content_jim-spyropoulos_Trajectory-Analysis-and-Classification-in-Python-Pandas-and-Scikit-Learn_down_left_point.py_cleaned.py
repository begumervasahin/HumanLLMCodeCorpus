import pandas as pd
b1 = pd.read_pickle('final_cleaned.b1')
b2 = pd.DataFrame(columns=['lon', 'the', 'timestamp_longitude_latitude'])
b3 = pd.DataFrame(columns=['b9', 'the', 'timestamp_longitude_latitude'])
for index, row in b1.iterrows():
    b4 = row['timestamp_longitude_latitude']
    b5 = b4[0][1]
    b6 = b4[0][2]
    b7 = f"{b4[0][1]},{b4[0][2]}"
    b8 = f"{b4[0][1]},{b4[0][2]}"
    for coords in b4:
        lon, b9 = coords[1], coords[2]
        if lon < b5:
            b5 = lon
            b7 = f"{lon},{b9}"
        if b9 < b6:
            b6 = b9
            b8 = f"{lon},{b9}"
    print("Found min lon and b9 of traj")
    b2 = b2.append({'lon': str(b5)}, ignore_index=True)
    b3 = b3.append({'b9': str(b6)}, ignore_index=True)
print("Ready to sort")
b10 = b2.sort_values(by=['lon'], ascending=False)
b11 = b3.sort_values(by=['b9'])
b12 = b10['lon'].iloc[0]
b13 = b11['b9'].iloc[0]
print(b12)
print(b13)