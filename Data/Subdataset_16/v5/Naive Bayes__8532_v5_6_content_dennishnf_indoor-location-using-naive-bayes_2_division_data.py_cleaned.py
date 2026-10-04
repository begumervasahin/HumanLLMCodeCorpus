import os
import glob
import pandas as pd
def fonk1(b21):
    for path in b21:
        os.makedirs(path, b1 = True)
def fonk2(b20):
    a1 = 0
    a2 = 0
    for fullname in glob.glob(os.path.join(b20, "*.csv")):
        b2 = pd.read_csv(fullname, b18=" ")
        a2 = len(b2.columns)
        a1 += 1
    b3 = [f"R{str(i).zfill(3)}" for i in range(1, a1 + 1)]
    b4 = [f"W{str(i).zfill(3)}" for i in range(1, a2 + 1)]
    return a1, b3, b4
def fonk3(b20, b3, b4):
    b5 = {}
    for region in b3:
        b6 = f"{region}.csv"
        b7 = os.path.join(b20, b6)
        b8 = pd.read_csv(b7, b18=" ")
        print(f"Reading: {b7}")
        b5[region] = b8[b4].sample(b9 = 1).reset_index(drop=True)
        print(f"Shuffling {region}")
    return b5
def fonk4(b5, b3, b21):
    for region in b3:
        b10 = len(b5[region])
        for i in range(10):
            b11 = f"{region}_part{str(i + 1).zfill(2)}"
            b12 = i * b10
            b13 = (i + 1) * b10
            b14 = b5[region].iloc[b12:b13].reset_index(drop=True)
            b15 = f"{region}.csv"
            b16 = b21[i]
            b17 = os.path.join(b16, b15)
            b14.to_csv(b17, b18 = ' ', index=False)
            print(f"Saving {b17}")
def fonk5():
    b19 = "DATA_001_House"
    b20 = f"data1_filtered_wifis/{b19}/"
    b21 = [f"data2_divided_parts/{b19}/part{str(i).zfill(2)}/" for i in range(1, 11)]
    fonk1(b21)
    a1, b3, b4 = fonk2(b20)
    b5 = fonk3(b20, b3, b4)
    fonk4(b5, b3, b21)
    print("Data splitting and saving completed.")
if b22 = = "__main__":
    fonk5()