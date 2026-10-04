import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random
def plot_cont(generator):
    y_vals, red_index = next(generator)
    total_frames = len(y_vals) ** 2
    fig, ax = plt.subplots()
    def update(frame):
        y_vals, red_index = next(generator)
        red_bar = [0] * len(y_vals)
        red_bar[red_index] = y_vals[red_index]
        x = range(len(y_vals))
        ax.clear()
        ax.bar(x, y_vals, width=1)
        ax.bar(x, red_bar, width=1, color="red")
        print(f'Iteration: {frame}')
    animation = anim.FuncAnimation(fig, update, frames=total_frames, repeat=False)
    plt.show()
def insertion_sort_step_generator(arr):
    assert len(arr) > 1, "List must contain more than one element to sort"
    curr_index = 1
    while curr_index < len(arr):
        sorted_index = curr_index
        while sorted_index > 0 and arr[sorted_index] < arr[sorted_index - 1]:
            arr[sorted_index], arr[sorted_index - 1] = arr[sorted_index - 1], arr[sorted_index]
            sorted_index -= 1
            yield arr, sorted_index
        curr_index = sorted_index + 1 if sorted_index != curr_index else curr_index + 1
        yield arr, curr_index
    yield arr, len(arr) - 1
if __name__ == "__main__":
    num_elements = 25
    random_list = [random.randint(1, 200) for _ in range(num_elements)]
    plot_cont(insertion_sort_step_generator(random_list))