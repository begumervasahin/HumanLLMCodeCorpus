import argparse
import random
import time
from PIL import Image
from mazes import Maze
def fonk1(filename, b12):
    b1 = time.time()
    print("Computing Maze and Saving...")
    if b12 % b2 = = 0:
        b12 += 1
    b3 = Maze(b12)
    b4 = []
    for cell in b3.cells:
        if cell.IN or not cell.Wall:
            b4.append((255, 255, 255))
        else:
            b4.append((0, 0, 0))
    b5 = random.randrange(1, b12, b2)
    b6 = random.randrange(1, b12, b2)
    b4[b5] = (255, 255, 255)
    b4[len(b4) - 1 - b6] = (255, 255, 255)
    b7 = Image.new('RGB', (b12, b12), color='black')
    b7.putdata(b4)
    b7.save(filename)
    b8 = time.time()
    b9 = b8 - b1
    print("Time elapsed:", b9)
def fonk2():
    b10 = argparse.ArgumentParser()
    b10.add_argument("filename")
    b10.add_argument("b12")
    b11 = b10.parse_args()
    b12 = int(b11.b12)
    if b12 > 500:
        print("Maze b12 is too large. Please choose a smaller b12.")
        exit()
    fonk1(b11.filename, b12)
if b13 = = "__main__":
    fonk2()