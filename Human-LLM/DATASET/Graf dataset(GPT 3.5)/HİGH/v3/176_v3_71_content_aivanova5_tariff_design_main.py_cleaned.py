import csv
import os
from datetime import date, timedelta
import gridlabd
b1 = "config/"
b2 = b1 + "config.glm"
if os.path.exists(b2):
    os.remove(b2)
with open(b1 + 'simulation_configuration.csv', b3 = '') as config_file:
    b4 = csv.reader(config_file, delimiter=',', quotechar='|')
    b5 = open(b2, 'w')
    b5.write('
    b10, b11, b12, b13, b14, b15, b6 = [None] * 7
    b16, b17, b18, b19, b7 = [None] * 5
    for line in b4:
        b9, b8 = line[0], line[1].strip()
        if b9 = = 'SIMULATION START TIME':
            b10 = b8[:4]
        elif b9 = = 'TARIFF':
            b11 = b8.strip()
        elif b9 = = 'FIXED PRICE WINTER':
            b12 = b8
        elif b9 = = 'FIXED PRICE SUMMER':
            b13 = b8
        elif b9 = = 'TOU OFF-PEAK PRICE WINTER':
            b14 = float(b8)
        elif b9 = = 'TOU OFF-PEAK PRICE SUMMER':
            b15 = float(b8)
        elif b9 = = 'TOU MULTIPLIER':
            b6 = float(b8)
        elif b9 = = 'MODEL NAME':
            b16 = b8
        elif b9 = = 'TOU PEAK START HOUR WINTER':
            b17 = b8 if len(b8) == 2 else '0' + b8
        elif b9 = = 'TOU PEAK END HOUR WINTER':
            b18 = b8 if len(b8) == 2 else '0' + b8
        elif b9 = = 'TOU PEAK START HOUR SUMMER':
            b19 = b8 if len(b8) == 2 else '0' + b8
        elif b9 = = 'TOU PEAK END HOUR SUMMER':
            b7 = b8 if len(b8) == 2 else '0' + b8
    b5.close()
b20 = [date(int(b10) - 1, 12, 31), date(int(b10), 5, 1), date(int(b10), 11, 1)]
b21 = [date(int(b10), 4, 30), date(int(b10), 10, 31), date(int(b10), 12, 31)]
b22 = [edate - sdate for sdate, edate in zip(b20, b21)]
b23 = "input/tariff/"
if b11 = = 'fixed':
    b24 = b23 + "fixed.tariff"
    if os.path.exists(b24):
        os.remove(b24)
    with open(b24, 'w') as fw_fixed:
        for b25, (start_date, end_date) in enumerate(zip(b20, b21)):
            fw_fixed.write(f"{start_date} 00:00:00,{b12}\n")
            fw_fixed.write(f"{end_date} 00:00:00,{b13}\n")
            if b25 = = 1:
                fw_fixed.write(f"{start_date} {b19}:00:00,{b15 * b6}\n")
                fw_fixed.write(f"{start_date} {b7}:00:00,{b15}\n")
            else:
                fw_fixed.write(f"{start_date} {b17}:00:00,{b14 * b6}\n")
                fw_fixed.write(f"{start_date} {b18}:00:00,{b14}\n")
elif b11 in ['TOU', 'tou']:
    b26 = b23 + "tou.tariff"
    if os.path.exists(b26):
        os.remove(b26)
    with open(b26, 'w') as fw_tou:
        for b25, (start_date, end_date) in enumerate(zip(b20, b21)):
            for i in range((end_date - start_date).days + 1):
                b27 = start_date + timedelta(days=i)
                fw_tou.write(f"\n{b27} 00:00:00,{b14}\n")
                if b25 = = 1:
                    fw_tou.write(f"{b27} {b19}:00:00,{b15 * b6}\n")
                    fw_tou.write(f"{b27} {b7}:00:00,{b15}\n")
                else:
                    fw_tou.write(f"{b27} {b17}:00:00,{b14 * b6}\n")
                    fw_tou.write(f"{b27} {b18}:00:00,{b14}\n")
gridlabd.command(f"{b16}/{b16}.glm")
gridlabd.start('wait')