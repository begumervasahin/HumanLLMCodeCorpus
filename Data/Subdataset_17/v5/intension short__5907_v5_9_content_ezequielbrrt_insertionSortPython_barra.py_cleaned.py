from time import sleep
from tqdm import tqdm
def process_items(item_count, delay):
    for _ in tqdm(range(item_count), desc="Processing items", unit="item"):
        sleep(delay)
if __name__ == "__main__":
    ITEM_COUNT = 1000
    DELAY_PER_ITEM = 0.02
    process_items(ITEM_COUNT, DELAY_PER_ITEM)