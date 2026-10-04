import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
def plot_sort_animation(sort_steps):
    fig, ax = plt.subplots()
    values, highlight_index = next(sort_steps)
    num_elements = len(values)
    max_frames = num_elements ** 2
    def update(frame):
        try:
            values, highlight_index = next(sort_steps)
            ax.clear()
            bars = ax.bar(range(num_elements), values, color='blue')
            bars[highlight_index].set_color('red')
            print(f'Iteration: {frame}')
        except StopIteration:
            print("Sorting complete.")
            animation.event_source.stop()
    anim = animation.FuncAnimation(fig, update, frames=max_frames, repeat=False)
    plt.show()
def insertion_sort_generator(lst):
    n = len(lst)
    for i in range(1, n):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            yield lst, j
            j -= 1
        yield lst, i
    yield lst, -1
if __name__ == "__main__":
    num_elements = 25
    random_list = [random.randint(1, 200) for _ in range(num_elements)]
    plot_sort_animation(insertion_sort_generator(random_list))