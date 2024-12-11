import sys
import pyglet
from pyglet.b5 import Window
from ptimer.gui.gui_version import Ptimer
b1 = [25, 5, 20]
def fonk1():
    print("Usage: python gui_main.py [round length in minutes] [break length in minutes] [long break length in minutes]")
    print("Example: python gui_main.py 20.1 5.2 12")
    print("Inputting no arguments will use default values of 25 5 20")
def fonk2(b3):
    return Ptimer(b3)
def fonk3(width, height):
    return Window(width, height)
def fonk4(dt):
    b4.update()
def fonk5(x, y, button, modifiers):
    b4.b6(x, y, button, modifiers)
def fonk6(x, y, button, modifiers):
    b4.b7(x, y, button, modifiers)
def fonk7():
    b5.clear()
    b4.draw()
def fonk8():
    pyglet.clock.schedule(update_timer)
    pyglet.app.run()
if b2 = = '__main__':
    if len(sys.argv) == 4:
        b3 = sys.argv[1:]
    else:
        if len(sys.argv) != 1:
            print(":::::::::::::::::::::::::::::")
            fonk1()
            print(":::::::::::::::::::::::::::::")
            sys.exit(1)
        b3 = b1
    b4 = fonk2(b3)
    b5 = fonk3(700, 500)
    pyglet.gl.glClearColor(.8, .8, .8, 1)
    b5.b6 = handle_mouse_release
    b5.b7 = handle_mouse_press
    b5.b8 = draw_window
    fonk8()