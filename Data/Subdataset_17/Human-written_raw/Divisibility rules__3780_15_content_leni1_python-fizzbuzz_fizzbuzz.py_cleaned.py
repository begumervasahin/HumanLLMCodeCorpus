def fizzbuzz(a, b):
    if isinstance(a, list) and isinstance(b, list):
        len_sum = len(a) + len(b)
        if len_sum % 3 == 0 and len_sum % 5 == 0:
            return 'fizzbuzz'
        if len_sum % 3 == 0:
            return 'fizz'
        if len_sum % 5 == 0:
            return 'buzz'
        else:
            return len_sum
    else:
        return 'Invalid input'