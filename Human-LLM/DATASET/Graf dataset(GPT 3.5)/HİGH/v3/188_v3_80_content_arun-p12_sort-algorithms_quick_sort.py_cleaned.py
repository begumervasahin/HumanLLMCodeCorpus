from common import swap
def fonk1(b4, b1 = 0, desc=0):
    def fonk2(lower_bound, upper_bound):
        pivot, start, b2 = b4[lower_bound], lower_bound, upper_bound
        while start < b2:
            while b4[start] <= pivot and start < upper_bound:
                start += 1
            while b4[b2] > pivot and b2 > lower_bound:
                b2 -= 1
            if start < b2:
                b4[start], b4[b2] = swap(b4[start], b4[b2])
            if b1 = = 2:
                print("  sub:", pivot, start, b2, " :: ", b4)
        b4[lower_bound], b4[b2] = swap(b4[lower_bound], b4[b2])
        return b2
    def fonk3(start_index, end_index):
        if start_index < end_index:
            b3 = fonk2(start_index, end_index)
            if b1:
                print("iter :", b3, start_index, end_index, " :: ", b4)
            fonk3(start_index, b3 - 1)
            fonk3(b3 + 1, end_index)
    fonk3(0, len(b4) - 1)
    if desc:
        b4 = b4[::-1]
    return b4
if b5 = = "__main__":
    b6 = [3, 1, 7, 2, 9, 5, 4, 8, 6]
    print("Original list:", b6)
    b7 = fonk1(b6, b1=1)
    print("Sorted list using Quick Sort:", b7)