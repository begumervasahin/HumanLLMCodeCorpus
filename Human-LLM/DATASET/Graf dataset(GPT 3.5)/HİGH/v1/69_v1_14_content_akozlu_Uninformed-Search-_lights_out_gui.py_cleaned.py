import sys
import tkinter as tk
import random
class class1(tk.Canvas):
    b1 = "white"
    b2 = "gray50"
    b3 = "red"
    b4 = "black"
    def fonk1(self, master, b5 = 60):
        tk.Canvas.fonk14(self, master, b6 = b5, width=b5,
                           b7 = class1.b2, highlightthickness=2,
                           b8 = class1.b4)
    def fonk2(self, state):
        b9 = class1.b1 if state else class1.b2
        self.configure(b7 = b9)
    def fonk3(self, selected):
        b9 = class1.b3 if selected else class1.b4
        self.configure(b8 = b9)
class class2(tk.Frame):
    def fonk4(self, master, b10, b11, b12):
        tk.Frame.fonk14(self, master)
        self.b10 = b10
        self.b11 = b11
        self.b12 = b12
        self.b13 = []
        for b16 in range(self.b11):
            b14 = []
            for b19 in range(self.b12):
                b15 = class1(self)
                b15.grid(b16 = b16, column=b19, padx=1, pady=1)
                b15.bind("<Button-1>", lambda event, b16 = b16, b19=b19: self.fonk5(b16, b19))
                b14.append(b15)
            self.b13.append(b14)
    def fonk5(self, b16, b19):
        self.b10.fonk15(b16, b19)
        self.fonk6()
    def fonk6(self):
        b17 = self.b10.fonk17()
        for b16 in range(self.b11):
            for b19 in range(self.b12):
                self.b13[b16][b19].fonk2(b17[b16][b19])
    def fonk7(self, moves, b18 = 500):
        if moves:
            b16, b19 = moves[0]
            def fonk8():
                self.b13[b16][b19].fonk3(True)
                self.after(b18, stage_2)
            def fonk9():
                self.b13[b16][b19].fonk3(False)
                self.b10.fonk15(b16, b19)
                self.fonk6()
                self.after(b18, stage_3)
            def fonk10():
                self.fonk7(moves[1:], b18 = b18)
            fonk8()
class class3(tk.Frame):
    def fonk11(self, master, b11, b12):
        tk.Frame.fonk14(self, master)
        self.b10 = class4(b11, b12)
        self.b20 = class2(self, self.b10, b11, b12)
        self.b20.pack(b21 = tk.LEFT, padx=1, pady=1)
        b22 = tk.Frame(self)
        tk.Button(b22, b23 = "Scramble", command=self.scramble_click).pack(fill=tk.X, padx=1, pady=1)
        tk.Button(b22, b23 = "Solve", command=self.solve_click).pack(fill=tk.X, padx=1, pady=1)
        b22.pack(b21 = tk.RIGHT)
    def fonk12(self):
        self.b10.fonk18()
        self.b20.fonk6()
    def fonk13(self):
        self.b20.fonk7(self.b10.fonk19())
class class4:
    def fonk14(self, b11, b12):
        self.b11 = b11
        self.b12 = b12
        self.b20 = [[False] * b12 for _ in range(b11)]
    def fonk15(self, b16, b19):
        self.fonk16(b16, b19)
        if b16 > 0:
            self.fonk16(b16 - 1, b19)
        if b16 < self.b11 - 1:
            self.fonk16(b16 + 1, b19)
        if b19 > 0:
            self.fonk16(b16, b19 - 1)
        if b19 < self.b12 - 1:
            self.fonk16(b16, b19 + 1)
    def fonk16(self, b16, b19):
        self.b20[b16][b19] = not self.b20[b16][b19]
    def fonk17(self):
        return self.b20
    def fonk18(self):
        for _ in range(self.b11 * self.b12 * 3):
            b16 = random.randint(0, self.b11 - 1)
            b19 = random.randint(0, self.b12 - 1)
            self.fonk15(b16, b19)
    def fonk19(self):
        return []
if b24 = = "__main__":
    b25 = tk.Tk()
    b25.title("Lights Out")
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <b11> <b12>")
        sys.exit(1)
    b11, b12 = map(int, sys.argv[1:])
    class3(b25, b11, b12).pack()
    b25.resizable(b6 = False, width=False)
    b25.mainloop()