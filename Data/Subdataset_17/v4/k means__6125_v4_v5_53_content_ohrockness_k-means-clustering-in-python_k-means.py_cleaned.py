import tkinter as tk
from tkinter import Canvas, Label
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def main():
    data = {
        'x': [25, 34, 22, 27, 33, 33, 31, 22, 35, 34, 67, 54, 57, 43, 50, 57, 59, 52, 65, 47, 49, 48, 35, 33, 44, 45, 38, 43, 51, 46],
        'y': [79, 51, 53, 78, 59, 74, 73, 57, 69, 75, 51, 32, 40, 47, 53, 36, 35, 58, 59, 50, 25, 20, 14, 12, 20, 5, 29, 27, 8, 7]
    }
    df = DataFrame(data, columns=['x', 'y'])
    kmeans = KMeans(n_clusters=3).fit(df)
    centroids = kmeans.cluster_centers_
    root = tk.Tk()
    root.title("KMeans Clustering Visualization")
    frame = tk.Frame(root)
    frame.pack()
    centroids_label = Label(frame, text=f"Centroids:\n{centroids}")
    centroids_label.grid(row=0, column=0, padx=10, pady=10)
    canvas = Canvas(frame, width=600, height=400)
    canvas.grid(row=0, column=1)
    fig = plt.Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float), s=50, alpha=0.5, label='Data Points')
    ax.scatter(centroids[:, 0], centroids[:, 1], c='red', s=100, marker='s', label='Centroids')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('KMeans Clustering')
    ax.legend()
    canvas = FigureCanvasTkAgg(fig, master=canvas)
    canvas.draw()
    canvas.get_tk_widget().pack()
    root.mainloop()
if __name__ == "__main__":
    main()