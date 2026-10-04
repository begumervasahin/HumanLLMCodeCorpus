import random
import time
import os
import sys
def generate_random_number() -> int:
    return random.randint(1, 10)
def clear_screen() -> None:
    os.system("clear" if os.name == "posix" else "cls")
def main() -> None:
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