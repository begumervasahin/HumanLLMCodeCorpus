class DijkstraPriorityQueue:
    def __init__(self):
        self.heap = []
    def __len__(self):
        return len(self.heap)
    def build_heap(self, items):
        self.heap = items[:]
        n = len(self.heap)
        for i in range(n
            self._percolate_down(i)
    def _percolate_up(self, i):
        while i > 0:
            parent = (i - 1)
            if self.heap[i][0] < self.heap[parent][0]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break
    def _percolate_down(self, i):
        while 2 * i + 1 < len(self.heap):
            left_child = 2 * i + 1
            right_child = left_child + 1
            min_child = left_child
            if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[left_child][0]:
                min_child = right_child
            if self.heap[i][0] > self.heap[min_child][0]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                i = min_child
            else:
                break
    def insert(self, item):
        self.heap.append(item)
        self._percolate_up(len(self.heap) - 1)
    def delete_min(self):
        if not self.heap:
            return None
        min_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._percolate_down(0)
        return min_item
    def update_priority(self, item, priority):
        for i in range(len(self.heap)):
            if self.heap[i][1] == item:
                old_priority = self.heap[i][0]
                self.heap[i] = (priority, item)
                if priority < old_priority:
                    self._percolate_up(i)
                else:
                    self._percolate_down(i)
def valid_within_bounding_box(start, end, point):
    if end is None:
        return True
    small_x, large_x = min(start[0], end[0]), max(start[0], end[0])
    small_y, large_y = min(start[1], end[1]), max(start[1], end[1])
    return small_x <= point[0] <= large_x and small_y <= point[1] <= large_y
def shortest_path(adj_list, source, end=None):
    """
    Runs Dijkstra's algorithm on the graph represented by adj_list.
    @param adj_list: A dictionary mapping each node to a list of (neighbor, edge_weight)
    @param source: The source node from which to begin our search
    @param end: Optional end node for bounded search
    @return dist: A dictionary mapping each node to its distance from "source"
    @return p: A "node to parent" mapping which can be traversed to yield the paths themselves
    """
    dist = {}
    p = {}
    for node in adj_list:
        if valid_within_bounding_box(source, end, node):
            dist[node] = float("inf")
            p[node] = None
    dist[source] = 0
    priority_queue = DijkstraPriorityQueue()
    priority_queue.build_heap([[v, k] for k, v in dist.items()])
    while len(priority_queue) > 0:
        curr = priority_queue.delete_min()[1]
        if curr == end:
            return dist, p
        for nbr, wt in adj_list[curr]:
            if valid_within_bounding_box(source, end, nbr) and wt + dist[curr] < dist[nbr]:
                dist[nbr] = wt + dist[curr]
                p[nbr] = curr
                priority_queue.update_priority(nbr, dist[nbr])
    return dist, p
def main():
    adj_list = {
        1: [(2, 15), (3, 71)],
        2: [(3, 7), (4, 1)],
        3: [(4, 19)],
        4: [(3, 1)]
    }
    print(shortest_path(adj_list, 1))
if __name__ == "__main__":
    main()