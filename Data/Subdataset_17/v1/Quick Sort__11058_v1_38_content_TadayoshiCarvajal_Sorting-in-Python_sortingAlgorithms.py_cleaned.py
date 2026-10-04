import hashlib
import os
from pathlib import Path
import time
import exifread
def get_date_taken(file_path):
    try:
        with open(str(file_path), 'rb') as fh:
            tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
            date_taken = tags.get("EXIF DateTimeOriginal")
            return date_taken
    except Exception as e:
        print(f"Error reading EXIF data from {file_path}: {e}")
        return None
def file_hash(file_path):
    hasher = hashlib.md5()
    with open(str(file_path), 'rb') as current_file:
        buf = current_file.read()
        hasher.update(buf)
    return hasher.hexdigest()
def move_file(source, destination, moved_count):
    print(f"{moved_count} From: {source} To: {destination}")
    if not destination.parent.exists():
        destination.parent.mkdir(parents=True)
    source.rename(destination)
def delete_file(file_path):
    print(f"Deleting file: {file_path}")
    os.unlink(str(file_path))
if __name__ == "__main__":
    source = Path(r"E:\Jewell Family Media\Photos")
    destination = Path(r"E:\Jewell Family Media")
    duplicates_folder = Path(r"E:\photo_duplicates")
    start_time = time.time()
    moved_file_count = 0
    duplicate_count = 0
    total_files = 0
    file_extensions = set()
    deleted_count = 0
    unhandled_count = 0
    video_count = 0
    image_extensions = ['.bmp', '.png', '.jpg', '.JPG', '.PNG', '.GIF', '.jpeg']
    video_extensions = ['.wmv', '.MOV', '.AVI', '.AAE', '.mov', '.mp4']
    ignore_extensions = ['.idx2', '.psd']
    delete_extensions = ['.ini', '.ithmb', '.db']
    for root, dirs, files in os.walk(str(source), topdown=True):
        root_path = Path(root)
        for name in files:
            total_files += 1
            file_path = root_path / name
            file_suffix = file_path.suffix
            file_extensions.add(file_suffix)
            if file_suffix in delete_extensions:
                deleted_count += 1
                delete_file(file_path)
            elif file_suffix in video_extensions:
                print(f"Skipping video file: {file_path}")
                video_count += 1
            elif file_suffix in image_extensions:
                date_taken = get_date_taken(file_path)
                if date_taken:
                    date_parts = str(date_taken).split(':')
                    date_folder = f"{date_parts[0]}-{date_parts[1]}"
                    new_location = destination / date_folder / file_path.name
                    if new_location.exists():
                        if file_hash(file_path) == file_hash(new_location):
                            print("Ignoring duplicate")
                            duplicate_count += 1
                            new_location = duplicates_folder / f"{time.time()}_{name}"
                            move_file(file_path, new_location, moved_file_count)
                        else:
                            new_location = new_location.parent / f"{time.time()}_{name}"
                            print(f"Fixed name {new_location}")
                            move_file(file_path, new_location, moved_file_count)
                            moved_file_count += 1
                    else:
                        move_file(file_path, new_location, moved_file_count)
                        moved_file_count += 1
                else:
                    print(f"Cannot process file: {file_path}")
                    unhandled_count += 1
            else:
                print(f"Unknown file type: {file_path}")
    print(f"Moved: {moved_file_count} files in {((time.time() - start_time)/60):.2f} minutes")
    print(f"Duplicate files: {duplicate_count}")
    print(f"File extensions encountered: {file_extensions}")
    print(f"Deleted files: {deleted_count}")
    print(f"Unhandled files: {unhandled_count}")
    print(f"Video files: {video_count}")
    print(f"Total files processed: {total_files}")
from matplotlib import pyplot as plt
from tqdm import tqdm
'''Utility Functions'''
def rand_list(n, low=0, high=100):
    from random import randint
    return [randint(1, n) for _ in range(n)]
def sort_time(f, A):
    from time import time
    from random import shuffle
    shuffle(A)
    start = time()
    f(A)
    stop = time()
    return stop - start
def avg_sort_time(f, A, trials=500):
    avg = 0
    for i in range(trials):
        avg += sort_time(f, A)
    return avg / trials
def is_sorted(A):
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            return False
    return True
'''Sorting Algorithms'''
def insertion_sort(A):
    for j in range(len(A)):
        key, i = A[j], j - 1
        while i > -1 and A[i] > key:
            A[i+1], i = A[i], i - 1
        A[i+1] = key
    return A
def bubble_sort(A):
    unsorted, j = True, len(A)
    while unsorted:
        unsorted = False
        for i in range(1, j):
            if A[i] < A[i-1]:
                A[i], A[i-1], unsorted = A[i-1], A[i], True
        j -= 1
    return A
def selection_sort(A):
    for k in range(len(A)):
        mnmm, i = float('infinity'), -1
        for j in range(k, len(A)):
            if A[j] < mnmm:
                mnmm, i = A[j], j
        A[k], A[i] = A[i], A[k]
    return A
def heap_sort(A):
    def sift_down(A, parent, upto):
        larger = 2 * parent + 1
        while larger < upto:
            if A[larger] < A[larger + 1]:
                larger += 1
            if A[larger] > A[parent]:
                A[larger], A[parent] = A[parent], A[larger]
                parent = larger
                larger = 2 * parent + 1
            else:
                break
    last_node = len(A) - 1
    last_parent = last_node
    [sift_down(A, i, last_node) for i in range(last_parent, -1, -1)]
    for i in range(last_node, 0, -1):
        if A[0] > A[i]:
            A[0], A[i] = A[i], A[0]
            sift_down(A, 0, i - 1)
    return A
def merge_sort(A):
    if len(A) > 1:
        mid = len(A)
        lh, rh = A[:mid], A[mid:]
        merge_sort(lh)
        merge_sort(rh)
        i, j, k = 0, 0, 0
        while i < len(lh) and j < len(rh):
            if lh[i] < rh[j]:
                A[k], i = lh[i], i + 1
            else:
                A[k], j = rh[j], j + 1
            k += 1
        while i < len(lh):
            A[k], i, k = lh[i], i + 1, k + 1
        while j < len(rh):
            A[k], j, k = rh[j], j + 1, k + 1
    return A
def quick_sort(A):
    def quick_sort_helper(A, first, last):
        if first < last:
            sp = partition(A, first, last)
            quick_sort_helper(A, first, sp-1)
            quick_sort_helper(A, sp+1, last)
    def partition(A, first, last):
        pv, lm, rm, done = A[first], first+1, last, False
        while not done:
            while lm <= rm and A[lm] <= pv:
                lm += 1
            while rm >= lm and A[rm] >= pv:
                rm -= 1
            if rm < lm:
                done = True
            else:
                A[lm], A[rm] = A[rm], A[lm]
        A[first], A[rm] = A[rm], A[first]
        return rm
    quick_sort_helper(A, 0, len(A)-1)
    return A
def radix_sort(A):
    mod, div = 10, 1
    while True:
        buckets = [list() for _ in range(10)]
        [buckets[(n % mod)
        mod, div = mod * 10, div * 10
        if len(buckets[0]) == len(A):
            return buckets[0]
        A = []
        [A.append(y) for x in buckets for y in x]
def tim_sort(A):
    return sorted(A)
if __name__ == '__main__':
    input_sizes = [i for i in range(100, 25000, 500)]
    sort_times = {
        'bubble_sort': [sort_time(bubble_sort, rand_list(i)) for i in tqdm(input_sizes[:10], 'bubble_sort')],
        'selection_sort': [sort_time(selection_sort, rand_list(i)) for i in tqdm(input_sizes[:10], 'selection_sort')],
        'insertion_sort': [sort_time(insertion_sort, rand_list(i)) for i in tqdm(input_sizes[:10], 'insertion_sort')],
        'merge_sort': [sort_time(merge_sort, rand_list(i)) for i in tqdm(input_sizes, 'merge_sort')],
        'heap_sort': [sort_time(heap_sort, rand_list(i)) for i in tqdm(input_sizes, 'heap_sort')],
        'quick_sort': [sort_time(quick_sort, rand_list(i)) for i in tqdm(input_sizes, 'quick_sort')],
        'radix_sort': [sort_time(radix_sort, rand_list(i)) for i in tqdm(input_sizes, 'radix_sort')]
    }
    n_squared = {'bubble_sort', 'selection_sort', 'insertion_sort'}
    for sort in sort_times:
        if sort in n_squared:
            plt.plot(input_sizes[:10], sort_times[sort], label=sort.replace('_', ' ').title())
        else:
            plt.plot(input_sizes, sort_times[sort], label=sort.replace('_', ' ').title())
    plt.legend(loc='lower right')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size')
    plt.show()