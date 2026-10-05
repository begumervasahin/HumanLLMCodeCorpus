import csv
import os
from datetime import date, timedelta
import gridlabd
b1 = "config/"
if os.b1.exists(b1 + "config.glm"):
    os.remove(b1 + "config.glm")
with open(b1 + 'simulation_configuration.csv', b2 = '') as config_file:
    b3 = csv.reader(config_file, delimiter=',', quotechar='|')
    b4 = open(b1 + 'config.glm', 'w')
    b4.write('
    b5 = None
    b6 = None
    b7 = None
    b8 = None
    b9 = None
    b10 = None
    b11 = None
    b12 = None
    b13 = None
    b14 = None
    b15 = None
    b16 = None
    for line in b3:
        if 'SIMULATION START TIME' in line[0]:
            b5 = line[1].strip(' ')[0:4]
        if 'TARIFF' == line[0]:
            b6 = str(line[1]).strip(' ')
        if 'FIXED PRICE WINTER' in line[0]:
            b7 = line[1].strip(' ')
        if 'FIXED PRICE SUMMER' in line[0]:
            b8 = line[1].strip(' ')
        if 'TOU OFF-PEAK PRICE WINTER' in line[0]:
            b9 = float(line[1].strip(' '))
        if 'TOU OFF-PEAK PRICE SUMMER' in line[0]:
            b10 = float(line[1].strip(' '))
        if 'TOU MULTIPLIER' in line[0]:
            b11 = float(line[1].strip(' '))
        if 'MODEL NAME' in line[0]:
            b12 = line[1].strip(" ")
        if 'TOU PEAK START HOUR WINTER' in line[0]:
            b13 = '0' + line[1].strip(" ") if len(line[1].strip(" ")) == 1 else line[1].strip(" ")
        if 'TOU PEAK END HOUR WINTER' in line[0]:
            b14 = '0' + line[1].strip(" ") if len(line[1].strip(" ")) == 1 else line[1].strip(" ")
        if 'TOU PEAK START HOUR SUMMER' in line[0]:
            b15 = '0' + line[1].strip(" ") if len(line[1].strip(" ")) == 1 else line[1].strip(" ")
        if 'TOU PEAK END HOUR SUMMER' in line[0]:
            b16 = '0' + line[1].strip(" ") if len(line[1].strip(" ")) == 1 else line[1].strip(" ")
    b4.close()
b17 = date(int(b5) - 1, 12, 31)
b18 = date(int(b5), 4, 30)
b19 = date(int(b5), 5, 1)
b20 = date(int(b5), 10, 31)
b21 = date(int(b5), 11, 1)
b22 = date(int(b5), 12, 31)
b23 = [b18 - b17, b20 - b19, b22 - b21]
b24 = [b17, b19, b21]
if b6 = = 'fixed':
    if os.b1.exists("input/tariff/fixed.tariff"):
        os.remove("input/tariff/fixed.tariff")
    b25 = open("input/tariff/fixed.tariff", 'w')
    b25.write(b5 + '-01-01 00:00:00,' + b7)
    b25.write('\n' + b5 + '-05-01 00:00:00,' + b8)
    b25.write('\n' + b5 + '-11-01 00:00:00,' + b7)
    b25.close()
elif b6 = = 'TOU' or b6 == 'tou':
    if os.b1.exists("input/tariff/tou.tariff"):
        os.remove("input/tariff/tou.tariff")
    b26 = open("input/tariff/tou.tariff", 'w')
    for b28, delta in enumerate(b23):
        for i in range(delta.days + 1):
            b27 = '\n' + str(b24[b28] + timedelta(days=i))
            if b28 = = 1:
                b26.write(b27 + ' 00:00:00,' + str(b10))
                b26.write(b27 + ' ' + b15 + ':00:00,' + str(b10 * b11))
                b26.write(b27 + ' ' + b16 + ':00:00,' + str(b10))
            else:
                b26.write(b27 + ' 00:00:00,' + str(b9))
                b26.write(b27 + ' ' + b13 + ':00:00,' + str(b9 * b11))
                b26.write(b27 + ' ' + b14 + ':00:00,' + str(b9))
    b26.close()
gridlabd.command(b12 + '/' + b12 + '.glm')
gridlabd.start('wait')