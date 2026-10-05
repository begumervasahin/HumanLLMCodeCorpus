b1 = [(0, 12), (13, 37), (38, 62), (63, 87), (88, 112),
                    (113, 137), (138, 162), (163, 187), (188, 212), (213, 237), (238, 9999)]
b2 = {
    'upset': {
        b1[0]: 8,
        b1[1]: 10,
        b1[2]: 13,
        b1[3]: 16,
        b1[4]: 20,
        b1[5]: 25,
        b1[6]: 30,
        b1[7]: 35,
        b1[8]: 40,
        b1[9]: 45,
        b1[10]: 50
    },
    'expected_result': {
        b1[0]: 8,
        b1[1]: 7,
        b1[2]: 6,
        b1[3]: 5,
        b1[4]: 4,
        b1[5]: 3,
        b1[6]: 2,
        b1[7]: 2,
        b1[8]: 1,
        b1[9]: 1,
        b1[10]: 0
    }
}
def fonk1(a1, a2):
    b3 = 'upset' if a1 < a2 else 'expected_result'
    b4 = abs(a1 - a2)
    for k, v in b2[b3].items():
        if b4 in range(k[0], k[1] + 1):
            return v
a1 = 100
a2 = 110
b5 = fonk1(a1, a2)
print(f"Adjustment for winner rating {a1} and loser rating {a2}:", b5)