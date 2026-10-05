import csv
import os
from datetime import date, timedelta
import gridlabd
path = "config/"
if os.path.exists(path + "config.glm"):
    os.remove(path + "config.glm")
with open(path + 'simulation_configuration.csv', newline='') as config_file:
    fc = csv.reader(config_file, delimiter=',', quotechar='|')
    fw = open(path + 'config.glm', 'w')
    fw.write('
    year = None
    tariff_type = None
    fixed_winter = None
    fixed_summer = None
    TOU_winter = None
    TOU_summer = None
    TOU_multiplier = None
    model_name = None
    tou_start_w = None
    tou_end_w = None
    tou_start_s = None
    tou_end_s = None
    for line in fc:
        if 'SIMULATION START TIME' in line[0]:
            year = line[1].strip(' ')[0:4]
        if 'TARIFF' == line[0]:
            tariff_type = str(line[1]).strip(' ')
        if 'FIXED PRICE WINTER' in line[0]:
            fixed_winter = line[1].strip(' ')
        if 'FIXED PRICE SUMMER' in line[0]:
            fixed_summer = line[1].strip(' ')
        if 'TOU OFF-PEAK PRICE WINTER' in line[0]:
            TOU_winter = float(line[1].strip(' '))
        if 'TOU OFF-PEAK PRICE SUMMER' in line[0]:
            TOU_summer = float(line[1].strip(' '))
        if 'TOU MULTIPLIER' in line[0]:
            TOU_multiplier = float(line[1].strip(' '))
        if 'MODEL NAME' in line[0]:
            model_name = line[1].strip(" ")
        if 'TOU PEAK START HOUR WINTER' in line[0]:
            tou_start_w = '0' + line[1].strip(" ") if len(line[1].strip(" ")) == 1 else line[1].strip(" ")
        if 'TOU PEAK END HOUR WINTER' in line[0]:
            tou_end_w = '0' + line[1].strip(" ") if len(line[1].strip(" ")) == 1 else line[1].strip(" ")
        if 'TOU PEAK START HOUR SUMMER' in line[0]:
            tou_start_s = '0' + line[1].strip(" ") if len(line[1].strip(" ")) == 1 else line[1].strip(" ")
        if 'TOU PEAK END HOUR SUMMER' in line[0]:
            tou_end_s = '0' + line[1].strip(" ") if len(line[1].strip(" ")) == 1 else line[1].strip(" ")
    fw.close()
sdate_w1 = date(int(year) - 1, 12, 31)
edate_w1 = date(int(year), 4, 30)
sdate_s1 = date(int(year), 5, 1)
edate_s1 = date(int(year), 10, 31)
sdate_w2 = date(int(year), 11, 1)
edate_w2 = date(int(year), 12, 31)
delta_list = [edate_w1 - sdate_w1, edate_s1 - sdate_s1, edate_w2 - sdate_w2]
s_list = [sdate_w1, sdate_s1, sdate_w2]
if tariff_type == 'fixed':
    if os.path.exists("input/tariff/fixed.tariff"):
        os.remove("input/tariff/fixed.tariff")
    fw_fixed = open("input/tariff/fixed.tariff", 'w')
    fw_fixed.write(year + '-01-01 00:00:00,' + fixed_winter)
    fw_fixed.write('\n' + year + '-05-01 00:00:00,' + fixed_summer)
    fw_fixed.write('\n' + year + '-11-01 00:00:00,' + fixed_winter)
    fw_fixed.close()
elif tariff_type == 'TOU' or tariff_type == 'tou':
    if os.path.exists("input/tariff/tou.tariff"):
        os.remove("input/tariff/tou.tariff")
    fw_tou = open("input/tariff/tou.tariff", 'w')
    for s, delta in enumerate(delta_list):
        for i in range(delta.days + 1):
            day = '\n' + str(s_list[s] + timedelta(days=i))
            if s == 1:
                fw_tou.write(day + ' 00:00:00,' + str(TOU_summer))
                fw_tou.write(day + ' ' + tou_start_s + ':00:00,' + str(TOU_summer * TOU_multiplier))
                fw_tou.write(day + ' ' + tou_end_s + ':00:00,' + str(TOU_summer))
            else:
                fw_tou.write(day + ' 00:00:00,' + str(TOU_winter))
                fw_tou.write(day + ' ' + tou_start_w + ':00:00,' + str(TOU_winter * TOU_multiplier))
                fw_tou.write(day + ' ' + tou_end_w + ':00:00,' + str(TOU_winter))
    fw_tou.close()
gridlabd.command(model_name + '/' + model_name + '.glm')
gridlabd.start('wait')