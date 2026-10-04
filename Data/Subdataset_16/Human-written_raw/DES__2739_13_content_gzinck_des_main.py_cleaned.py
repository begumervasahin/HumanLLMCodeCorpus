from cli.menus.main_menu import main_menu
import global_settings
from tempfile import TemporaryDirectory
global_settings.initialize()
b1 = [main_menu]
b2 = []
with TemporaryDirectory() as temp_dir:
    while len(b1) > 0:
        b3 = b1[-1]
        b3(b1, b2, temp_dir)