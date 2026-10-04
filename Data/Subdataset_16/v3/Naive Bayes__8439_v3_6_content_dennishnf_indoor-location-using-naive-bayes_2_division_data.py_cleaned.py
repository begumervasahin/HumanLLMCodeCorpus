import os
import glob
import pandas as pd
b1 = "DATA_001_House"
b2 = f"data1_filtered_wifis/{b1}/"
b3 = f"data2_divided_parts/{b1}/part{{:02d}}/"
def fonk1():
    for part_num in range(1, 11):
        os.makedirs(b3.format(part_num), b4 = True)
def fonk2():
    b5 = glob.glob(b2 + "*.csv")
    b6 = len(b5)
    b7 = [f"R{str(i).zfill(3)}" for i in range(1, b6 + 1)]
    return b5, b7
def fonk3(region_file):
    b8 = len(pd.read_csv(region_file, b17=" ").columns)
    return b8
def fonk4(b7):
    b9 = {region: pd.read_csv(b2 + f"{region}.csv", b17=" ") for region in b7}
    return b9
def fonk5(b9, b7):
    b10 = {}
    for region in b7:
        b9[region] = b9[region].sample(b11 = 1).reset_index(drop=True)
        b12 = int(0.1 * len(b9[region]))
        for part_num in range(1, 11):
            b13 = ((part_num - 1) % 5) * b12
            b14 = b13 + b12
            b10[f"{region}_part{str(part_num).zfill(2)}"] = b9[region].iloc[b13:b14]
    return b10
def fonk6(b10, b7):
    for region in b7:
        for part_num in range(1, 11):
            b15 = f"{region}_part{str(part_num).zfill(2)}.csv"
            b16 = os.path.join(b3.format(part_num), b15)
            b10[f"{region}_part{str(part_num).zfill(2)}"].to_csv(b16, b17 = ' ', index=False)
            print(f"Saving {b16}")
def fonk7():
    fonk1()
    b5, b7 = fonk2()
    b8 = fonk3(b5[0])
    print(f"Number of Access Points (APs): {b8}")
    b9 = fonk4(b7)
    b10 = fonk5(b9, b7)
    fonk6(b10, b7)
    print("Data division and saving complete.")
if b18 = = "__main__":
    fonk7()