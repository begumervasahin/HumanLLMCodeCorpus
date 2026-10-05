def fizzbuzz(a, b):
    '''
    Determines the result based on the lengths of two lists a and b:
    - If the combined length is divisible by both 3 and 5, returns 'fizzbuzz'.
    - If the combined length is divisible by 3 only, returns 'fizz'.
    - If the combined length is divisible by 5 only, returns 'buzz'.
    - Otherwise, returns the sum of the lengths of lists a and b.
    '''
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