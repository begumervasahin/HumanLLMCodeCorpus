import random
class Cell:
    def __init__(self, position, cell_type, cell_id=None):
        self.position = position
        self.cell_type = cell_type
        self.cell_id = cell_id
def generate_maze(width, height):
    internal_width = width * 2 + 1
    internal_height = height * 2 + 1
    outer_walls = generate_outer_walls(internal_width, internal_height)
    blocks = generate_blocks(internal_width, internal_height)
    cells = generate_cells(internal_width, internal_height)
    new_walls = []
    while len(blocks) > 0:
        current_block = blocks[random.randint(0, len(blocks)-1)]
        cell1, cell2 = get_neighbor_cells(current_block, cells)
        if cell1.cell_id == cell2.cell_id:
            new_walls.append(Cell(current_block.position, 0))
            blocks.remove(current_block)
        else:
            old_id = cell2.cell_id
            new_id = cell1.cell_id
            for cell in cells:
                if cell.cell_id == old_id:
                    cell.cell_id = new_id
            blocks.remove(current_block)
    raw_output = []
    for cell in outer_walls:
        raw_output.append(cell.position)
    for cell in new_walls:
        raw_output.append(cell.position)
    output = [[0 for _ in range(internal_width)] for _ in range(internal_height)]
    for position in raw_output:
        output[position[1]][position[0]] = 1
    return output
def generate_outer_walls(width, height):
    output = []
    for x in range(width):
        for y in range(height):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                output.append(Cell((x, y), 0))
            elif x % 2 == 0 and y % 2 == 0:
                output.append(Cell((x, y), 0))
    return output
def generate_blocks(width, height):
    output = []
    for x in range(width):
        for y in range(height):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                pass
            elif x % 2 == 1 and y % 2 == 0:
                output.append(Cell((x, y), 1))
            elif x % 2 == 0 and y % 2 == 1:
                output.append(Cell((x, y), 1))
    return output
def generate_cells(width, height):
    output = []
    current_id = 0
    for x in range(width):
        for y in range(height):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                pass
            elif x % 2 == 1 and y % 2 == 1:
                output.append(Cell((x, y), 2, current_id))
                current_id += 1
    return output
def search_cell(x, y, cells):
    position = (x, y)
    for cell in cells:
        if cell.position == position:
            return cell
    return None
def get_neighbor_cells(current_block, cells):
    neighbor_cells = []
    neighbor_cells.append(search_cell(current_block.position[0], current_block.position[1] + 1, cells))
    neighbor_cells.append(search_cell(current_block.position[0], current_block.position[1] - 1, cells))
    neighbor_cells.append(search_cell(current_block.position[0] + 1, current_block.position[1], cells))
    neighbor_cells.append(search_cell(current_block.position[0] - 1, current_block.position[1], cells))
    neighbor_cells = [neighbor for neighbor in neighbor_cells if neighbor is not None]
    return neighbor_cells[0], neighbor_cells[1]
if __name__ == "__main__":
    print(generate_maze(5, 6))