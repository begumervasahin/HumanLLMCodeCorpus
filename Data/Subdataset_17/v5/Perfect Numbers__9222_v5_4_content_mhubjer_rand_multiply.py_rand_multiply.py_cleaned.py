import random
import time
import os
import sys
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def generate_random_number():
    return random.randint(1, 10)
def main():
    rand1 = generate_random_number()
    rand2 = generate_random_number()
    print(f"THE FIRST NUMBER IS {rand1}.")
    time.sleep(3)
    print(f"THE SECOND NUMBER IS {rand2}.")
    time.sleep(3)
    product = rand1 * rand2
    print(f"{rand1} X {rand2} = {product}")
    time.sleep(3)
    clear_screen()
    sys.exit()
if __name__ == "__main__":
    main()