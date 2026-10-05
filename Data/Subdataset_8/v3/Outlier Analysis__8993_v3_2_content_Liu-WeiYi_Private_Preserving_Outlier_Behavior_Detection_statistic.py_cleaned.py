import sys
import json
from Process_TianChi_Main import analysis_Time
from utils import *
def analyze_devices(all_user_info):
    devices = set()
    total_users = len(all_user_info)
    count = 0
    for user_info in all_user_info.values():
        count += 1
        percentage = (count / total_users) * 100
        sys.stdout.write(f'\r>> Processing Users............ {percentage:.2f} %')
        sys.stdout.flush()
        reach_time_info = user_info.get("Reach_Time", {})
        for time_info in reach_time_info.values():
            devices.update(time_info.keys())
    return devices
def analyze_time(user_time_info):
    total_time_groups = sum(len(analysis_Time(user, info)[1]) for user, info in user_time_info.items())
    return total_time_groups
def analyze_features(all_user_info):
    total_users = len(all_user_info)
    total_keywords = sum(len(info["Keyword"]) for user_info in all_user_info.values() for info in user_info.get("Reach_Time", {}).values())
    total_ips = sum(len(info["Device_IP"]) for user_info in all_user_info.values() for info in user_info.get("Reach_Time", {}).values())
    avg_keywords = total_keywords / total_users
    avg_ips = total_ips / total_users
    return avg_keywords, avg_ips
def main():
    users = []
    with open('all_user_id.txt', 'r+') as f:
        users = [line.strip() for line in f.readlines()]
    choice = sys.argv[1]
    if choice == '0':
        print('Analyzing devices group...')
        with open('all_user_info.json') as f:
            all_user_info = json.load(f)
        devices = analyze_devices(all_user_info)
        print('\nTotal number of devices:', len(devices))
    elif choice == '1':
        print('Analyzing time group...')
        with open('user_time_info.json') as f:
            user_time_info = json.load(f)
        total_time_groups = analyze_time(user_time_info)
        print('\nTotal time groups:', total_time_groups)
    elif choice == '2':
        print('Analyzing features...')
        with open('all_user_info.json') as f:
            all_user_info = json.load(f)
        avg_keywords, avg_ips = analyze_features(all_user_info)
        print('\nAverage number of keywords:', avg_keywords)
        print('Average number of IP addresses:', avg_ips)
if __name__ == "__main__":
    main()