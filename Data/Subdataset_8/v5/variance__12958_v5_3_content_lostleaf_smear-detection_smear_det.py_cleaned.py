import numpy as np
import glob
import matplotlib.pyplot as plt
from collections import deque
LOW_THRESHOLD = 200
HIGH_THRESHOLD = 600
def bfs(variance_map, initial_positions):
    DIRECTIONS_X = [1, 0, -1, 0]
    DIRECTIONS_Y = [0, 1, 0, -1]
    visited = set(initial_positions)
    queue = deque(initial_positions)
    mask = np.zeros_like(variance_map, dtype=np.uint8)
    mask[variance_map < LOW_THRESHOLD] = 255
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(DIRECTIONS_X, DIRECTIONS_Y):
            nx, ny = x + dx, y + dy
            if (0 <= nx < variance_map.shape[0] and 0 <= ny < variance_map.shape[1] and
                    variance_map[nx, ny] < HIGH_THRESHOLD and (nx, ny) not in visited):
                visited.add((nx, ny))
                mask[nx, ny] = 255
                queue.append((nx, ny))
    return mask
def main():
    variance_files = glob.glob("*.npy")
    for idx, filename in enumerate(variance_files):
        variance_map = np.load(filename)
        initial_positions = np.argwhere(variance_map < LOW_THRESHOLD).tolist()
        mask = bfs(variance_map, initial_positions)
        plt.subplot(231 + idx)
        plt.imshow(mask, cmap="gray")
        plt.title(filename)
    plt.show()
if __name__ == "__main__":
    main()