import time
from tqdm import tqdm
total_iterations = 1000
for _ in tqdm(range(total_iterations), desc="Processing", unit="iteration"):
    time.sleep(0.02)