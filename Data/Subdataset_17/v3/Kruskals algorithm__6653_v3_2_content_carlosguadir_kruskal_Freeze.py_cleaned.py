from cx_Freeze import setup, Executable
setup(
    name="Ventana",
    version="0.1",
    description="Ventana - Maritime Routes Application",
    executables=[Executable("RutasMaritimas.py")],
)