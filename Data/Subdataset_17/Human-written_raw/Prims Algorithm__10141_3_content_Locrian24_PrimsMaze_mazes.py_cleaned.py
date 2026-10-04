import random
class Maze:
	class Cell:
		def __init__(self, x, y):
			self.X = x
			self.Y = y
			self.Wall = True
			self.IN = False
		def get_neighbours(self, size):
			n = []
			x = self.X
			y = self.Y
			if x > 0:
				n.append([x - 1, y])
			else:
				n.append(None)
			if x + 1 < size:
				n.append([x + 1, y])
			else:
				n.append(None)
			if y > 0:
				n.append([x, y - 1])
			else:
				n.append(None)
			if y + 1 < size:
				n.append([x, y + 1])
			else:
				n.append(None)
			return n
		def get_walls(self, size, cells):
			w = []
			for n in self.get_neighbours(size):
				if n is None:
					continue
				cell = cells[n[0] + n[1] * size]
				if cell.Wall:
					w.append(cell)
			return w
		def opposite_is_valid(self, cells, size):
			cx, cy = -1, -1
			for n in self.get_neighbours(size):
				if n is None:
					continue
				cell = cells[n[0] + n[1] * size]
				if cell.IN:
					cx = n[0]
					cy = n[1]
					break
			if cx == -1:
				print("No valid neighbours. SOMETHING IS WRONG?")
				return None
			nx = 2*self.X - cx
			ny = 2*self.Y - cy
			if nx < 0 or ny < 0 or nx >= size or ny >= size:
				return None
			other = cells[nx + ny * size]
			if not other.IN:
				return other
			else:
				return None
	def __init__(self, size):
		self.cells = []
		for i in range(0, size):
			for j in range(0, size):
				self.cells.append(Maze.Cell(j, i))
		x = random.randrange(1, size, 2)
		y = random.randrange(1, size, 2)
		start = self.cells[x + y * size]
		wlist = start.get_walls(size, self.cells)
		start.IN = True
		start.Wall = False
		cell = None
		while len(wlist) != 0:
			curr_w = wlist[random.randint(0, len(wlist)-1)]
			cell = curr_w.opposite_is_valid(self.cells, size)
			if cell:
				curr_w.Wall = False
				cell.IN = True
				wlist.extend(cell.get_walls(size, self.cells))
				wlist = list(set(wlist))
			wlist.remove(curr_w)