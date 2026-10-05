import numpy as np
def update_routers(routes):
    num_routers = routes.shape[1]
    temp = np.full((1, num_routers, num_routers, num_routers), fill_value=100)
    for i in range(num_routers):
        for j in range(num_routers):
            if i != j:
                if routes[-1, i, i, j] == 100:
                    temp[0, i, j, :] = 100
                else:
                    temp[0, i, j, :] = routes[-1, j, j, :]
            else:
                for t in range(num_routers):
                    if t == i:
                        temp[0, i, i, t] = 0
                    else:
                        temp[0, i, i, t] = 100
                        for u in range(num_routers):
                            current_route = routes[-1, i, i, u] + routes[-1, u, u, t]
                            if current_route < temp[0, i, i, t]:
                                temp[0, i, i, t] = current_route
    if not np.array_equal(routes[-1, :, :, :], temp[0, :, :, :]):
        routes = np.concatenate((routes, temp))
    return routes
def main():
    num_routers = int(input("Please enter the number of routers: "))
    routes = np.full((1, num_routers, num_routers, num_routers), fill_value=100, dtype=int)
    for i in range(num_routers):
        s = input("Fill row number %d of the matrix: " % (i + 1))
        routes[0, i] = np.fromstring(s, dtype=int, sep=' ')
    for j in range(num_routers):
        routes[0, j, j, :] = routes[0, j, :]
    while True:
        before_matrix_shape = routes.shape[0]
        routes = update_routers(routes)
        after_matrix_shape = routes.shape[0]
        if after_matrix_shape == before_matrix_shape:
            break
    iterations = routes.shape[0]
    while True:
        print("\nThere are %d iterations and %d routers.\n" % (iterations, num_routers))
        print("-------------------------------------------------------------")
        iteration_pointer = input("Routing finished successfully...\nPlease enter the iteration level you want to take a look at: ")
        router_pointer = input("Enter router number or enter 'a' for an overall view: ")
        if router_pointer == 'a':
            print(routes[int(iteration_pointer) - 1])
        else:
            print(routes[int(iteration_pointer) - 1, int(router_pointer) - 1])
        if input("Do you need more report? (Y/N)").lower() == 'n':
            break
if __name__ == "__main__":
    main()