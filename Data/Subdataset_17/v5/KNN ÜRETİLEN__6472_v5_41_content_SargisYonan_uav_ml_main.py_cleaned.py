import map_driver
import knn
import matplotlib.pyplot as plt
def main():
    map_driver.initialize_uavs(3)
    map_driver.place_interest_point(25, 25, 20)
    map_driver.place_interest_point(19, 25, 20)
    map_driver.uav_flight(knn.predicted_map, output_filename='predicted.mp4')
    map_driver.plot_map(knn.predicted_map)
if __name__ == "__main__":
    main()