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
    current_index = 1
    def swap(position1, position2):
        nonlocal array
        array[position1], array[position2] = array[position2], array[position1]
    while current_index < len(array):
        previous_index = current_index
        while current_index > 0 and array[current_index] < array[current_index - 1]:
            swap(current_index, current_index - 1)
            current_index -= 1
            yield array, current_index
        if current_index != previous_index:
            current_index = previous_index + 1
        else:
            current_index += 1
            yield array, current_index
    yield array, len(array) - 1
number_of_elements = 25
random_list = [random.randrange(1, 200) for _ in range(number_of_elements)]
plot_cont(insertion_sort_step_generator(random_list))