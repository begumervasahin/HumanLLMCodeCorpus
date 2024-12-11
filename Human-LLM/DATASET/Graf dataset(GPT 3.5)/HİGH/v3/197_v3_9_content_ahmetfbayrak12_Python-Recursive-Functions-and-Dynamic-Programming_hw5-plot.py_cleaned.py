import matplotlib.pyplot as plt
b1 = [15, 16, 18, 20, 22]
b2 = [0.000281095504761, 0.000301122665405, 0.000349998474121, 0.000365018844604, 0.000380992889404]
b3 = [0.527917861938, 1.51841020584, 8.46917390823, 54.8444831371, 269.672949076]
plt.figure(b4 = (8, 6))
plt.subplot(2, 1, 1)
plt.plot(b1, b2, b5 = 'o', linestyle='-', label="Dynamic Method", color="red")
plt.ylabel("Time (s)")
plt.legend(b6 = "lower right")
plt.title("Dynamic Programming Method")
plt.subplot(2, 1, 2)
plt.plot(b1, b3, b5 = 'o', linestyle='-', label="Recursive Method", color="blue")
plt.xlabel("M + N")
plt.ylabel("Time (s)")
plt.legend(b6 = "upper left")
plt.title("Recursive Method")
plt.tight_layout()
plt.show()