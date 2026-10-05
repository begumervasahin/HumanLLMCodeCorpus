import random
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
def count_comparisons(arr):
    global comparisons
    comparisons = 0
    def merge_sort_count(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)
        left = merge_sort_count(arr[:mid])
        right = merge_sort_count(arr[mid:])
        return merge_count(left, right)
    def merge_count(left, right):
        nonlocal comparisons
        merged = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    merge_sort_count(arr)
    return comparisons
def main():
    lines = [line.rstrip('\n') for line in open('words.txt')]
    sizes_to_test = [10, 30, 100, 300, 1000, 3000, 10000, len(lines)]
    for size in sizes_to_test:
        print('-------------')
        print(f'Testing on {size} words')
        words_to_test = lines[:size]
        sorted_words = merge_sort(words_to_test)
        comparisons = count_comparisons(words_to_test)
        print(f'{size} words sorted')
        print('Sorted words:', sorted_words)
        print('Number of comparisons:', comparisons)
        reversed_words = list(reversed(words_to_test))
        comparisons = count_comparisons(reversed_words)
        print(f'{size} words reversed')
        print('Sorted words:', reversed_words)
        print('Number of comparisons:', comparisons)
        random.shuffle(words_to_test)
        sorted_words = merge_sort(words_to_test)
        comparisons = count_comparisons(words_to_test)
        print(f'{size} words random')
        print('Sorted words:', sorted_words)
        print('Number of comparisons:', comparisons)
        print('-------------')
        print()
if __name__ == "__main__":
    main()