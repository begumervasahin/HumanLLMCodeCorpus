import tkinter as tk
from funcoesAux import *
import tkinter.messagebox
import os
from sympy.ntheory import isprime
class class1(tk.Frame):
    def fonk1(self, master):
        tk.Frame.fonk1(self, master)
        tk.Label(self, b1 = "Gerar chave publica",
            b2 = ('Verdana', 22)).pack(side="top", fill="b4")
        tk.Label(self, b1 = "Insira os valores abaixo",
            b2 = ('Verdana', 10)).pack(side="top", fill="b4")
        tk.Label(self, b1 = "",
            b2 = ('Verdana', 22)).pack(side="top", fill="b4")
        tk.Label(self, b1 = "",
            b2 = ('Verdana', 22)).pack(side="top", fill="b4")
        tk.Label(self, b1 = "",
            b2 = ('Verdana', 22)).pack(side="top", fill="b4")
        tk.Label(self, b1 = "",
            b2 = ('Verdana', 22)).pack(side="top", fill="b4")
        tk.Label(self, b1 = "",
            b2 = ('Verdana', 22)).pack(side="top", fill="b4")
        b3 = tk.Label(self, b1="b7:")
        b3.pack(); b3.place(b4 = 80, y = 65)
        b5 = tk.Label(self, b1="b8:")
        b5.pack(); b5.place(b4 = 80, y = 90)
        b6 = tk.Label(self, b1="b9:")
        b6.pack(); b6.place(b4 = 80, y = 115)
        b7 = tk.Entry(self)
        b7.pack(); b7.place(b4 = 100, y = 65)
        b8 = tk.Entry(self)
        b8.pack(); b8.place(b4 = 100, y = 90)
        b9 = tk.Entry(self)
        b9.pack(); b9.place(b4 = 100, y = 115)
        def fonk2():
            b11, b10 = pqeValidacao(b7.get(), b8.get(), b9.get()), "ERRO!"
            if(b11 = = ""):
                if os.path.exists("chavePublica.txt"):
                    os.remove("chavePublica.txt")
                b12 = open("chavePublica.txt", "w")
                b12.write(str( (int(b7.get())*int(b8.get()), int(b9.get())) ))
                b12.close()
                b11 = "Chave Gerada com Sucesso!"
                b10 = "Concluido"
            tkinter.messagebox.showinfo(b10, b11)
        b13 = tk.Button(self, b1="Gerar chave", command=gerar)
        b13.pack()
        b13.place(b4 = 95, y=145)