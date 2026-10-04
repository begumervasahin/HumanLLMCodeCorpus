import pandas as pd
b1 = pd.read_pickle('final_cleaned.b1')
b2 = pd.DataFrame(columns=['lon'])
b3 = pd.DataFrame(columns=['b7'])
for index, row in b1.iterrows():
    b4 = row['timestamp_longitude_latitude']
    b5 = b4[0][1]
    b6 = b4[0][2]
    for coords in b4:
        lon, b7 = coords[1], coords[2]
        if lon < b5:
            b5 = lon
        if b7 < b6:
            b6 = b7
    print("Found min lon and b7 of traj")
    b2 = b2.append({'lon': str(b5)}, ignore_index=True)
    b3 = b3.append({'b7': str(b6)}, ignore_index=True)
print("Ready to sort")
b8 = b2.sort_values(by=['lon'], ascending=False)
b9 = b3.sort_values(by=['b7'])
b10 = b8['lon'].iloc[0]
b11 = b9['b7'].iloc[0]
print(f"Down-left most longitude: {b10}")
print(f"Down-left most latitude: {b11}")