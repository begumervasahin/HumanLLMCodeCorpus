import sys
import tkinter as tk
import random
class class1(tk.Canvas):
    b1 = "white"
    b2 = "gray50"
    b3 = "red"
    b4 = "black"
    def fonk1(self, master, b5 = 60):
        tk.Canvas.fonk14(self, master, b6 = b5, width=b5, b9=class1.b2,
                           b7 = 2, b10=class1.b4)
    def fonk2(self, state):
        b8 = class1.b1 if state else class1.b2
        self.configure(b9 = b8)
    def fonk3(self, selected):
        b8 = class1.b3 if selected else class1.b4
        self.configure(b10 = b8)
class class2(tk.Frame):
    def fonk4(self, master, b11, b12, b13):
        tk.Frame.fonk14(self, master)
        self.b11 = b11
        self.b12 = b12
        self.b13 = b13
        self.b14 = []
        for b17 in range(self.b12):
            b15 = []
            for b20 in range(self.b13):
                b16 = class1(self)
                b16.grid(b17 = b17, column=b20, padx=1, pady=1)
                b16.bind("<Button-1>", lambda event, b17 = b17, b20=b20: self.fonk5(b17, b20))
                b15.append(b16)
            self.b14.append(b15)
    def fonk5(self, b17, b20):
        self.b11.fonk15(b17, b20)
        self.fonk6()
    def fonk6(self):
        b18 = self.b11.fonk17()
        for b17 in range(self.b12):
            for b20 in range(self.b13):
                self.b14[b17][b20].fonk2(b18[b17][b20])
    def fonk7(self, moves, b19 = 500):
        if moves:
            b17, b20 = moves[0]
            def fonk8():
                self.b14[b17][b20].fonk3(True)
                self.after(b19, stage_2)
            def fonk9():
                self.b14[b17][b20].fonk3(False)
                self.b11.fonk15(b17, b20)
                self.fonk6()
                self.after(b19, stage_3)
            def fonk10():
                self.fonk7(moves[1:], b19 = b19)
            fonk8()
class class3(tk.Frame):
    def fonk11(self, master, b12, b13):
        tk.Frame.fonk14(self, master)
        self.b11 = class4(b12, b13)
        self.b21 = class2(self, self.b11, b12, b13)
        self.b21.pack(b22 = tk.LEFT, padx=1, pady=1)
        b23 = tk.Frame(self)
        tk.Button(b23, b24 = "Scramble", command=self.scramble_click).pack(fill=tk.X, padx=1, pady=1)
        tk.Button(b23, b24 = "Solve", command=self.solve_click).pack(fill=tk.X, padx=1, pady=1)
        b23.pack(b22 = tk.RIGHT)
    def fonk12(self):
        self.b11.fonk18()
        self.b21.fonk6()
    def fonk13(self):
        self.b21.fonk7(self.b11.fonk19())
class class4:
    def fonk14(self, b12, b13):
        self.b12 = b12
        self.b13 = b13
        self.b21 = [[False] * b13 for _ in range(b12)]
    def fonk15(self, b17, b20):
        self.fonk16(b17, b20)
        if b17 > 0:
            self.fonk16(b17 - 1, b20)
        if b17 < self.b12 - 1:
            self.fonk16(b17 + 1, b20)
        if b20 > 0:
            self.fonk16(b17, b20 - 1)
        if b20 < self.b13 - 1:
            self.fonk16(b17, b20 + 1)
    def fonk16(self, b17, b20):
        self.b21[b17][b20] = not self.b21[b17][b20]
    def fonk17(self):
        return self.b21
    def fonk18(self):
        for _ in range(self.b12 * self.b13 * 3):
            b17 = random.randint(0, self.b12 - 1)
            b20 = random.randint(0, self.b13 - 1)
            self.fonk15(b17, b20)
    def fonk19(self):
        return []
if b25 = = "__main__":
    b26 = tk.Tk()
    b26.title("Lights Out")
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <b12> <b13>")
        sys.exit(1)
    b12, b13 = map(int, sys.argv[1:])
    class3(b26, b12, b13).pack()
    b26.resizable(b6 = False, width=False)
    b26.mainloop()