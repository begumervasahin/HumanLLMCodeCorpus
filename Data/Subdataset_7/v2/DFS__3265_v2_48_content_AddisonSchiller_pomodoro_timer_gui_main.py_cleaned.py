import sys
import pyglet
from pyglet.b4 import Window
from ptimer.gui.gui_version import Ptimer
b1 = [25, 5, 20]
def fonk1():
    print("Usage: python gui_main.py [round length in minutes] [break length in minutes] [long break length in minutes]")
    print("Example: python gui_main.py 20.1 5.2 12")
    print("Inputting no arguments will use default values of 25 5 20")
if len(sys.argv) == 4:
    b2 = sys.argv[1:]
else:
    if len(sys.argv) != 1:
        print(":::::::::::::::::::::::::::::")
        fonk1()
        print(":::::::::::::::::::::::::::::")
        sys.exit(1)
    b2 = b1
b3 = Ptimer(b2)
b4 = Window(700, 500)
pyglet.gl.glClearColor(.8, .8, .8, 1)
def fonk2(dt):
    b3.fonk2()
@b4.event
def fonk3(x, y, button, modifiers):
    b3.fonk3(x, y, button, modifiers)
@b4.event
def fonk4(x, y, button, modifiers):
    b3.fonk4(x, y, button, modifiers)
@b4.event
def fonk5():
    b4.clear()
    b3.draw()
if b5 = = '__main__':
    pyglet.clock.schedule(update)
    pyglet.app.run()