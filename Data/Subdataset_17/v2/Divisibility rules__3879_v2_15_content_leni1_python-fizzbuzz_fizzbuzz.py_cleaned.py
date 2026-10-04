def fizzbuzz(a, b):
    if not isinstance(a, list) or not isinstance(b, list):
        return 'Invalid input'
    len_sum = len(a) + len(b)
    if len_sum % 3 == 0 and len_sum % 5 == 0:
        return 'fizzbuzz'
    elif len_sum % 3 == 0:
        return 'fizz'
    elif len_sum % 5 == 0:
        return 'buzz'
    else:
        return len_sum
if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [4, 5, 6, 7]
    result = fizzbuzz(list1, list2)
    print(result)
