import argparse
import random
import time
from PIL import Image
from mazes import Maze
def generate_maze_image(filename, size):
    start_time = time.time()
    print("Generating Maze and Saving...")
    if size % 2 == 0:
        size += 1
    maze = Maze(size)
    image_data = [(255, 255, 255) if cell.IN or not cell.Wall else (0, 0, 0) for cell in maze.cells]
    start_point = random.randrange(1, size, 2)
    end_point = random.randrange(1, size, 2)
    image_data[start_point] = (255, 255, 255)
    image_data[len(image_data) - 1 - end_point] = (255, 255, 255)
    maze_image = Image.new('RGB', (size, size), color='black')
    maze_image.putdata(image_data)
    maze_image.save(filename)
    end_time = time.time()
    total_time = end_time - start_time
    print("Maze generated and saved successfully.")
    print("Time taken:", total_time)
def main():
    parser = argparse.ArgumentParser(description="Generate a maze image.")
    parser.add_argument("filename", help="Output filename for the maze image")
    parser.add_argument("size", type=int, help="Size of the maze (an odd integer)")
    args = parser.parse_args()
    maze_size = args.size
    if maze_size > 500:
        print("Error: Size must be less than or equal to 500.")
        return
    generate_maze_image(args.filename, maze_size)
if __name__ == "__main__":
    main()