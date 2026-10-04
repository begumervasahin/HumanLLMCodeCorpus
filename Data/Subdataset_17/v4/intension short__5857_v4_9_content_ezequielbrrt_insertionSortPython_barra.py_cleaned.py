from time import sleep
from tqdm import tqdm
for _ in tqdm(range(1000), desc="Processing items", unit="item"):
    sleep(0.02)