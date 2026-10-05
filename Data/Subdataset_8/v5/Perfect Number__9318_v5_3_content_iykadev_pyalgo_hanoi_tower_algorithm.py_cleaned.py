def move_disk(source, destination):
    print(f"Move disk from {source} to {destination}")
def hanoi_tower_algorithm(n, source, auxiliary, destination):
    if n == 1:
        move_disk(source, destination)
    else:
        hanoi_tower_algorithm(n - 1, source, destination, auxiliary)
        move_disk(source, destination)
        hanoi_tower_algorithm(n - 1, auxiliary, source, destination)
def hanoi_tower_algorithm_main(ndiscs):
    print(f"Solving Tower of Hanoi problem for {ndiscs} discs:")
    hanoi_tower_algorithm(ndiscs, "A", "B", "C")
hanoi_tower_algorithm_main(3)