import sys
import tkinter as tk
import UninformedSearch
class class1(tk.Canvas):
    b1 = "white"
    b2 = "gray50"
    b3 = "red"
    b4 = "black"
    def fonk1(self, master, b5 = 60):
        super().fonk11(master, b6 = b5, width=b5,
                         b7 = self.b2, highlightthickness=2,
                         b8 = self.b4)
    def fonk2(self, state):
        b9 = self.b1 if state else self.b2
        self.configure(b7 = b9)
    def fonk3(self, selected):
        b9 = self.b3 if selected else self.b4
        self.configure(b8 = b9)
class class2(tk.Frame):
    def fonk4(self, master, b10, b11, b12):
        super().fonk11(master)
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
        self.b10.perform_move(b16, b19)
        self.fonk6()
    def fonk6(self):
        b17 = self.b10.get_board()
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
                self.b10.perform_move(b16, b19)
                self.fonk6()
                self.after(b18, stage_3)
            def fonk10():
                self.fonk7(moves[1:], b18 = b18)
            fonk8()
class class3(tk.Frame):
    def fonk11(self, master, b11, b12):
        super().fonk11(master)
        self.b10 = UninformedSearch.create_puzzle(b11, b12)
        self.b20 = class2(self, self.b10, b11, b12)
        self.b20.pack(b21 = tk.LEFT, padx=1, pady=1)
        b22 = tk.Frame(self)
        tk.Button(b22, b23 = "Scramble", command=self.scramble_click).pack(fill=tk.X, padx=1, pady=1)
        tk.Button(b22, b23 = "Solve", command=self.solve_click).pack(fill=tk.X, padx=1, pady=1)
        b22.pack(b21 = tk.RIGHT)
    def fonk12(self):
        self.b10.scramble()
        self.b20.fonk6()
    def fonk13(self):
        self.b20.fonk7(self.b10.find_solution())
def fonk14():
    b24 = tk.Tk()
    b24.title("Lights Out")
    try:
        b11, b12 = sys.argv[1:]
    except ValueError:
        print("Usage: python script.py <b11> <b12>")
        sys.exit(1)
    class3(b24, int(b11), int(b12)).pack()
    b24.resizable(b6 = False, width=False)
    b24.mainloop()
if b25 = = "__main__":
    fonk14()