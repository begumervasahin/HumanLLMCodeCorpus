import pandas as pd
b1 = pd.read_pickle('final_cleaned.b1')
b2 = pd.DataFrame(columns=['b5'])
b3 = pd.DataFrame(columns=['b6'])
for index, row in b1.iterrows():
    b4 = b1['timestamp_longitude_latitude'].iloc[index]
    b5 = min(point[1] for point in b4)
    b6 = min(point[2] for point in b4)
    b2 = b2.append({'b5': b5}, ignore_index=True)
    b3 = b3.append({'b6': b6}, ignore_index=True)
print("Found the minimum longitude and latitude for each b4.")
b7 = b2.sort_values(by=['b5'], ascending=False)
b8 = b3.sort_values(by=['b6'])
b9 = b7['b5'].iloc[0]
b10 = b8['b6'].iloc[0]
print("Lowest Longitude:", b9)
print("Lowest Latitude:", b10)