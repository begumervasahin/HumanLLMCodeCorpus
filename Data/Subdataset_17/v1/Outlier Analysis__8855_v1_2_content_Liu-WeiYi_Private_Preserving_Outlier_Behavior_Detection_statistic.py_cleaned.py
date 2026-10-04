import json
import sys
def load_users(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]
def process_devices_info(user_info_file):
    print('Processing devices group...')
    with open(user_info_file) as f:
        all_user_info = json.load(f)
    devices = set()
    count = 0
    total_users = len(all_user_info.keys())
    for user in all_user_info.keys():
        count += 1
        percentage = 100 * count / total_users
        sys.stdout.write('\r>> Processing Users............ %.2f %%' % percentage)
        sys.stdout.flush()
        info = all_user_info[user]["Reach_Time"]
        for time in info.keys():
            current_devices = info[time].keys()
            devices.update(current_devices)
    num_devices = len(devices)
    print(f'\nTotal number of devices: {num_devices}')
def process_timegroup_info(user_time_file):
    print('Processing time group...')
    with open(user_time_file) as f:
        user_time = json.load(f)
    all_time = 0
    count = 0
    total_users = len(user_time.keys())
    for user in user_time.keys():
        count += 1
        percentage = 100 * count / total_users
        sys.stdout.write('\r>> Processing Users............ %.2f %%' % percentage)
        sys.stdout.flush()
        per_user_info = user_time[user]
        _, Dates_Interval_Dict = analysis_Time(user, per_user_info)
        all_time += len(Dates_Interval_Dict.keys())
    print(f'\nTotal number of time intervals: {all_time}')
def process_features_info(user_info_file):
    print('Processing features...')
    with open(user_info_file) as f:
        all_user_info = json.load(f)
    all_keyword = 0
    all_IP = 0
    count = 0
    total_users = len(all_user_info.keys())
    for user in all_user_info.keys():
        count += 1
        percentage = 100 * count / total_users
        sys.stdout.write('\r>> Processing Users............ %.2f %%' % percentage)
        sys.stdout.flush()
        info = all_user_info[user]["Reach_Time"]
        for time in info.keys():
            for user in info[time].keys():
                all_keyword += len(info[time][user]["Keyword"])
                all_IP += len(info[time][user]["Device_IP"])
    avg_keyword = all_keyword / total_users
    avg_IP = all_IP / total_users
    print(f'\nTotal keywords: {all_keyword}')
    print(f'Average keywords per user: {avg_keyword}')
    print(f'Total IP addresses: {all_IP}')
    print(f'Average IP addresses per user: {avg_IP}')
def main():
    if len(sys.argv) < 2:
        print("Please provide an argument (0, 1, or 2).")
        return
    choice = sys.argv[1]
    if choice == '0':
        process_devices_info('all_user_info.json')
    elif choice == '1':
        process_timegroup_info('user_time_info.json')
    elif choice == '2':
        process_features_info('all_user_info.json')
    else:
        print("Invalid choice. Please provide 0, 1, or 2.")
if __name__ == "__main__":
    main()