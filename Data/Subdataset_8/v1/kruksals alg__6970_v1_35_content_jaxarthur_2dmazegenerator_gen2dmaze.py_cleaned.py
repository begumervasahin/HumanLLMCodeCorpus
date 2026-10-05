import math
import random
class Cell:
    def __init__(self, position, typ, id=None):
        self.position = position
        self.typ = typ
        self.id = id
def generate(width, height):
    internalwidth = width * 2 + 1
    internalheight = height * 2 + 1
    walls = gen_walls(internalwidth, internalheight)
    blocks = gen_blocks(internalwidth, internalheight)
    cells = gen_cells(internalwidth, internalheight)
    new_walls = []
    while len(blocks) > 0:
        current_block = blocks[random.randint(0, len(blocks)-1)]
        cell1, cell2 = get_neighbors(current_block, cells)
        if cell1.id == cell2.id:
            new_walls.append(Cell(current_block.position, 0))
            blocks.remove(current_block)
        else:
            old_id = cell2.id
            new_id = cell1.id
            for cel in cells:
                if cel.id == old_id:
                    cel.id = new_id
            blocks.remove(current_block)
    raw_output = []
    for cel in walls:
        raw_output.append(cel.position)
    for cel in new_walls:
        raw_output.append(cel.position)
    output = [[0 for _ in range(internalwidth)] for _ in range(internalheight)]
    for position in raw_output:
        output[position[1]][position[0]] = 1
    return output
def gen_walls(width, height):
    output = []
    for x in range(width):
        for y in range(height):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                output.append(Cell((x, y), 0))
            elif x % 2 == 0 and y % 2 == 0:
                output.append(Cell((x, y), 0))
    return output
def gen_blocks(width, height):
    output = []
    for x in range(width):
        for y in range(height):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                pass
            elif x % 2 == 1 and y % 2 == 0:
                output.append(Cell((x, y), 1))
            elif x % 2 == 0 and y % 2 == 1:
                output.append(Cell((x,y), 1))
    return output
def gen_cells(width, height):
    output = []
    current_num = 0
    for x in range(width):
        for y in range(height):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                pass
            elif x % 2 == 1 and y % 2 == 1:
                output.append(Cell((x, y), 2, current_num))
                current_num += 1
    return output
def search_cells(x, y, cells):
    position = (x, y)
    for cel in cells:
        if cel.position == position:
            return cel
    return None
def get_neighbors(current_block, cells):
    neighbor_cells = []
    neighbor_cells.append(search_cells(current_block.position[0], current_block.position[1] + 1, cells))
    neighbor_cells.append(search_cells(current_block.position[0], current_block.position[1] - 1, cells))
    neighbor_cells.append(search_cells(current_block.position[0] + 1, current_block.position[1], cells))
    neighbor_cells.append(search_cells(current_block.position[0] - 1, current_block.position[1], cells))
    neighbor_cells = [neighbor for neighbor in neighbor_cells if neighbor is not None]
    return neighbor_cells[0], neighbor_cells[1]
if __name__ == "__main__":
    print(generate(5, 6))