
TIME_INTERVALS = [(0, 0), (0, 3), (3, 6), (6, float('inf'))]
MIN_SUP = 0.50
DB = [
    [('a', 1), ('b', 3), ('c', 3), ('a', 5), ('e', 5), ('c', 10)],
    [('d', 5), ('a', 7), ('b', 7), ('e', 7), ('d', 8), ('e', 8), ('c', 14), ('d', 15)],
    [('a', 8), ('b', 8), ('e', 11), ('d', 12), ('b', 13), ('c', 13), ('c', 16)],
    [('b', 15), ('f', 15), ('e', 16), ('b', 17), ('c', 17)]
]
class MultiTimeIntervalApriori:
    def __init__(self, db=DB, time_intervals=TIME_INTERVALS, min_sup=MIN_SUP):
        self.db = db
        self.time_intervals = time_intervals
        self.min_sup = min_sup
    def run_apriori(self, max_sequence_length=6, verbose=True):
        pass
if __name__ == "__main__":
    from config import DB, TIME_INTERVALS, MIN_SUP
    m = MultiTimeIntervalApriori(db=DB, time_intervals=TIME_INTERVALS, min_sup=MIN_SUP)
    m.run_apriori(max_sequence_length=6, verbose=True)