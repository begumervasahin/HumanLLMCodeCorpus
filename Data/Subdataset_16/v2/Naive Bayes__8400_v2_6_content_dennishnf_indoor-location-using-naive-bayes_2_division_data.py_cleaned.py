import os
import glob
import pandas as pd
b1 = "DATA_001_House"
b2 = f"data1_filtered_wifis/{b1}/"
b3 = f"data2_divided_parts/{b1}/part{{:02d}}/"
for part_num in range(1, 11):
    os.makedirs(b3.format(part_num), b4 = True)
b5 = glob.glob(b2 + "*.csv")
b6 = len(b5)
b7 = [f"R{str(i).zfill(3)}" for i in range(1, b6 + 1)]
b8 = len(pd.read_csv(b5[0], b18=" ").columns)
b9 = [f"W{str(i).zfill(3)}" for i in range(1, b8 + 1)]
b10 = {region: pd.read_csv(b2 + f"{region}.csv", b18=" ") for region in b7}
b11 = {}
for region in b7:
    b10[region] = b10[region].sample(b12 = 1).reset_index(drop=True)
    b13 = int(0.1 * len(b10[region]))
    for part_num in range(1, 11):
        b14 = ((part_num - 1) % 5) * b13
        b15 = b14 + b13
        b11[f"{region}_part{str(part_num).zfill(2)}"] = b10[region].iloc[b14:b15]
for region in b7:
    for part_num in range(1, 11):
        b16 = f"{region}_part{str(part_num).zfill(2)}.csv"
        b17 = os.path.join(b3.format(part_num), b16)
        b11[f"{region}_part{str(part_num).zfill(2)}"].to_csv(b17, b18 = ' ', index=False)
        print(f"Saving {b17}")
if b19 = = "__main__":
    print("Data division and saving complete.")