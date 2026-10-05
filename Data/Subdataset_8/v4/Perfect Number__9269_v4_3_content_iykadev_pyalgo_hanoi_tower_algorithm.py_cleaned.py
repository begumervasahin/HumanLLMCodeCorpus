def hanoi_tower_algorithm(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk from {source} to {destination}")
    else:
        hanoi_tower_algorithm(n - 1, source, destination, auxiliary)
        hanoi_tower_algorithm(1, source, auxiliary, destination)
        hanoi_tower_algorithm(n - 1, auxiliary, source, destination)
def hanoi_tower_algorithm_main(ndiscs):
    print(f"Solving Tower of Hanoi problem for {ndiscs} discs:")
    hanoi_tower_algorithm(ndiscs, "A", "B", "C")
hanoi_tower_algorithm_main(3)
