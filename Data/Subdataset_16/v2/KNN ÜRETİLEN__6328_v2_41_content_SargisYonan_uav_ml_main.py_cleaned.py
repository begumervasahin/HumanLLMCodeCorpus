import map_driver
import knn
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
def fonk1():
    map_driver.initialize_uavs(3)
    b1 = [(25, 25, 20), (19, 25, 20)]
    for point in b1:
        map_driver.place_interest_point(*point)
    map_driver.uav_flight(knn.predicted_map, 'predicted.mp4')
    map_driver.plot_map(knn.predicted_map)
if b2 = = "__main__":
    fonk1()