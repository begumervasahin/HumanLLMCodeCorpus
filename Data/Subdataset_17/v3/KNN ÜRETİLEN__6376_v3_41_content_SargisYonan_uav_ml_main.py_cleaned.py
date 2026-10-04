import map_driver
import knn
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def initialize_simulation(uav_count, interest_points):
    map_driver.initialize_uavs(uav_count)
    for point in interest_points:
        map_driver.place_interest_point(*point)
def run_uav_simulation(predicted_map, output_file):
    map_driver.uav_flight(predicted_map, output_file)
def plot_predicted_map(predicted_map):
    map_driver.plot_map(predicted_map)
def main():
    uav_count = 3
    interest_points = [(25, 25, 20), (19, 25, 20)]
    initialize_simulation(uav_count, interest_points)
    run_uav_simulation(knn.predicted_map, 'predicted.mp4')
    plot_predicted_map(knn.predicted_map)
if __name__ == "__main__":
    main()