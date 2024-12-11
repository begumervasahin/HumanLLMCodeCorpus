
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
b6 = tk.Canvas(b5, width=100, height=100)
b6.pack()
b7 = tk.Label(b5, text=b4, justify='center')
b6.create_window(70, 50, b8 = b7)
b9 = plt.Figure(figsize=(5, 4), dpi=100)
b10 = b9.add_subplot(111)
b10.scatter(b2['x'], b2['y'], b11 = b3.labels_.astype(float), s=50, alpha=0.5)
b10.scatter(b4[:, 0], b4[:, 1], b11 = 'red', s=50)
b12 = FigureCanvasTkAgg(b9, b5)
b12.get_tk_widget().pack(b13 = tk.LEFT, fill=tk.BOTH)
b5.mainloop()