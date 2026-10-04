from cx_Freeze import setup, Executable
setup(
    b1 = "ventana",
    b2 = "0.1",
    b3 = "Ventana - Maritime Routes Application",
    b4 = [Executable("RutasMaritimas.py")]
)