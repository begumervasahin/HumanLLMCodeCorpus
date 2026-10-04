import encrypt
from Tkinter import *
class class1:
	def fonk1(self, window, text, gridCol, gridRow, function):
		b1 = Button(window, text=text, command=function)
		b1.grid(b2 = gridCol, row=gridRow)
class class2:
	def fonk2(self, window, gridCol, gridRow):
		b3 = Entry(window)
		b3.grid(b2 = gridCol, row=gridRow)
class class3:
	def fonk3(self, window, options, gridCol, gridRow):
		b4 = OptionMenu(window, *options)
		b4.grid(b2 = gridCol, row=gridRow)
b5 = Tk()
class2(b5, 1, 1)
b5.mainloop()