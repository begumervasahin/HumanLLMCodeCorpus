import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random
def plot_sort_animation(generator):
    fig, ax = plt.subplots()
    y_values, highlight_index = next(generator)
    max_frames = len(y_values) ** 2
    def update(frame):
        y_values, highlight_index = next(generator)
        highlight_bar = [0] * len(y_values)
        highlight_bar[highlight_index] = y_values[highlight_index]
        ax.clear()
        ax.bar(range(len(y_values)), y_values, width=1)
        ax.bar(range(len(y_values)), highlight_bar, width=1, color="red")
        print(f'Iteration: {frame}')
    animation = anim.FuncAnimation(fig, update, frames=max_frames, repeat=False)
    plt.show()
def insertion_sort_step_generator(lst):
    assert len(lst) > 1, "List must contain more than one element to sort."
    current_index = 1
    def swap(index1, index2):
        lst[index1], lst[index2] = lst[index2], lst[index1]
    while current_index < len(lst):
        temp_index = current_index
        while current_index > 0 and lst[current_index] < lst[current_index - 1]:
            swap(current_index, current_index - 1)
            current_index -= 1
            yield lst, current_index
        if current_index != temp_index:
            current_index = temp_index + 1
        else:
            current_index += 1
            yield lst, current_index
    yield lst, len(lst) - 1
if __name__ == "__main__":
    num_elements = 25
    random_list = [random.randint(1, 200) for _ in range(num_elements)]
    plot_sort_animation(insertion_sort_step_generator(random_list))