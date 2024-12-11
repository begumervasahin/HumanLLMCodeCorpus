import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random
def fonk1(gen):
    y_vals, b1 = next(gen)
    b2 = len(y_vals) ** 2
    b3 = plt.figure()
    b4 = b3.add_subplot(1,1,1)
    def fonk2(i):
        y_vals, b1 = next(gen)
        b5 = [0] * len(y_vals)
        b5[b1] = y_vals[b1]
        b6 = range(len(y_vals))
        b4.clear()
        b4.bar(b6, y_vals, b7 = 1)
        b4.bar(b6, b5, b7 = 1, color="red")
        print('Iteration: ', i)
    b8 = anim.FuncAnimation(b3, update, frames=b2, repeat=False)
    plt.show()
def fonk3(ls):
	assert len(ls) > 1, "Length of list must be greater than 1 to sort"
	b9 = 1;
	def fonk4(pos1, pos2):
		nonlocal ls
		ls[pos1], ls[pos2] = ls[pos2], ls[pos1]
	while b9 < len(ls):
		b10 = b9
		while b9 > 0 and ls[b9] < ls[b9 - 1]:
			fonk4(b9, b9 - 1)
			b9 = b9 - 1
			yield ls, b9
		if b9 != b10:
			b9 = b10 + 1
		else:
			b9 = b9 + 1
			yield ls, b9
	yield ls, len(ls) - 1
a1 = 25
b11 = []
for _ in range(a1):
	b11 += [random.randrange(1, 200)]
fonk1(fonk3(b11))