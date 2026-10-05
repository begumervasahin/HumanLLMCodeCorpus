from random import shuffle, seed
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def swap(arr, index_1, index_2):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
def bubblesort_generator(A):
    if len(A) == 1:
        yield A
        return
    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A
def insertionsort_generator(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            swap(A, j, j - 1)
            j -= 1
            yield A
def get_speed_choice():
    speed_choice = int(input("Enter speed of sorting (1/Fast, 2/Medium, 3/Slow, 4/Manual): "))
    if speed_choice == 1:
        return 10
    elif speed_choice == 2:
        return 100
    elif speed_choice == 3:
        return 500
    elif speed_choice == 4:
        return int(input("Enter speed (1-1000 milliseconds): "))
    else:
        print("Invalid choice")
        exit()
def get_sorting_method():
    sort_choice = input("Enter sorting method (1/Bubble Sort, 2/Insertion Sort, 3/Merge Sort, 4/Quick Sort): ")
    if sort_choice == "1":
        return "Bubble Sort", bubblesort_generator
    elif sort_choice == "2":
        return "Insertion Sort", insertionsort_generator
def main():
    seed(time.time())
    N = int(input("Enter number of integers you want to sort: "))
    A = [x + 1 for x in range(N)]
    shuffle(A)
    speedofSort = get_speed_choice()
    title, sorting_algorithm = get_sorting_method()
    generator = sorting_algorithm(A.copy())
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(A)), A, align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))
    noOfOperations = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    timeTaken = ax.text(0.02, 0.91, "", transform=ax.transAxes)
    interval = ax.text(0.02, 0.87, f"Interval duration: {speedofSort} ms", transform=ax.transAxes)
    i = [0]
    start_time = time.time()
    def update_fig(A, rects, i):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        i[0] += 1
        noOfOperations.set_text(f"No. of operations: {i[0]}")
        time_elapsed = (time.time() - start_time)
        time_elapsed = float("{0:.2f}".format(time_elapsed))
        time_elapsed = str(time_elapsed)
        timeTaken.set_text(f"Time taken: {time_elapsed} sec")
    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, i), frames=generator, interval=speedofSort,
        repeat=False)
    plt.show()
if __name__ == "__main__":
    main()