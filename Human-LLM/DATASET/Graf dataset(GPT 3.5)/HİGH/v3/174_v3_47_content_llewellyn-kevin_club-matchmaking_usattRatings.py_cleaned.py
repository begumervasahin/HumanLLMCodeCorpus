
b1 = {
    'upset': {
        (0, 12): 8, (13, 37): 10, (38, 62): 13, (63, 87): 16, (88, 112): 20,
        (113, 137): 25, (138, 162): 30, (163, 187): 35, (188, 212): 40,
        (213, 237): 45, (238, 9999): 50
    },
    'expected_result': {
        (0, 12): 8, (13, 37): 7, (38, 62): 6, (63, 87): 5, (88, 112): 4,
        (113, 137): 3, (138, 162): 2, (163, 187): 2, (188, 212): 1,
        (213, 237): 1, (238, 9999): 0
    }
}
def fonk1(a1, a2):
    b2 = 'upset' if a1 < a2 else 'expected_result'
    b3 = abs(a1 - a2)
    for score_range, b4 in b1[b2].items():
        if score_range[0] <= b3 <= score_range[1]:
            return b4
a1 = 100
a2 = 110
b4 = fonk1(a1, a2)
print(f"Adjustment for winner rating {a1} and loser rating {a2}:", b4)