import map_driver
import knn
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def fonk1(a1, b1):
    map_driver.initialize_uavs(a1)
    for point in b1:
        map_driver.place_interest_point(*point)
def fonk2(predicted_map, output_file):
    map_driver.uav_flight(predicted_map, output_file)
def fonk3(predicted_map):
    map_driver.plot_map(predicted_map)
def fonk4():
    a1 = 3
    b1 = [(25, 25, 20), (19, 25, 20)]
    fonk1(a1, b1)
    fonk2(knn.predicted_map, 'predicted.mp4')
    fonk3(knn.predicted_map)
if b2 = = "__main__":
    fonk4()