def tuple_list_sum(list_a, list_b):
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(list_a, list_b)]
def inverse_dictionary(d):
    return {value: key for key, value in d.items()}
def generate_sequence(start, length):
    return [start + i for i in range(length)]
