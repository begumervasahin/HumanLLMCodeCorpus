import tkinter as tk
from tkinter import Canvas, Label
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def fonk1():
    b1 = {'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
            'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
           }
    b2 = DataFrame(b1, columns=['x','y'])
    b3 = KMeans(n_clusters=3).fit(b2)
    b4 = b3.cluster_centers_
    b5 = tk.Tk()
    b5.title("KMeans Clustering Visualization")
    b6 = tk.Frame(b5)
    b6.pack()
    b7 = Label(b6, text=f"Centroids:\n{b4}")
    b7.grid(b8 = 0, column=0)
    b9 = Canvas(b6, width=600, height=400)
    b9.grid(b8 = 0, column=1)
    b10 = plt.Figure(figsize=(6, 4))
    b11 = b10.add_subplot(111)
    b11.scatter(b2['x'], b2['y'], b12 = b3.labels_.astype(float), s=50, alpha=0.5, label='Data Points')
    b11.scatter(b4[:, 0], b4[:, 1], b12 = 'red', s=100, marker='s', label='Centroids')
    b11.set_xlabel('X')
    b11.set_ylabel('Y')
    b11.set_title('KMeans Clustering')
    b11.legend()
    b9 = FigureCanvasTkAgg(b10, master=b9)
    b9.draw()
    b9.get_tk_widget().pack()
    b5.mainloop()
if b13 = = "__main__":
    fonk1()