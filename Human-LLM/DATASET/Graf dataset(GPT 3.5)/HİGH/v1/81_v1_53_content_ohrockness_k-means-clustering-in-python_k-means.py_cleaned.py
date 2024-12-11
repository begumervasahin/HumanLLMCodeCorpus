from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
b1 = {'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
       }
b2 = DataFrame(b1, columns=['x','y'])
b3 = KMeans(n_clusters=3).fit(b2)
b4 = b3.cluster_centers_
b5 = tk.Tk()
b5.title("KMeans Clustering")
b6 = tk.Canvas(b5, width=200, height=100)
b6.pack()
b7 = tk.Label(b5, text="Centroids: " + str(b4))
b7.pack()
b8 = plt.Figure(figsize=(5,4), dpi=100)
b9 = b8.add_subplot(111)
b9.scatter(b2['x'], b2['y'], b10 = b3.labels_.astype(float), s=50, alpha=0.5)
b9.scatter(b4[:, 0], b4[:, 1], b10 = 'red', s=50)
b9.set_xlabel('X')
b9.set_ylabel('Y')
b9.set_title('KMeans Clustering')
b11 = FigureCanvasTkAgg(b8, b5)
b11.get_tk_widget().pack(b12 = tk.LEFT, fill=tk.BOTH)
b5.mainloop()