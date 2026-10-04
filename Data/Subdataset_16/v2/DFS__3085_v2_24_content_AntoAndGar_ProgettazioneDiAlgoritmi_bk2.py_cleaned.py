def fonk1(n, k):
    def fonk2(b1, ones_count, current_string):
        if b1 = = n:
            print(''.join(current_string))
            return
        current_string.append('0')
        fonk2(b1 + 1, ones_count, current_string)
        current_string.pop()
        if ones_count < k:
            current_string.append('1')
            fonk2(b1 + 1, ones_count + 1, current_string)
            current_string.pop()
    fonk2(0, 0, [])
fonk1(4, 1)