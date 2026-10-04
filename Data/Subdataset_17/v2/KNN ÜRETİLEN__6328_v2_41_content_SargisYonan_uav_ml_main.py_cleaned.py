import map_driver
import knn
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
def main():
    map_driver.initialize_uavs(3)
    interest_points = [(25, 25, 20), (19, 25, 20)]
    for point in interest_points:
        map_driver.place_interest_point(*point)
    map_driver.uav_flight(knn.predicted_map, 'predicted.mp4')
    map_driver.plot_map(knn.predicted_map)
if __name__ == "__main__":
    main()