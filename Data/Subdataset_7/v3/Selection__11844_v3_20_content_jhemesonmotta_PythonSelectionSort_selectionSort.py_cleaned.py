def fonk1(b2):
    for last_unsorted_pos in range(len(b2) - 1, 0, -1):
        a1 = 0
        for current_pos in range(1, last_unsorted_pos + 1):
            if b2[current_pos] > b2[a1]:
                a1 = current_pos
        b2[last_unsorted_pos], b2[a1] = b2[a1], b2[last_unsorted_pos]
if b1 = = "__main__":
    b2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    fonk1(b2)
    print("Sorted array:", b2)