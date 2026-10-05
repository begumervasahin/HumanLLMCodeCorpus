import sys
import pyglet
from pyglet.window import Window
from ptimer.gui.gui_version import Ptimer
DEFAULT_TIME_SETTINGS = [25, 5, 20]
def display_usage():
    print("Usage: python gui_main.py [round length in minutes] [break length in minutes] [long break length in minutes]")
    print("Example: python gui_main.py 20.1 5.2 12")
    print("Inputting no arguments will use default values of 25 5 20")
def initialize_timer(time_settings):
    return Ptimer(time_settings)
def create_window(width, height):
    return Window(width, height)
def update_timer(dt):
    timer.update()
def handle_mouse_release(x, y, button, modifiers):
    timer.on_mouse_release(x, y, button, modifiers)
def handle_mouse_press(x, y, button, modifiers):
    timer.on_mouse_press(x, y, button, modifiers)
def draw_window():
    window.clear()
    timer.draw()
def run_application():
    pyglet.clock.schedule(update_timer)
    pyglet.app.run()
if __name__ == '__main__':
    if len(sys.argv) == 4:
        time_settings = sys.argv[1:]
    else:
        if len(sys.argv) != 1:
            print(":::::::::::::::::::::::::::::")
            display_usage()
            print(":::::::::::::::::::::::::::::")
            sys.exit(1)
        time_settings = DEFAULT_TIME_SETTINGS
    timer = initialize_timer(time_settings)
    window = create_window(700, 500)
    pyglet.gl.glClearColor(.8, .8, .8, 1)
    window.on_mouse_release = handle_mouse_release
    window.on_mouse_press = handle_mouse_press
    window.on_draw = draw_window
    run_application()