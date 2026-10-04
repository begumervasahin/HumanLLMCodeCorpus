import random
comparison_count = 0
def merge_sort(lst):
    global comparison_count
    if len(lst) <= 1:
        return lst
    mid = len(lst)
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    global comparison_count
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        comparison_count += 1
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
def load_words(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
def test_sorting(words, description):
    global comparison_count
    print(f'Testing on {description}')
    comparison_count = 0
    print(f'{description} sorted')
    merge_sort(words.copy())
    print('Number of comparisons:', comparison_count)
    comparison_count = 0
    print(f'{description} reversed')
    merge_sort(list(reversed(words)))
    print('Number of comparisons:', comparison_count)
    comparison_count = 0
    print(f'{description} random')
    random.shuffle(words)
    merge_sort(words.copy())
    print('Number of comparisons:', comparison_count)
    print('-------------\n')
def main():
    words = load_words('words.txt')
    total_words = len(words)
    print(f'Total words: {total_words}\n')
    test_cases = [
        (words[0:10], "10 words"),
        (words[0:30], "30 words"),
        (words[0:100], "100 words"),
        (words[0:300], "300 words"),
        (words[0:1000], "1000 words"),
        (words[0:3000], "3000 words"),
        (words[0:10000], "10000 words"),
        (words, "all words"),
    ]
    for case, description in test_cases:
        test_sorting(case, description)
if __name__ == "__main__":
    main()