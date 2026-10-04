import time
from tqdm import tqdm
def simulate_work(total_iterations, delay):
    for _ in tqdm(range(total_iterations), desc="Processing", unit="iteration"):
        time.sleep(delay)
if __name__ == "__main__":
    total_iterations = 1000
    delay_per_iteration = 0.02
    simulate_work(total_iterations, delay_per_iteration)