class PriorityQueueImpl:
    def __init__(self, heuristicFlag):
        self.items = []
        self.heuristicFlag = heuristicFlag
    def isEmpty(self):
        return len(self.items) == 0
    def sortComparatorByCost(self, item):
        return item.cost
    def sortComparatorByHeuristic(self, item):
        return item.heuristicFunction
    def enqueue(self, item):
        self.items.append(item)
        if self.heuristicFlag:
            self.items.sort(key=self.sortComparatorByHeuristic)
        else:
            self.items.sort(key=self.sortComparatorByCost)
    def dequeue(self):
        return self.items.pop(0)
    def returnQueueAsString(self):
        return ' '.join(str(eachItem) for eachItem in self.items)
    def isQueueContainsElement(self, element):
        for eachElement in self.items:
            if eachElement[0] == element:
                return True
        return False
if __name__ == "__main__":
    class Item:
        def __init__(self, cost, heuristicFunction):
            self.cost = cost
            self.heuristicFunction = heuristicFunction
        def __str__(self):
            return f"Item(cost={self.cost}, heuristicFunction={self.heuristicFunction})"
    priority_queue = PriorityQueueImpl(heuristicFlag=True)
    priority_queue.enqueue(Item(10, 5))
    priority_queue.enqueue(Item(8, 3))
    priority_queue.enqueue(Item(12, 7))
    print(priority_queue.returnQueueAsString())
    dequeued_item = priority_queue.dequeue()
    print("Dequeued item:", dequeued_item)
    print("Queue contains 5:", priority_queue.isQueueContainsElement(5))