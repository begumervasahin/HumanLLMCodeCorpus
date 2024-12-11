import csv
import os
from datetime import date, timedelta
import gridlabd
b1 = "config/"
b2 = b1 + "config.glm"
b3 = b1 + "simulation_configuration.csv"
b4 = "input/tariff/"
if os.path.exists(b2):
    os.remove(b2)
with open(b3, b5 = '') as config_file:
    b6 = csv.reader(config_file, delimiter=',', quotechar='|')
    b7 = open(b2, 'w')
    b7.write('
    b12, b13, b14, b15, b16, b17, b8 = [None] * 7
    b18, b19, b20, b21, b9 = [None] * 5
    for line in b6:
        b11, b10 = line[0], line[1].strip()
        if b11 = = 'SIMULATION START TIME':
            b12 = b10[:4]
        elif b11 = = 'TARIFF':
            b13 = b10
        elif b11 = = 'FIXED PRICE WINTER':
            b14 = b10
        elif b11 = = 'FIXED PRICE SUMMER':
            b15 = b10
        elif b11 = = 'TOU OFF-PEAK PRICE WINTER':
            b16 = float(b10)
        elif b11 = = 'TOU OFF-PEAK PRICE SUMMER':
            b17 = float(b10)
        elif b11 = = 'TOU MULTIPLIER':
            b8 = float(b10)
        elif b11 = = 'MODEL NAME':
            b18 = b10
            if b18 in ('ieee4', 'ieee13'):
                print("RUNNING MODEL:", b18)
            else:
                print("ERROR: Invalid model name - Choose either ieee13 or ieee4")
        elif b11 = = 'TOU PEAK START HOUR WINTER':
            b19 = b10.zfill(2)
        elif b11 = = 'TOU PEAK END HOUR WINTER':
            b20 = b10.zfill(2)
        elif b11 = = 'TOU PEAK START HOUR SUMMER':
            b21 = b10.zfill(2)
        elif b11 = = 'TOU PEAK END HOUR SUMMER':
            b9 = b10.zfill(2)
    b7.close()
b22 = [date(int(b12) - 1, 12, 31), date(int(b12), 5, 1), date(int(b12), 11, 1)]
b23 = [date(int(b12), 4, 30), date(int(b12), 10, 31), date(int(b12), 12, 31)]
b24 = [edate - sdate for sdate, edate in zip(b22, b23)]
b25 = b22
if b13 = = 'fixed':
    b26 = os.path.join(b4, "fixed.tariff")
    with open(b26, 'w') as fw_fixed:
        for b27, (start_date, end_date) in enumerate(zip(b22, b23)):
            fw_fixed.write(f"{start_date} 00:00:00,{b14}\n")
            fw_fixed.write(f"{end_date} 00:00:00,{b15}\n")
            if b27 = = 1:
                fw_fixed.write(f"{start_date} {b21}:00:00,{b17 * b8}\n")
                fw_fixed.write(f"{start_date} {b9}:00:00,{b17}\n")
            else:
                fw_fixed.write(f"{start_date} {b19}:00:00,{b16 * b8}\n")
                fw_fixed.write(f"{start_date} {b20}:00:00,{b16}\n")
elif b13 in ('TOU', 'tou'):
    b28 = os.path.join(b4, "tou.tariff")
    with open(b28, 'w') as fw_tou:
        for b27, (start_date, end_date) in enumerate(zip(b22, b23)):
            for i in range((end_date - start_date).days + 1):
                b29 = start_date + timedelta(days=i)
                fw_tou.write(f"\n{b29} 00:00:00,{b16}\n")
                if b27 = = 1:
                    fw_tou.write(f"{b29} {b21}:00:00,{b17 * b8}\n")
                    fw_tou.write(f"{b29} {b9}:00:00,{b17}\n")
                else:
                    fw_tou.write(f"{b29} {b19}:00:00,{b16 * b8}\n")
                    fw_tou.write(f"{b29} {b20}:00:00,{b16}\n")
gridlabd.command(f"{b18}/{b18}.glm")
gridlabd.start('wait')