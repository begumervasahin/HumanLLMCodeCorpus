def fonk1(list_a, list_b):
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(list_a, list_b)]
def fonk2(d):
    return {value: key for key, value in d.items()}
def fonk3(start, length):
    return [start + i for i in range(length)]
