import numpy as np
import glob
import matplotlib.pyplot as plt
from collections import deque
THRESHOLD_LOW = 200
THRESHOLD_HIGH = 600
def bfs(variance, pos):
    MOVEMENT_X = [1, 0, -1, 0]
    MOVEMENT_Y = [0, 1, 0, -1]
    visited = set([(x, y) for x, y in pos])
    que = deque(pos)
    mask = np.zeros_like(variance, dtype=np.uint8)
    mask[variance < THRESHOLD_LOW] = 255
    while que:
        x, y = que.popleft()
        for dx, dy in zip(MOVEMENT_X, MOVEMENT_Y):
            nx, ny = x + dx, y + dy
            if variance[nx, ny] < THRESHOLD_HIGH and (nx, ny) not in visited:
                visited.add((nx, ny))
                mask[nx, ny] = 255
                que.append((nx, ny))
    return mask
def main():
    file_names = glob.glob("*.npy")
    for idx, name in enumerate(file_names):
        variance = np.load(name)
        positions = np.argwhere(variance < THRESHOLD_LOW).tolist()
        mask = bfs(variance, positions)
        plt.subplot(231 + idx)
        plt.imshow(mask, cmap="gray")
        plt.title(name)
    plt.show()
if __name__ == "__main__":
    main()