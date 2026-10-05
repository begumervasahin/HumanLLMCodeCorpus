from collections import deque
from Stations import stationMap, stationStringMap
def search(station, dst):
    search_queue = deque()
    searched = {station.getName(): None}
    search_queue.append(station)
    while search_queue:
        cur_station = search_queue.popleft()
        for sub_station in stationMap[cur_station]:
            if sub_station.getName() not in searched:
                if sub_station.getName() == dst.getName():
                    searched[sub_station.getName()] = cur_station.getName()
                    return searched, dst.getName()
                else:
                    search_queue.append(sub_station)
                    searched[sub_station.getName()] = cur_station.getName()
    print("No path found.")
    return False, dst
start = input("Enter the starting station: ")
dst = input("Enter the destination station: ")
searched_out, dst_out = search(stationStringMap[start], stationStringMap[dst])
print("-" * 10 + "Path Below" + "-" * 10)
path = [dst_out]
while searched_out[dst_out] is not None:
    path.append(searched_out[dst_out])
    dst_out = searched_out[dst_out]
path.reverse()
print("Shortest path:")
for station_name in path:
    print(station_name, end=" ")
print("\n")