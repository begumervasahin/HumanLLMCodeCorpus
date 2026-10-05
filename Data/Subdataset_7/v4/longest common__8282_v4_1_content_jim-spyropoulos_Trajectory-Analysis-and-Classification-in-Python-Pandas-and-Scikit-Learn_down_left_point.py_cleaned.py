import pandas as pd
b1 = pd.read_pickle('final_cleaned.b1')
b2 = pd.DataFrame(columns=['lon'])
b3 = pd.DataFrame(columns=['lat'])
for index, row in b1.iterrows():
    b4 = b1['timestamp_longitude_latitude'].iloc[index]
    b5 = b4[0][1]
    b6 = b4[0][2]
    for point in b4:
        b7 = point[1]
        b8 = point[2]
        if b7 < b5:
            b5 = b7
        if b8 < b6:
            b6 = b8
    b2 = b2.append({'lon': str(b5)}, ignore_index=True)
    b3 = b3.append({'lat': str(b6)}, ignore_index=True)
print("Found the minimum longitude and latitude for each b4.")
b9 = b2.sort_values(by=['lon'], ascending=False)
b10 = b3.sort_values(by=['lat'])
b11 = b9['lon'].iloc[0]
b12 = b10['lat'].iloc[0]
print("Lowest Longitude:", b11)
print("Lowest Latitude:", b12)