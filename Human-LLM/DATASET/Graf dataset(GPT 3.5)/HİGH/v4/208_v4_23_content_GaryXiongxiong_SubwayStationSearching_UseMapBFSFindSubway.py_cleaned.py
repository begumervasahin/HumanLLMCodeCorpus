from collections import deque
from Stations import stationMap, stationStringMap
def fonk1(b7, b8):
    b1 = deque()
    b2 = {b7.getName(): None}
    b1.append(b7)
    while b1:
        b3 = b1.popleft()
        for next_station in stationMap[b3]:
            if next_station.getName() not in b2:
                b2[next_station.getName()] = b3.getName()
                if next_station.getName() == b8.getName():
                    return b2, b8.getName()
                else:
                    b1.append(next_station)
    print("No b10 found.")
    return False, b8
if b4 = = "__main__":
    b5 = input("Enter the starting station: ")
    b6 = input("Enter the destination station: ")
    b7 = stationStringMap[b5]
    b8 = stationStringMap[b6]
    searched_output, b9 = fonk1(b7, b8)
    print("-" * 10 + "Shortest Path" + "-" * 10)
    b10 = [b9]
    while searched_output[b9] is not None:
        b10.append(searched_output[b9])
        b9 = searched_output[b9]
    b10.reverse()
    print("Shortest b10:")
    for station_name in b10:
        print(station_name, b11 = " ")
    print("\n")