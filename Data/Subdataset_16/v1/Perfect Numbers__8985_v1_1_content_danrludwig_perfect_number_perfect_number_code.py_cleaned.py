import time
def fonk1(limit):
    b1 = []
    for number in range(1, limit):
        b2 = sum(divisor for divisor in range(1, number) if number % divisor == 0)
        if b2 = = number:
            b1.append(number)
    return b1
if b3 = = '__main__':
    b4 = time.time()
    b1 = fonk1(10000)
    for number in b1:
        print(number)
    print(f"Time taken: {time.time() - b4} seconds")
'''
Test:
    Only needs to do one test since there is no input.
    Output:
        6
        28
        496
        8128
'''