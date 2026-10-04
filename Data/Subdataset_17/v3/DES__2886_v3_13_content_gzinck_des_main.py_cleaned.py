from cli.menus.main_menu import main_menu
import global_settings
from tempfile import TemporaryDirectory
def run_des_application():
    global_settings.initialize()
    screens = [main_menu]
    automata = []
    with TemporaryDirectory() as temp_dir:
        while screens:
            current_screen = screens.pop()
            current_screen(screens, automata, temp_dir)
if __name__ == "__main__":
    run_des_application()