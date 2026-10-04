from cli.menus.main_menu import main_menu
import global_settings
from tempfile import TemporaryDirectory
global_settings.initialize()
screens = [main_menu]
automata = []
with TemporaryDirectory() as temp_dir:
    while len(screens) > 0:
        next_screen = screens[-1]
        next_screen(screens, automata, temp_dir)