from cx_Freeze import setup, Executable
setup(
    b1 = "ventana",
    b2 = "0.1",
    b3 = "Script for ventana",
    b4 = [Executable("RutasMaritimas.py")]
)