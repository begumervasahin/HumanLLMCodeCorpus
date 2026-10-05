import argparse
from PIL import Image, ImageDraw
from mazes import Maze
import time
import random
def imageMaze(filename, size):
	t0 = time.time()
	print("Computing Maze and Saving...")
	if size%2 == 0:
		size += 1
	mz = Maze(size)
	data = []
	for c in mz.cells:
		if c.IN or not c.Wall:
			data.append((255, 255, 255))
		else:
			data.append(0)
	start = random.randrange(1, size, 2)
	end = random.randrange(1, size, 2)
	data[start] = (255, 255, 255)
	data[len(data) - 1 - end] = (255, 255, 255)
	img = Image.new('RGB', (size, size), color = 'black')
	img.putdata(data)
	img.save(filename)
	t1 = time.time()
	total = t1-t0
	print("Time elapsed:", total)
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename")
	parser.add_argument("size")
	args = parser.parse_args()
	size = int(args.size)
	if size > 500:
		print("Please no")
		exit()
	imageMaze(args.filename, size)
if __name__ == "__main__":
	main()