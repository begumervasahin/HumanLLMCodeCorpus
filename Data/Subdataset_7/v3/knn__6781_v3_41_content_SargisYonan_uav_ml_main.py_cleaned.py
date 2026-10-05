import knn
import map_driver
import matplotlib.pyplot as plt
def fonk1():
    a1 = 3
    map_driver.initialize_uavs(a1)
    map_driver.place_interest_point(25, 25, 20)
    map_driver.place_interest_point(19, 25, 20)
    b1 = knn.b1
    b2 = 'predicted.mp4'
    map_driver.uav_flight(b1, b2)
    map_driver.plot_map(b1)
    plt.show()
if b3 = = "__main__":
    fonk1()