
STUDENT_CODE_DEFAULT = 'searchAgents.py,search.py'
PROJECT_TEST_CLASSES = 'searchTestClasses.py'
PROJECT_NAME = 'Project 1: Search'
BONUS_PIC = False
import searchAgents
import search
def main():
    maze = load_maze("maze_file.txt")
    print("Choose the search algorithm:")
    print("1. Depth First Search")
    print("2. Breadth First Search")
    print("3. Uniform Cost Search")
    print("4. A* Search")
    choice = input("Enter your choice: ")
    if choice == '1':
        path = searchAgents.depthFirstSearch(maze)
    elif choice == '2':
        path = searchAgents.breadthFirstSearch(maze)
    elif choice == '3':
        path = searchAgents.uniformCostSearch(maze)
    elif choice == '4':
        path = searchAgents.aStarSearch(maze, search.heuristic)
    else:
        print("Invalid choice!")
        return
    print("Path found:", path)
def load_maze(file_name):
    return []
if __name__ == "__main__":
    main()
def depthFirstSearch(problem):
    pass
def breadthFirstSearch(problem):
    pass
def uniformCostSearch(problem):
    pass
def aStarSearch(problem, heuristic):
    pass
def heuristic(state, problem=None):
    return 0
The searching pacman project performed as part of CSE 537 Artificial Intelligence Fall 2018.
Pac-man's got them searchin' blues
Searchin' for dots when there ain't no clues
Implemented the following techniques on various types of mazes, along with other heuristics.
1. Depth First Search
2. Breadth First Search
3. Uniform Cost Search
4. A* search
Please use Python 2.7.
Q8 in the autograder output wasn't a part of the assignment.