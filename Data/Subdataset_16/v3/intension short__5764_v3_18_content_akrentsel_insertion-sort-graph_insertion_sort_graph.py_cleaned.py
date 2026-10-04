import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
def fonk1(sort_steps):
    fig, b1 = plt.subplots()
    values, b2 = next(sort_steps)
    b3 = len(values)
    b4 = b3 ** 2
    def fonk2(frame):
        try:
            values, b2 = next(sort_steps)
            b1.clear()
            b5 = b1.bar(range(b3), values, color='blue')
            b5[b2].set_color('red')
            print(f'Iteration: {frame}')
        except StopIteration:
            print("Sorting complete.")
            animation.event_source.stop()
    b6 = animation.FuncAnimation(fig, update, frames=b4, repeat=False)
    plt.show()
def fonk3(lst):
    b7 = len(lst)
    for i in range(1, b7):
        b8 = i
        while b8 > 0 and lst[b8] < lst[b8 - 1]:
            lst[b8], lst[b8 - 1] = lst[b8 - 1], lst[b8]
            yield lst, b8
            b8 -= 1
        yield lst, i
    yield lst, -1
if b9 = = "__main__":
    b3 = 25
    b10 = [random.randint(1, 200) for _ in range(b3)]
    fonk1(fonk3(b10))