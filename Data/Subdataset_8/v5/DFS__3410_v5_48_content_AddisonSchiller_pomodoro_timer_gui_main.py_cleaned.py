import sys
import pyglet
from pyglet.window import Window
from ptimer.gui.gui_version import Ptimer
DEFAULT_TIME_SETTINGS = [25, 5, 20]
def display_usage_instructions():
    print(":::::::::::::::::::::::::::::")
    print("Usage: python gui_main.py [round length in minutes] [break length in minutes] [long break length in minutes]")
    print("Example: python gui_main 20.1 5.2 12")
    print("Inputting no arguments will use default values of 25 5 20")
    print(":::::::::::::::::::::::::::::")
if len(sys.argv) == 4:
    time_settings = sys.argv[1:]
else:
    if len(sys.argv) != 1:
        display_usage_instructions()
        sys.exit(1)
    time_settings = DEFAULT_TIME_SETTINGS
timer = Ptimer(time_settings)
window = Window(700, 500)
pyglet.gl.glClearColor(0.8, 0.8, 0.8, 1)
def update(dt):
    timer.update()
@window.event
def on_mouse_release(x, y, button, modifiers):
    timer.on_mouse_release(x, y, button, modifiers)
@window.event
def on_mouse_press(x, y, button, modifiers):
    timer.on_mouse_press(x, y, button, modifiers)
@window.event
def on_draw():
    window.clear()
    timer.draw()
if __name__ == '__main__':
    pyglet.clock.schedule(update)
    pyglet.app.run()