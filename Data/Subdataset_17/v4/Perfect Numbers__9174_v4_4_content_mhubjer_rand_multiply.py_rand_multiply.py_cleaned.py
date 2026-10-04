import random
import time
import os
import sys
def main():
    rand1 = random.randint(1, 10)
    rand2 = random.randint(1, 10)
    print(f"THE FIRST NUMBER IS {rand1}.")
    time.sleep(3)
    print(f"THE SECOND NUMBER IS {rand2}.")
    time.sleep(3)
    sol1 = rand1 * rand2
    print(f"{rand1} X {rand2} = {sol1}")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit()
if __name__ == "__main__":
    main()