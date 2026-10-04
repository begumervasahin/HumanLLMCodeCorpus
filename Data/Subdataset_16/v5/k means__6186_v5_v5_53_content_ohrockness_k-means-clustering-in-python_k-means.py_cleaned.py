import tkinter as tk
from tkinter import Canvas, Label
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def fonk1():
    b1 = {
        'x': [25, 34, 22, 27, 33, 33, 31, 22, 35, 34, 67, 54, 57, 43, 50, 57, 59, 52, 65, 47, 49, 48, 35, 33, 44, 45, 38, 43, 51, 46],
        'y': [79, 51, 53, 78, 59, 74, 73, 57, 69, 75, 51, 32, 40, 47, 53, 36, 35, 58, 59, 50, 25, 20, 14, 12, 20, 5, 29, 27, 8, 7]
    }
    return DataFrame(b1, b2 = ['x', 'y'])
def fonk2(b8, b3 = 3):
    b4 = KMeans(b3=b3).fit(b8)
    return b4.cluster_centers_, b4.labels_
def fonk3(b8, centroids, b9):
    b5 = plt.Figure(figsize=(6, 4))
    b6 = b5.add_subplot(111)
    b6.scatter(b8['x'], b8['y'], b7 = b9.astype(float), s=50, alpha=0.5, label='Data Points')
    b6.scatter(centroids[:, 0], centroids[:, 1], b7 = 'red', s=100, marker='s', label='Centroids')
    b6.set_xlabel('X')
    b6.set_ylabel('Y')
    b6.set_title('KMeans Clustering')
    b6.legend()
    return b5
def fonk4():
    b8 = fonk1()
    centroids, b9 = fonk2(b8)
    b10 = tk.Tk()
    b10.title("KMeans Clustering Visualization")
    b11 = tk.Frame(b10)
    b11.pack()
    b12 = Label(b11, text=f"Centroids:\n{centroids}")
    b12.grid(b13 = 0, column=0, padx=10, pady=10)
    b14 = Canvas(b11, width=600, height=400)
    b14.grid(b13 = 0, column=1)
    b5 = fonk3(b8, centroids, b9)
    b15 = FigureCanvasTkAgg(b5, master=b14)
    b15.draw()
    b15.get_tk_widget().pack()
    b10.mainloop()
if b16 = = "__main__":
    fonk4()