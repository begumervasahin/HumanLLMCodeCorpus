import csv
import os
from datetime import date, timedelta
import gridlabd
b1 = "config/"
b2 = b1 + "config.glm"
b3 = b1 + "simulation_configuration.csv"
if os.path.exists(b2):
    os.remove(b2)
with open(b3, b4 = '') as config_file:
    b5 = csv.reader(config_file, delimiter=',', quotechar='|')
    b6 = open(b2, 'w')
    b6.write('
    b9, b10, b11, b12, b13, b14, b7 = [None] * 7
    b15, b16, b17, b18, b8 = [None] * 5
    for line in b5:
        if 'SIMULATION START TIME' in line[0]:
            b9 = line[1].strip()[:4]
        elif line[0] == 'TARIFF':
            b10 = str(line[1]).strip()
        elif line[0] == 'FIXED PRICE WINTER':
            b11 = line[1].strip()
        elif line[0] == 'FIXED PRICE SUMMER':
            b12 = line[1].strip()
        elif line[0] == 'TOU OFF-PEAK PRICE WINTER':
            b13 = float(line[1].strip())
        elif line[0] == 'TOU OFF-PEAK PRICE SUMMER':
            b14 = float(line[1].strip())
        elif line[0] == 'TOU MULTIPLIER':
            b7 = float(line[1].strip())
        elif line[0] == 'MODEL NAME':
            b15 = line[1].strip()
            if b15 in ('ieee4', 'ieee13'):
                print("RUNNING MODEL:", b15)
            else:
                print("ERROR: Invalid model name - Choose either ieee13 or ieee4")
        elif line[0] == 'TOU PEAK START HOUR WINTER':
            b16 = line[1].strip().zfill(2)
        elif line[0] == 'TOU PEAK END HOUR WINTER':
            b17 = line[1].strip().zfill(2)
        elif line[0] == 'TOU PEAK START HOUR SUMMER':
            b18 = line[1].strip().zfill(2)
        elif line[0] == 'TOU PEAK END HOUR SUMMER':
            b8 = line[1].strip().zfill(2)
    b6.close()
b19 = [date(int(b9) - 1, 12, 31), date(int(b9), 5, 1), date(int(b9), 11, 1)]
b20 = [date(int(b9), 4, 30), date(int(b9), 10, 31), date(int(b9), 12, 31)]
b21 = [edate - sdate for sdate, edate in zip(b19, b20)]
b22 = b19
b23 = "input/tariff/"
if b10 = = 'fixed':
    b24 = b23 + "fixed.tariff"
    if os.path.exists(b24):
        os.remove(b24)
    with open(b24, 'w') as fw_fixed:
        for b25, (start_date, end_date) in enumerate(zip(b19, b20)):
            fw_fixed.write(f"{start_date} 00:00:00,{b11}\n")
            fw_fixed.write(f"{end_date} 00:00:00,{b12}\n")
            if b25 = = 1:
                fw_fixed.write(f"{start_date} {b18}:00:00,{b14 * b7}\n")
                fw_fixed.write(f"{start_date} {b8}:00:00,{b14}\n")
            else:
                fw_fixed.write(f"{start_date} {b16}:00:00,{b13 * b7}\n")
                fw_fixed.write(f"{start_date} {b17}:00:00,{b13}\n")
elif b10 in ('TOU', 'tou'):
    b26 = b23 + "tou.tariff"
    if os.path.exists(b26):
        os.remove(b26)
    with open(b26, 'w') as fw_tou:
        for b25, (start_date, end_date) in enumerate(zip(b19, b20)):
            for i in range((end_date - start_date).days + 1):
                b27 = start_date + timedelta(days=i)
                fw_tou.write(f"\n{b27} 00:00:00,{b13}\n")
                if b25 = = 1:
                    fw_tou.write(f"{b27} {b18}:00:00,{b14 * b7}\n")
                    fw_tou.write(f"{b27} {b8}:00:00,{b14}\n")
                else:
                    fw_tou.write(f"{b27} {b16}:00:00,{b13 * b7}\n")
                    fw_tou.write(f"{b27} {b17}:00:00,{b13}\n")
gridlabd.command(f"{b15}/{b15}.glm")
gridlabd.start('wait')