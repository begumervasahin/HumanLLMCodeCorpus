import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random
def plot_sort_animation(sort_generator):
    initial_values, red_index = next(sort_generator)
    max_frames = len(initial_values) ** 2
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    def update_frame(i):
        values, red_index = next(sort_generator)
        red_bar = [0] * len(values)
        red_bar[red_index] = values[red_index]
        x = range(len(values))
        ax.clear()
        ax.bar(x, values, width=1)
        ax.bar(x, red_bar, width=1, color="red")
        print('Iteration:', i)
    animation = anim.FuncAnimation(fig, update_frame, frames=max_frames, repeat=False)
    plt.show()
def insertion_sort_step_generator(lst):
    assert len(lst) > 1, "Length of list must be greater than 1 to sort"
    current_index = 1
    def swap(pos1, pos2):
        nonlocal lst
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    while current_index < len(lst):
        temp = current_index
        while current_index > 0 and lst[current_index] < lst[current_index - 1]:
            swap(current_index, current_index - 1)
            current_index -= 1
            yield lst, current_index
        if current_index != temp:
            current_index = temp + 1
        else:
            current_index += 1
            yield lst, current_index
    yield lst, len(lst) - 1
number_of_elements = 25
random_list = [random.randrange(1, 200) for _ in range(number_of_elements)]
plot_sort_animation(insertion_sort_step_generator(random_list))