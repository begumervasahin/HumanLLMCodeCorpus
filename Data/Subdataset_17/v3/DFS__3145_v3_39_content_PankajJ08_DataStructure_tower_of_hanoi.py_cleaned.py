
move_counter = 1
def tower_of_hanoi(height, start, end, auxiliary):
    global move_counter
    if height >= 1:
        tower_of_hanoi(height - 1, start, auxiliary, end)
        print(f"{move_counter}: Move from {start} to {end}")
        move_counter += 1
        tower_of_hanoi(height - 1, auxiliary, end, start)
def main():
    num_disks = 3
    tower_of_hanoi(num_disks, 'A', 'C', 'B')
if __name__ == "__main__":
    main()