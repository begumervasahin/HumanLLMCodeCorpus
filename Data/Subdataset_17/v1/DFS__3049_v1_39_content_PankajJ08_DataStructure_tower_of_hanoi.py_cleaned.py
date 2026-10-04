
move_counter = 1
def tower_of_hanoi_sol(height, start, end, auxiliary):
    global move_counter
    if height >= 1:
        tower_of_hanoi_sol(height - 1, start, auxiliary, end)
        print(f"{move_counter}: Move from {start} to {end}")
        move_counter += 1
        tower_of_hanoi_sol(height - 1, auxiliary, end, start)
num_disks = 3
tower_of_hanoi_sol(num_disks, 1, 2, 3)