import random
class Cell:
    def __init__(self, position, cell_type, id=None):
        self.position = position
        self.cell_type = cell_type
        self.id = id
def generate(width, height):
    internal_width = width * 2 + 1
    internal_height = height * 2 + 1
    walls = gen_walls(internal_width, internal_height)
    blocks = gen_blocks(internal_width, internal_height)
    cells = gen_cells(internal_width, internal_height)
    new_walls = []
    while blocks:
        current_block = random.choice(blocks)
        cell1, cell2 = get_neighbors(current_block, cells)
        if cell1.id == cell2.id:
            new_walls.append(Cell(current_block.position, 0))
            blocks.remove(current_block)
        else:
            old_id = cell2.id
            new_id = cell1.id
            for cell in cells:
                if cell.id == old_id:
                    cell.id = new_id
            blocks.remove(current_block)
    raw_output = [cell.position for cell in walls]
    raw_output.extend([cell.position for cell in new_walls])
    output = [[0 for _ in range(internal_width)] for _ in range(internal_height)]
    for position in raw_output:
        output[position[1]][position[0]] = 1
    return output
def gen_walls(width, height):
    walls = []
    for x in range(width):
        for y in range(height):
            if x == 0 or y == 0 or x == width - 1 or y == height - 1 or (x % 2 == 0 and y % 2 == 0):
                walls.append(Cell((x, y), 0))
    return walls
def gen_blocks(width, height):
    blocks = []
    for x in range(width):
        for y in range(height):
            if 0 < x < width - 1 and 0 < y < height - 1 and ((x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1)):
                blocks.append(Cell((x, y), 1))
    return blocks
def gen_cells(width, height):
    cells = []
    current_num = 0
    for x in range(width):
        for y in range(height):
            if 0 < x < width - 1 and 0 < y < height - 1 and x % 2 == 1 and y % 2 == 1:
                cells.append(Cell((x, y), 2, current_num))
                current_num += 1
    return cells
def search_cells(x, y, cells):
    position = (x, y)
    for cell in cells:
        if cell.position == position:
            return cell
    return None
def get_neighbors(current_block, cells):
    neighbor_cells = [
        search_cells(current_block.position[0], current_block.position[1] + 1, cells),
        search_cells(current_block.position[0], current_block.position[1] - 1, cells),
        search_cells(current_block.position[0] + 1, current_block.position[1], cells),
        search_cells(current_block.position[0] - 1, current_block.position[1], cells)
    ]
    neighbor_cells = [n for n in neighbor_cells if n is not None]
    return neighbor_cells[0], neighbor_cells[1]
if __name__ == "__main__":
    print(generate(5, 6))