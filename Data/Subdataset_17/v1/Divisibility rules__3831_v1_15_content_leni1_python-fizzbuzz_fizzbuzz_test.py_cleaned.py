def fizzbuzz(a, b):
    if not isinstance(a, list) or not isinstance(b, list):
        return 'Invalid input'
    total_length = len(a) + len(b)
    if total_length % 3 == 0 and total_length % 5 == 0:
        return 'fizzbuzz'
    elif total_length % 3 == 0:
        return 'fizz'
    elif total_length % 5 == 0:
        return 'buzz'
    else:
        return total_length
if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [4, 5, 6, 7]
    result = fizzbuzz(list1, list2)
    print(result)
