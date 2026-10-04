import json
import sys
from Process_TianChi_Main import analysis_Time
from utils import *
def load_users(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]
def process_devices(all_user_info):
    devices = set()
    total_users = len(all_user_info)
    for count, user in enumerate(all_user_info.keys(), start=1):
        percentage = 100 * count / total_users
        sys.stdout.write(f'\r>> Processing Users............ {percentage:.2f} %')
        sys.stdout.flush()
        info = all_user_info[user]["Reach_Time"]
        for time in info.keys():
            devices.update(info[time].keys())
    return len(devices)
def process_timegroup(user_time):
    all_time = 0
    total_users = len(user_time)
    for count, user in enumerate(user_time.keys(), start=1):
        percentage = 100 * count / total_users
        sys.stdout.write(f'\r>> Processing Users............ {percentage:.2f} %')
        sys.stdout.flush()
        per_user_info = user_time[user]
        _, dates_interval_dict = analysis_Time(user, per_user_info)
        all_time += len(dates_interval_dict.keys())
    return all_time
def process_features(all_user_info):
    total_keywords = 0
    total_ips = 0
    total_users = len(all_user_info)
    for count, user in enumerate(all_user_info.keys(), start=1):
        percentage = 100 * count / total_users
        sys.stdout.write(f'\r>> Processing Users............ {percentage:.2f} %')
        sys.stdout.flush()
        info = all_user_info[user]["Reach_Time"]
        for time in info.keys():
            for user_info in info[time].values():
                total_keywords += len(user_info["Keyword"])
                total_ips += len(user_info["Device_IP"])
    avg_keywords = total_keywords / total_users
    avg_ips = total_ips / total_users
    return total_keywords, avg_keywords, total_ips, avg_ips
def main():
    users = load_users('all_user_id.txt')
    if len(sys.argv) < 2:
        print("Please provide a valid option (0, 1, or 2).")
        return
    option = sys.argv[1]
    if option == '0':
        print('devices group...')
        with open('all_user_info.json') as f:
            all_user_info = json.load(f)
        num_devices = process_devices(all_user_info)
        print(f'\nNumber of unique devices: {num_devices}')
    elif option == '1':
        print('time group...')
        with open('user_time_info.json') as f:
            user_time = json.load(f)
        total_time_intervals = process_timegroup(user_time)
        print(f'\nTotal time intervals: {total_time_intervals}')
    elif option == '2':
        print('features...')
        with open('all_user_info.json') as f:
            all_user_info = json.load(f)
        total_keywords, avg_keywords, total_ips, avg_ips = process_features(all_user_info)
        print(f'\nTotal keywords: {total_keywords}')
        print(f'Average keywords per user: {avg_keywords:.2f}')
        print(f'Total IPs: {total_ips}')
        print(f'Average IPs per user: {avg_ips:.2f}')
    else:
        print("Invalid option. Please choose 0, 1, or 2.")
if __name__ == "__main__":
    main()