import os
import glob
import pandas as pd
b1 = "DATA_001_House"
b2 = f"data1_filtered_wifis/{b1}/"
b3 = f"data2_divided_parts/{b1}/part{{:02d}}/"
for part_num in range(1, 11):
    os.makedirs(b3.format(part_num), b4 = True)
b5 = len(glob.glob(b2 + "*.csv"))
b6 = [f"R{str(i).zfill(3)}" for i in range(1, b5 + 1)]
b7 = len(pd.read_csv(glob.glob(b2 + "*.csv")[0], b17=" ").columns)
b8 = [f"W{str(i).zfill(3)}" for i in range(1, b7 + 1)]
b9 = {region: pd.read_csv(b2 + f"{region}.csv", b17=" ") for region in b6}
b10 = {}
for region in b6:
    b9[region] = b9[region].sample(b11 = 1).reset_index(drop=True)
    b12 = int(0.1 * len(b9[region]))
    for part_num in range(1, 11):
        b13 = (part_num - 1) % 5 * b12
        b14 = b13 + b12
        b10[f"{region}_part{str(part_num).zfill(2)}"] = b9[region].iloc[b13:b14]
for region in b6:
    for part_num in range(1, 11):
        b15 = f"{region}_part{str(part_num).zfill(2)}.csv"
        b16 = b3.format(part_num) + b15
        b10[f"{region}_part{str(part_num).zfill(2)}"].to_csv(b16, b17 = ' ', index=False)
        print(f"Saving {b16}")