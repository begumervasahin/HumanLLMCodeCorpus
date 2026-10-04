import random
import time
import os
import sys
def fonk1() -> int:
    return random.randint(1, 10)
def fonk2() -> None:
    os.system("clear" if os.b1 = = "posix" else "cls")
def fonk3() -> None:
    b2 = fonk1()
    b3 = fonk1()
    print(f"THE FIRST NUMBER IS {b2}.")
    time.sleep(3)
    print(f"THE SECOND NUMBER IS {b3}.")
    time.sleep(3)
    b4 = b2 * b3
    print(f"{b2} X {b3} = {b4}")
    time.sleep(3)
    fonk2()
    sys.exit()
if b5 = = "__main__":
    fonk3()