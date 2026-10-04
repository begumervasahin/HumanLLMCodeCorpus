import queue as Q
class ComparableString(str):
    def __lt__(self, other):
        return len(self) < len(other)
def main():
    priority_queue = Q.PriorityQueue()
    strings = ['jeej', 'kek', 'topkek', 'non']
    for string in strings:
        priority_queue.put(ComparableString(string))
    smallest_string = priority_queue.get()
    print("Smallest string by length:", smallest_string)
if __name__ == "__main__":
    main()