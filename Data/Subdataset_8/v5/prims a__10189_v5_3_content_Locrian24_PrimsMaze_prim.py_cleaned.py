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
    maze_data = [(255, 255, 255) if cell.IN or not cell.Wall else (0, 0, 0) for cell in maze.cells]
    start_point = random.randrange(1, size, 2)
    end_point = random.randrange(1, size, 2)
    maze_data[start_point] = (255, 255, 255)
    maze_data[len(maze_data) - 1 - end_point] = (255, 255, 255)
    maze_image = Image.new('RGB', (size, size), color='black')
    maze_image.putdata(maze_data)
    maze_image.save(filename)
    end_time = time.time()
    total_time = end_time - start_time
    print("Time elapsed:", total_time)
def main():
    parser = argparse.ArgumentParser(description="Generate and save a maze image.")
    parser.add_argument("filename", help="Output filename for the maze image.")
    parser.add_argument("size", type=int, help="Size of the maze image.")
    args = parser.parse_args()
    if args.size > 500:
        print("Maze size is too large. Please choose a smaller size.")
        exit()
    generate_image_maze(args.filename, args.size)
if __name__ == "__main__":
    main()