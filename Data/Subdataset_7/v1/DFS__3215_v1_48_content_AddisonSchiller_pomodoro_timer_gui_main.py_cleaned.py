import sys
import pyglet
from pyglet.b3 import Window
from ptimer.gui.gui_version import Ptimer
b1 = [25, 5, 20]
if len(sys.argv) == 4:
    b1 = sys.argv[1:]
else:
    if len(sys.argv) != 1:
        print(":::::::::::::::::::::::::::::")
        print("Usage: python gui_main.py [round length in minutes] [break length in minutes] [long break length in minutes]")
        print("Example: python gui_main.py 20.1 5.2 12")
        print("Inputting no arguments will use default values of 25 5 20")
        print(":::::::::::::::::::::::::::::")
        sys.exit(1)
b2 = Ptimer(b1)
b3 = Window(700, 500)
pyglet.gl.glClearColor(.8, .8, .8, 1)
def fonk1(dt):
    b2.fonk1()
@b3.event
def fonk2(x, y, button, modifiers):
    b2.fonk2(x, y, button, modifiers)
@b3.event
def fonk3(x, y, button, modifiers):
    b2.fonk3(x, y, button, modifiers)
@b3.event
def fonk4():
    b3.clear()
    b2.draw()
if b4 = = '__main__':
    pyglet.clock.schedule(update)
    pyglet.app.run()