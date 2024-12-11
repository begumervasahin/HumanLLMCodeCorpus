import argparse
import random
import time
from PIL import Image
from mazes import Maze
def fonk1(filename, size):
    b1 = time.time()
    print("Generating Maze and Saving...")
    if size % b2 = = 0:
        size += 1
    b3 = Maze(size)
    b4 = [(255, 255, 255) if cell.IN or not cell.Wall else (0, 0, 0) for cell in b3.cells]
    b5 = random.randrange(1, size, b2)
    b6 = random.randrange(1, size, b2)
    b4[b5] = (255, 255, 255)
    b4[len(b4) - 1 - b6] = (255, 255, 255)
    b7 = Image.new('RGB', (size, size), color='black')
    b7.putdata(b4)
    b7.save(filename)
    b8 = time.time()
    b9 = b8 - b1
    print("Maze generated and saved successfully.")
    print("Time taken:", b9)
def fonk2():
    b10 = argparse.ArgumentParser(description="Generate a b3 image.")
    b10.add_argument("filename", b11 = "Output filename for the b3 image")
    b10.add_argument("size", b12 = int, b11="Size of the b3 (an odd integer)")
    b13 = b10.parse_args()
    b14 = b13.size
    if b14 > 500:
        print("Error: Size must be less than or equal to 500.")
        return
    fonk1(b13.filename, b14)
if b15 = = "__main__":
    fonk2()