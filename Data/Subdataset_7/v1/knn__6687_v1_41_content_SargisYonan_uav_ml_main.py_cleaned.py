import knn
import map_driver
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def fonk1():
    map_driver.initialize_uavs(3)
    map_driver.place_interest_point(25, 25, 20)
    map_driver.place_interest_point(19, 25, 20)
    b1 = knn.b1
    map_driver.uav_flight(b1, 'predicted.mp4')
    map_driver.plot_map(b1)
    plt.show()
if b2 = = "__main__":
    fonk1()