import argparse
import random
import time
from PIL import Image
from mazes import Maze
def generate_image_maze(filename, size):
    start_time = time.time()
    print("Computing Maze and Saving...")
    if size % 2 == 0:
        size += 1
    maze = Maze(size)
    data = []
    for cell in maze.cells:
        if cell.IN or not cell.Wall:
            data.append((255, 255, 255))
        else:
            data.append((0, 0, 0))
    start = random.randrange(1, size, 2)
    end = random.randrange(1, size, 2)
    data[start] = (255, 255, 255)
    data[len(data) - 1 - end] = (255, 255, 255)
    img = Image.new('RGB', (size, size), color='black')
    img.putdata(data)
    img.save(filename)
    end_time = time.time()
    total_time = end_time - start_time
    print("Time elapsed:", total_time)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("size")
    args = parser.parse_args()
    size = int(args.size)
    if size > 500:
        print("Maze size is too large. Please choose a smaller size.")
        exit()
    generate_image_maze(args.filename, size)
if __name__ == "__main__":
    main()