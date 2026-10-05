import random
import networkx as nx
from datetime import datetime
def extract_user_time(filenames):
    pass
def extract_user_devices_info(all_user_id, filenames):
    pass
def calculate_median_delta_t(all_time):
    pass
def generate_time_groups(all_time, delta_t):
    pass
def extract_device_behaviors_on_time_group(time_group, current_user_info):
    pass
def calculate_devices_weight(device1, device2, devices_info):
    pass
def draw_graph(median_delta_t, current_time, user_idx, user, graph):
    pass
def main():
    filenames = ['device_data.csv', 'cookie_data.csv']
    all_user_id, all_user_time_info = extract_user_time(filenames)
    all_user_info = extract_user_devices_info(all_user_id, filenames)
    all_time = ['201705040913', '201705040932', ...]
    median_delta_t = calculate_median_delta_t(all_time)
    print("Median Delta T:", median_delta_t)
    delta_t = 60 * 60
    time_group = generate_time_groups(all_time, delta_t)
    print("Time Group:", time_group)
    user = random.choice(list(all_user_info.keys()))
    current_user_info = all_user_info[user]
    grouped_devices_dict = extract_device_behaviors_on_time_group(time_group, current_user_info)
    print("Grouped Devices Dictionary for User", user, ":", grouped_devices_dict)
    device1 = random.choice(list(grouped_devices_dict.keys()))
    device2 = random.choice(list(grouped_devices_dict.keys()))
    weight = calculate_devices_weight(device1, device2, grouped_devices_dict)
    print("Weight between", device1, "and", device2, ":", weight)
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    user_idx = 0
    graph = nx.Graph()
    draw_graph(median_delta_t, current_time, user_idx, user, graph)
if __name__ == "__main__":
    main()