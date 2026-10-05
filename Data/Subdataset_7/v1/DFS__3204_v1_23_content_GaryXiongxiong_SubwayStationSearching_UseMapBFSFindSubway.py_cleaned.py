from collections import deque
from Stations import stationMap, stationStringMap
def fonk1(station, b5):
    b1 = deque()
    b2 = {station.getName(): None}
    b1.append(station)
    while b1:
        b3 = b1.popleft()
        for sub_station in stationMap[b3]:
            if sub_station.getName() not in b2:
                if sub_station.getName() == b5.getName():
                    b2[sub_station.getName()] = b3.getName()
                    return b2, b5.getName()
                else:
                    b1.append(sub_station)
                    b2[sub_station.getName()] = b3.getName()
    print("No b7 found.")
    return False, b5
b4 = input("Enter the starting station: ")
b5 = input("Enter the destination station: ")
searched_out, b6 = fonk1(stationStringMap[b4], stationStringMap[b5])
print("-" * 10 + "Path Below" + "-" * 10)
b7 = [b6]
while searched_out[b6] is not None:
    b7.append(searched_out[b6])
    b6 = searched_out[b6]
b7.reverse()
print("Shortest b7:")
for station_name in b7:
    print(station_name, b8 = " ")
print("\n")