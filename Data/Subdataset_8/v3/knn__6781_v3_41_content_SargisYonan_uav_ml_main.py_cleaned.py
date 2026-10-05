import knn
import map_driver
import matplotlib.pyplot as plt
def main():
    num_uavs = 3
    map_driver.initialize_uavs(num_uavs)
    map_driver.place_interest_point(25, 25, 20)
    map_driver.place_interest_point(19, 25, 20)
    predicted_map = knn.predicted_map
    animation_file = 'predicted.mp4'
    map_driver.uav_flight(predicted_map, animation_file)
    map_driver.plot_map(predicted_map)
    plt.show()
if __name__ == "__main__":
    main()