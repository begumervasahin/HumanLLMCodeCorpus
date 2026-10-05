import map_driver
import knn
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def fonk1():
    map_driver.initialize_uavs(3)
    map_driver.place_interest_point(25, 25, 20)
    map_driver.place_interest_point(19, 25, 20)
    map_driver.uav_flight(knn.predicted_map, 'predicted.mp4')
    map_driver.plot_map(knn.predicted_map)
if b1 = = "__main__":
    fonk1()