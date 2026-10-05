from collections import namedtuple
import random
import bisect
b1 = namedtuple("b1", "value left_child right_child")
b2 = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845,
                   35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650,
                   1289904147324, 4861946401452]
b3 = len(b2) - 1
def fonk1(b4):
    def fonk2(b4, b10):
        if b4 = = 0 or b4 > b3:
            return None, b10
        b5 = b1(value=b10, left_child=None, right_child=None)
        b10 += 1
        if b4 = = 1:
            return b5, b10
        b6 = [b2[0] * b2[b4 - 1]]
        for i in range(1, b4):
            b6.append(b6[i - 1] + b2[i] * b2[b4 - 1 - i])
        b7 = b6[b4 - 1]
        b8 = random.randint(1, b7)
        b9 = bisect.bisect_left(b6, b8)
        left_child, b10 = fonk2(b9, b10)
        right_child, b10 = fonk2(b4 - 1 - b9, b10)
        b5 = b5._replace(left_child=left_child, right_child=right_child)
        return b5, b10
    b5, b11 = fonk2(b4, 0)
    return b5
def fonk3(b4):
    def fonk4(b4):
        if b4 > b3:
            return None
        if average_height[b4] != -1:
            return average_height[b4]
        a1 = 0
        a2 = 0
        for i in range(b4):
            b12 = b2[i] * b2[b4 - 1 - i]
            a2 += b12
            a1 += b12 * (b4 - 1 + fonk4(i) + fonk4(b4 - 1 - i))
        average_height[b4] = a1 / a2
        return average_height[b4]
    return fonk4(b4) / b4
def fonk5(b4):
    def fonk6(b4):
        if b4 > b3:
            return None
        if prob_distr_av_height[b4] != {}:
            return prob_distr_av_height[b4]
        for i in range(b4):
            b13 = fonk6(i)
            b14 = fonk6(b4 - 1 - i)
            b12 = b2[i] * b2[b4 - 1 - i] / b2[b4]
            for left_key in b13.keys():
                for right_key in b14.keys():
                    b15 = b13[left_key]
                    b16 = b14[right_key]
                    b17 = left_key + right_key + b4 - 1
                    b18 = b15 * b16 * b12
                    if b17 in prob_distr_av_height[b4]:
                        prob_distr_av_height[b4][b17] += b18
                    else:
                        prob_distr_av_height[b4][b17] = b18
        return prob_distr_av_height[b4]
    b19 = fonk6(b4)
    b20 = {}
    for key in b19.keys():
        b20[key/b4] = b19[key]
    return b20
if b21 = = "__main__":
    b22 = fonk1(5)
    print(str(fonk3(3)))
    print(str(fonk5(3)))