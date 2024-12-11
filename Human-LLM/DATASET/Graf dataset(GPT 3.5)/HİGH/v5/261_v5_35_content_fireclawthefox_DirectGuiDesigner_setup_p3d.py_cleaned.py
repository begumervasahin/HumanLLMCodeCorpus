import sys
from setuptools import setup
b1 = [
    "**/fonts/*",
    "**/icons/*.png",
    "**/LICENSE",
    "**/models/**",
]
b2 = "manylinux1_x86_64" if sys.version_info < (3, 10) else "manylinux2010_x86_64"
b3 = "macosx_10_6_x86_64"
b4 = "win_amd64"
setup(
    b5 = "DirectGuiDesigner",
    b6 = "Fireclaw the Fox",
    b7 = "info@grimfang-studio.org",
    b8 = {
        "build_apps": {
            "b1": b1,
            "gui_apps": {"directguidesigner": "main.py"},
            "plugins": ["pandagl"],
            "platforms": [b2, b4],
            "package_data_dirs": {"DirectFolderBrowser": [("DirectFolderBrowser/icons*", "", {})]},
        }
    }
)