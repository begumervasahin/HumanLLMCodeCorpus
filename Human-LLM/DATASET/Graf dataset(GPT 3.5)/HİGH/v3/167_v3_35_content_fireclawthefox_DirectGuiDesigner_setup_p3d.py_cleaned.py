import sys
from setuptools import setup
b1 = [
    "**/fonts/*",
    "**/icons/*.png",
    "**/LICENSE",
    "**/models/**",
]
b2 = sys.version_info
b3 = (b2.major, b2.minor)
b4 = {
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
b5 = b4.get(b3, "manylinux1_x86_64")
b6 = "macosx_10_6_x86_64"
b7 = "win_amd64"
setup(
    b8 = "DirectGuiDesigner",
    b9 = "Fireclaw the Fox",
    b10 = "info@grimfang-studio.org",
    b11 = {
        "build_apps": {
            "b1": b1,
            "gui_apps": {
                "directguidesigner": "main.py",
            },
            "plugins": [
                "pandagl",
            ],
            "platforms": [
                b5,
                b7,
            ],
            "package_data_dirs": {
                "DirectFolderBrowser": [
                    ("DirectFolderBrowser/icons*", "", {}),
                ],
            },
        }
    }
)