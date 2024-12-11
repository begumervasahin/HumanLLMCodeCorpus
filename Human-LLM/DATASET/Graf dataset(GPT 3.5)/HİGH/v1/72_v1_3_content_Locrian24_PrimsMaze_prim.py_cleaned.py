import argparse
from PIL import Image, ImageDraw
from mazes import Maze
import time
import random
def fonk1(filename, b14):
    b1 = time.time()
    print("Computing Maze and Saving...")
    if b14 % b2 = = 0:
        b14 += 1
    b3 = Maze(b14)
    b4 = []
    for c in b3.cells:
        if c.IN or not c.Wall:
            b4.append((255, 255, 255))
        else:
            b4.append((0, 0, 0))
    b5 = random.randrange(1, b14, b2)
    b6 = random.randrange(1, b14, b2)
    b4[b5] = (255, 255, 255)
    b4[len(b4) - 1 - b6] = (255, 255, 255)
    b7 = Image.new('RGB', (b14, b14), color='black')
    b7.putdata(b4)
    b7.save(filename)
    b8 = time.time()
    b9 = b8 - b1
    print("Time elapsed:", b9)
def fonk2():
    b10 = argparse.ArgumentParser()
    b10.add_argument("filename", b11 = "Output filename for the maze image")
    b10.add_argument("b14", b12 = int, b11="Size of the maze (an odd integer)")
    b13 = b10.parse_args()
    b14 = b13.b14
    if b14 > 500:
        print("Please choose a b14 less than or equal to 500.")
        exit()
    fonk1(b13.filename, b14)
if b15 = = "__main__":
    fonk2()