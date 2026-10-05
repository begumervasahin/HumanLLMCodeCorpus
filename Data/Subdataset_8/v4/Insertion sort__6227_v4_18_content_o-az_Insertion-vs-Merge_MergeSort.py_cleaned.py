import random
counter = 0
def merge_sort(lst):
    global counter
    if len(lst) <= 1:
        counter += 1
        return lst
    mid = len(lst)
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)
def merge(left, right):
    global counter
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            counter += 1
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    counter += 1
    merged += left[i:]
    merged += right[j:]
    return merged
def generate_words(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
def test_merge_sort(words, size):
    global counter
    counter = 0
    random_words = random.sample(words, size)
    sorted_words = merge_sort(random_words)
    print(f'Testing on {size} words:')
    print('Sorted words:', sorted_words)
    print('Number of comparisons:', counter)
    print()
def main():
    words = generate_words('words.txt')
    sizes_to_test = [10, 30, 100, 300, 1000, 3000, 10000, len(words)]
    for size in sizes_to_test:
        test_merge_sort(words, size)
if __name__ == "__main__":
    main()