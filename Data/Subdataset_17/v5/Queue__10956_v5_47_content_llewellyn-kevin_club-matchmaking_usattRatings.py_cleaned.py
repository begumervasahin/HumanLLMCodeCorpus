
RATING_RANGE_KEYS = [
    (0, 12), (13, 37), (38, 62), (63, 87), (88, 112),
    (113, 137), (138, 162), (163, 187), (188, 212), (213, 237), (238, 9999)
]
LOOKUP_TABLE = {
    'upset': {
        RATING_RANGE_KEYS[0]: 8,
        RATING_RANGE_KEYS[1]: 10,
        RATING_RANGE_KEYS[2]: 13,
        RATING_RANGE_KEYS[3]: 16,
        RATING_RANGE_KEYS[4]: 20,
        RATING_RANGE_KEYS[5]: 25,
        RATING_RANGE_KEYS[6]: 30,
        RATING_RANGE_KEYS[7]: 35,
        RATING_RANGE_KEYS[8]: 40,
        RATING_RANGE_KEYS[9]: 45,
        RATING_RANGE_KEYS[10]: 50
    },
    'expected_result': {
        RATING_RANGE_KEYS[0]: 8,
        RATING_RANGE_KEYS[1]: 7,
        RATING_RANGE_KEYS[2]: 6,
        RATING_RANGE_KEYS[3]: 5,
        RATING_RANGE_KEYS[4]: 4,
        RATING_RANGE_KEYS[5]: 3,
        RATING_RANGE_KEYS[6]: 2,
        RATING_RANGE_KEYS[7]: 2,
        RATING_RANGE_KEYS[8]: 1,
        RATING_RANGE_KEYS[9]: 1,
        RATING_RANGE_KEYS[10]: 0
    }
}
def get_adjustment(winner_rating, loser_rating):
    result_type = 'upset' if winner_rating < loser_rating else 'expected_result'
    score_differential = abs(winner_rating - loser_rating)
    for range_key, adjustment_value in LOOKUP_TABLE[result_type].items():
        if range_key[0] <= score_differential <= range_key[1]:
            return adjustment_value
if __name__ == "__main__":
    winner_rating = 1500
    loser_rating = 1400
    adjustment = get_adjustment(winner_rating, loser_rating)
    print(f"The adjustment value is: {adjustment}")