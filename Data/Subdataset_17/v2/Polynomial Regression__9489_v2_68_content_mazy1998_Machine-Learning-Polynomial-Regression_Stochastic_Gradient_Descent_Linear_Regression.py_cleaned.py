import random
from tkinter import *
import time
class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        numPoints = 600
        self.myCanvas = Canvas(self, width=numPoints, height=numPoints, bg="black")
        self.myCanvas.grid()
        deltaB = random.uniform(-1, 1)
        deltaM = random.uniform(-1, 1)
        def function(x):
            return 0.5 * x + 250
        data = [(i, function(i) + random.randint(-10, 10)) for i in range(numPoints)]
        for x, y in data:
            self.myCanvas.create_line(x, numPoints - y, x + 1, numPoints - y + 1, fill="green")
        size = len(data)
        def update():
            canvas_id = self.myCanvas.create_line(
                0, numPoints - b,
                numPoints, numPoints - (m * numPoints + b),
                fill="red"
            )
            self.myCanvas.update()
            time.sleep(0.1)
            self.myCanvas.after(10, self.myCanvas.delete, canvas_id)
        for _ in range(120):
            deltaB += (data[0][1] - deltaB) * 0.05
            for x, y in data:
                guess = deltaM * x + deltaB
                error = y - guess
                deltaM += (1 / size) * x * error * 0.001
            m = deltaM
            b = deltaB
            update()
        self.myCanvas.create_line(
            0, numPoints - b,
            numPoints, numPoints - (m * numPoints + b),
            fill="red"
        )
        print(m, b)
frame02 = MyFrame()
frame02.mainloop()