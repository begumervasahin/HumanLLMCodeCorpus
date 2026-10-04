import random
comparison_counter = 0
def merge_sort(lst):
    global comparison_counter
    if len(lst) <= 1:
        comparison_counter += 1
        return lst
    mid = len(lst)
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)
def merge(left, right):
    global comparison_counter
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            comparison_counter += 1
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    comparison_counter += 1
    merged += left[i:]
    merged += right[j:]
    return merged
def test_merge_sort_on_words(lines, num_words):
    global comparison_counter
    print(f'Testing on {num_words} words')
    print(f'{num_words} words sorted')
    words_sorted = lines[:num_words]
    merge_sort(words_sorted)
    print('Number of comparisons:', comparison_counter)
    print(f'{num_words} words reversed')
    comparison_counter = 0
    words_reversed = list(reversed(words_sorted))
    merge_sort(words_reversed)
    print('Number of comparisons:', comparison_counter)
    print(f'{num_words} words random')
    comparison_counter = 0
    random_start_index = random.randint(0, len(lines) - num_words)
    words_random = lines[random_start_index:random_start_index + num_words]
    random.shuffle(words_random)
    merge_sort(words_random)
    print('Number of comparisons:', comparison_counter)
    print('-------------')
def main():
    with open('words.txt') as file:
        lines = [line.strip() for line in file]
    print(f'Total words: {len(lines)}')
    test_cases = [10, 30, 100, 300, 1000, 3000, 10000, len(lines)]
    for num_words in test_cases:
        test_merge_sort_on_words(lines, num_words)
if __name__ == "__main__":
    main()