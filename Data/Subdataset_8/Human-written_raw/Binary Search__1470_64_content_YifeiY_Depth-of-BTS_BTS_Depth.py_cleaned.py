from random import shuffle
import csv
class Tree():
    def __init__(self,value = None,left = None,right = None):
        self.value = value
        self.left = left
        self.right = right
    def insert(self,x):
        self.rec_insert(x)
    def rec_insert(current,x):
        if current == None:
            return Tree(x,None,None)
        elif current.value > x:
            current.left = Tree.rec_insert(current.left,x)
        else:
            current.right = Tree.rec_insert(current.right,x)
        return current
    def height(self,tree=None):
        if tree == None:
            return 0
        return max(self.height(tree.left),self.height(tree.right)) + 1
def generate_random_array(n):
    array = [i for i in range (n)]
    shuffle(array)
    return array
def build_tree(arr):
    tree = Tree(arr[0], None, None)
    for i in range (1,len(arr)):
        tree.insert(arr[i])
    return tree
def main():
    print("n is the number of vertices in the Binary Search Tree \nh is the corresponding average height of 500 randomly generated sample\n")
    results = [["number of nodes","height"]]
    trail = 500
    print("Generating results.....")
    for n in range (100, 1001, 100):
        height_sum = 0
        for t in range (trail):
            arr = generate_random_array(n)
            tree = build_tree(arr)
            height_sum = height_sum + tree.height(tree)
        results.append([n,height_sum/500])
        print("n = %4d, h = %2.3f" % (results[-1][0], results[-1][1]))
    with open("results.csv","w+") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(results)
main()