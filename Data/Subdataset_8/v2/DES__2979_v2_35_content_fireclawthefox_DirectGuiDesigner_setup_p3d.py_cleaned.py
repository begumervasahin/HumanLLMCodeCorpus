import sys
from setuptools import setup
include_patterns = [
    "**/fonts/*",
    "**/icons/*.png",
    "**/LICENSE",
    "**/models/**",
]
platform_tags = {
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
python_version = sys.version_info
linux64 = platform_tags.get((python_version.major, python_version.minor), "manylinux1_x86_64")
mac64 = "macosx_10_6_x86_64"
win64 = "win_amd64"
setup(
    name="DirectGuiDesigner",
    author="Fireclaw the Fox",
    author_email="info@grimfang-studio.org",
    options={
        "build_apps": {
            "include_patterns": include_patterns,
            "gui_apps": {
                "directguidesigner": "main.py",
            },
            "plugins": [
                "pandagl",
            ],
            "platforms": [
                linux64,
                win64,
            ],
            "package_data_dirs": {
                "DirectFolderBrowser": [
                    ("DirectFolderBrowser/icons*", "", {}),
                ],
            },
        }
    }
)