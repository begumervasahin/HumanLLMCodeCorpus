import sys
from setuptools import setup
b1 = [
    "**/fonts/*",
    "**/icons/*.png",
    "**/LICENSE",
    "**/models/**",
]
b2 = {
    (3, 10): "manylinux2010_x86_64",
    (3, 9): "manylinux1_x86_64",
    (3, 8): "manylinux1_x86_64",
    (3, 7): "manylinux1_x86_64",
    (3, 6): "manylinux1_x86_64",
    (3, 5): "manylinux1_x86_64",
    (3, 4): "manylinux1_x86_64",
    (3, 3): "manylinux1_x86_64",
    (3, 2): "manylinux1_x86_64",
    (3, 1): "manylinux1_x86_64",
    (3, 0): "manylinux1_x86_64",
    (2, 7): "manylinux1_x86_64",
}
b3 = sys.version_info
b4 = b2.get((b3.major, b3.minor), "manylinux1_x86_64")
b5 = "macosx_10_6_x86_64"
b6 = "win_amd64"
setup(
    b7 = "DirectGuiDesigner",
    b8 = "Fireclaw the Fox",
    b9 = "info@grimfang-studio.org",
    b10 = {
        "build_apps": {
            "b1": b1,
            "gui_apps": {
                "directguidesigner": "main.py",
            },
            "plugins": [
                "pandagl",
            ],
            "platforms": [
                b4,
                b6,
            ],
            "package_data_dirs": {
                "DirectFolderBrowser": [
                    ("DirectFolderBrowser/icons*", "", {}),
                ],
            },
        }
    }
)