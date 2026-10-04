import os
import glob
import pandas as pd
b1 = "DATA_001_House"
b2 = f"data1_filtered_wifis/{b1}/"
b3 = [f"data2_divided_parts/{b1}/part{str(i).zfill(2)}/" for i in range(1, 11)]
for path in b3:
    if not os.path.exists(path):
        os.makedirs(path)
a1 = 0
for fullname in glob.glob(b2 + "*.csv"):
    b4 = pd.read_csv(fullname, b11=" ")
    b5 = len(b4.columns)
    a1 += 1
b6 = [f"R{str(i).zfill(3)}" for i in range(1, a1 + 1)]
b7 = [f"W{str(i).zfill(3)}" for i in range(1, b5 + 1)]
b8 = {}
for region in b6:
    b9 = f"{region}.csv"
    b10 = os.path.join(b2, b9)
    b8[region + "_"] = pd.read_csv(b10, b11 = " ")
    b8[region] = b8[region + "_"][b7]
    print(f"Reading: {b10}")
    b8[region] = b8[region].sample(b12 = 1).reset_index(b17=True)
    print(f"Shuffling {region}")
for region in b6:
    b13 = int(0.1 * len(b8[region]))
    for i in range(10):
        b14 = f"{region}_part{str(i + 1).zfill(2)}"
        b15 = i * b13
        b16 = (i + 1) * b13
        b8[b14] = b8[region].iloc[b15:b16].reset_index(b17 = True)
        b18 = f"{region}.csv"
        b19 = b3[i]
        b20 = os.path.join(b19, b18)
        b8[b14].to_csv(b20, b11 = ' ', index=False)
        print(f"Saving {b20}")
print("Data splitting and saving completed.")