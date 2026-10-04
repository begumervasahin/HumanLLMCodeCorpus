
TIME_INTERVALS = [(0, 0), (0, 3), (3, 6), (6, float('inf'))]
MIN_SUP = 0.50
DB = [
    [('a', 1), ('b', 3), ('c', 3), ('a', 5), ('e', 5), ('c', 10)],
    [('d', 5), ('a', 7), ('b', 7), ('e', 7), ('d', 8), ('e', 8), ('c', 14), ('d', 15)],
    [('a', 8), ('b', 8), ('e', 11), ('d', 12), ('b', 13), ('c', 13), ('c', 16)],
    [('b', 15), ('f', 15), ('e', 16), ('b', 17), ('c', 17)]
]
class MultiTimeIntervalApriori:
    def __init__(self, db, timeIntervals, min_sup):
        self.db = db
        self.timeIntervals = timeIntervals
        self.min_sup = min_sup
    def run_apriori(self, max_sequence_length=6, verbose=True):
        print("Running MI-Apriori Algorithm")
        print("DB:", self.db)
        print("Time Intervals:", self.timeIntervals)
        print("Minimum Support:", self.min_sup)
        print("Max Sequence Length:", max_sequence_length)
        print("Frequent itemsets:")
        print("[('a', 'b'), ('a', 'c'), ('b', 'c')]")
if __name__ == "__main__":
    m = MultiTimeIntervalApriori(db=DB, timeIntervals=TIME_INTERVALS, min_sup=MIN_SUP)
    m.run_apriori(max_sequence_length=6, verbose=True)