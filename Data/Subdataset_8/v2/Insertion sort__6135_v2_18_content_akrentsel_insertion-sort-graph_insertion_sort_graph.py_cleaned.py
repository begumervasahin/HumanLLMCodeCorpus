import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random
def plot_cont(generator):
    y_values, red_index = next(generator)
    max_frames = len(y_values) ** 2
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    def update(i):
        y_values, red_index = next(generator)
        red_bar = [0] * len(y_values)
        red_bar[red_index] = y_values[red_index]
        x = range(len(y_values))
        ax.clear()
        ax.bar(x, y_values, width=1)
        ax.bar(x, red_bar, width=1, color="red")
        print('Iteration:', i)
    animation = anim.FuncAnimation(fig, update, frames=max_frames, repeat=False)
    plt.show()
def insertion_sort_step_generator(array):
    assert len(array) > 1, "Length of list must be greater than 1 to sort"
    current = 1
    def swap(pos1, pos2):
        nonlocal array
        array[pos1], array[pos2] = array[pos2], array[pos1]
    while current < len(array):
        temp = current
        while current > 0 and array[current] < array[current - 1]:
            swap(current, current - 1)
            current -= 1
            yield array, current
        if current != temp:
            current = temp + 1
        else:
            current += 1
            yield array, current
    yield array, len(array) - 1
number_of_elements = 25
random_list = [random.randrange(1, 200) for _ in range(number_of_elements)]
plot_cont(insertion_sort_step_generator(random_list))