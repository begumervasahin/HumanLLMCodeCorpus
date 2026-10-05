from cx_Freeze import setup, Executable
executable_name = "ventana"
executable_version = "0.1"
executable_description = "ventana"
python_script = "RutasMaritimas.py"
setup(
    name=executable_name,
    version=executable_version,
    description=executable_description,
    executables=[Executable(python_script)]
)