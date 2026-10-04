
score_differential_ranges = [
    (0, 12), (13, 37), (38, 62), (63, 87), (88, 112),
    (113, 137), (138, 162), (163, 187), (188, 212),
    (213, 237), (238, 9999)
]
lookup_table = {
    'upset': {
        score_differential_ranges[0]: 8,
        score_differential_ranges[1]: 10,
        score_differential_ranges[2]: 13,
        score_differential_ranges[3]: 16,
        score_differential_ranges[4]: 20,
        score_differential_ranges[5]: 25,
        score_differential_ranges[6]: 30,
        score_differential_ranges[7]: 35,
        score_differential_ranges[8]: 40,
        score_differential_ranges[9]: 45,
        score_differential_ranges[10]: 50
    },
    'expected_result': {
        score_differential_ranges[0]: 8,
        score_differential_ranges[1]: 7,
        score_differential_ranges[2]: 6,
        score_differential_ranges[3]: 5,
        score_differential_ranges[4]: 4,
        score_differential_ranges[5]: 3,
        score_differential_ranges[6]: 2,
        score_differential_ranges[7]: 2,
        score_differential_ranges[8]: 1,
        score_differential_ranges[9]: 1,
        score_differential_ranges[10]: 0
    }
}
def get_adjustment(winner_rating, loser_rating):
    result_type = 'upset' if winner_rating < loser_rating else 'expected_result'
    score_differential = abs(winner_rating - loser_rating)
    for differential_range, adjustment_value in lookup_table[result_type].items():
        if score_differential in range(differential_range[0], differential_range[1] + 1):
            return adjustment_value
if __name__ == "__main__":
    winner_rating = 1500
    loser_rating = 1450
    adjustment = get_adjustment(winner_rating, loser_rating)
    print(f"The adjustment value is: {adjustment}")