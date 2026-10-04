import queue as Q
class ComparableString(str):
    def __lt__(self, other):
        return len(self) < len(other)
def main():
    priority_queue = Q.PriorityQueue()
    priority_queue.put(ComparableString('jeej'))
    priority_queue.put(ComparableString('kek'))
    priority_queue.put(ComparableString('topkek'))
    priority_queue.put(ComparableString('non'))
    smallest_string = sorted(priority_queue.queue)[0]
    print(smallest_string)
if __name__ == "__main__":
    main()