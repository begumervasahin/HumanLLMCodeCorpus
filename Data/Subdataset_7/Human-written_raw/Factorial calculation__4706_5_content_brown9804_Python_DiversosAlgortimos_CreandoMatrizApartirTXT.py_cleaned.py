import numpy as np
import sys
def fonk1(nombreArchivo, b6, b5):
    b1 = []
    try:
        b2 = open(nombreArchivo,"r")
        for linea in b2:
            b3 = linea.split(",")
            for i in range(len(b5)):
                for j in range(len(b6)):
                    b1.append(b3)
        b2.close()
    except(FileNotFoundError):
        print("Archivo No encontrado")
    except(ValueError):
        print("Error en los tipos-valores de datos")
    return b1
b4 = input("Digite el nombre del b2 a leer junto con su extensiÃ³n siendo esta (.txt)\n")
b5 = input("Digite la cantidad de elementos por oraciÃ³n en el b2 (.txt)\n")
b6 = input("Digite el numero de oraciones que posee el (.txt)\n")
b7 = fonk1(b4,b6,b5)
print("Matriz solicitada orden NxM")
b8 = np.matrix(b7)
b9 = str(b8)[1:-1]
print (b9)
print()