def fonk1(array, b1 = 0, desc=0):
    def fonk2(low, high):
        b2 = array[low]
        left, b3 = low + 1, high
        while True:
            while left <= b3 and array[left] <= b2:
                left += 1
            while left <= b3 and array[b3] > b2:
                b3 -= 1
            if left <= b3:
                array[left], array[b3] = array[b3], array[left]
                if b1 = = 2:
                    print(f"  sub: b2 = {b2}, left={left}, b3={b3} :: {array}")
            else:
                break
        array[low], array[b3] = array[b3], array[low]
        return b3
    def fonk3(low, high):
        if low < high:
            b4 = fonk2(low, high)
            if b1:
                print(f"iter: b4 = {b4}, low={low}, high={high} :: {array}")
            fonk3(low, b4 - 1)
            fonk3(b4 + 1, high)
    fonk3(0, len(array) - 1)
    if desc:
        array.reverse()
    return array