import tkinter as tk
import tkinter.messagebox
import os
from sympy.ntheory import isprime
def fonk1(b10, b11, b1):
    if not (b10.isdigit() and b11.isdigit() and b1.isdigit()):
        return "Todos os valores devem ser nÃºmeros inteiros."
    b10, b11, b1 = int(b10), int(b11), int(b1)
    if not (isprime(b10) and isprime(b11)):
        return "b10 b1 b11 devem ser nÃºmeros primos."
    if not (1 < b1 < (b10 - 1) * (b11 - 1)):
        return "b1 deve estar no intervalo (1, (b10-1)*(b11-1))."
    return ""
class class1(tk.Frame):
    def fonk2(self, master):
        super().fonk2(master)
        self.fonk3()
    def fonk3(self):
        tk.Label(self, b2 = "Gerar chave publica", font=('Verdana', 22)).pack(b16="top", fill="b7")
        tk.Label(self, b2 = "Insira os valores abaixo", font=('Verdana', 10)).pack(b16="top", fill="b7")
        for _ in range(5):
            tk.Label(self, b2 = "", font=('Verdana', 22)).pack(b16="top", fill="b7")
        self.fonk4("b10:", 80, 65)
        self.fonk4("b11:", 80, 90)
        self.fonk4("b1:", 80, 115)
        self.b3 = self.fonk5(100, 65)
        self.b4 = self.fonk5(100, 90)
        self.b5 = self.fonk5(100, 115)
        b6 = tk.Button(self, b2="Gerar chave", command=self.generate_key)
        b6.pack()
        b6.place(b7 = 95, y=145)
    def fonk4(self, b2, b7, y):
        b8 = tk.Label(self, b2=b2)
        b8.pack()
        b8.place(b7 = b7, y=y)
    def fonk5(self, b7, y):
        b9 = tk.Entry(self)
        b9.pack()
        b9.place(b7 = b7, y=y)
        return b9
    def fonk6(self):
        b10 = self.b3.get()
        b11 = self.b4.get()
        b1 = self.b5.get()
        b12 = fonk1(b10, b11, b1)
        b13 = "ERRO!" if b12 else "Concluido"
        if not b12:
            if os.path.exists("chavePublica.txt"):
                os.remove("chavePublica.txt")
            with open("chavePublica.txt", "w") as file:
                file.write(str((int(b10) * int(b11), int(b1))))
            b12 = "Chave Gerada com Sucesso!"
        tk.messagebox.showinfo(b13, b12)
if b14 = = "__main__":
    b15 = tk.Tk()
    b15.geometry("300x200")
    class1(b15).pack(b16 = "top", fill="both", expand=True)
    b15.mainloop()