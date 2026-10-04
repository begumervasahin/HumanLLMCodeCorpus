import numpy as np
import sys
def leerArchivo(nombreArchivo, columnas, filas):
    arreglo = []
    try:
        archivo = open(nombreArchivo,"r")
        for linea in archivo:
            linea_nueva =linea.split(",")
            for i in range(len(filas)):
                for j in range(len(columnas)):
                    arreglo.append(linea_nueva)
        archivo.close()
    except(FileNotFoundError):
        print("Archivo No encontrado")
    except(ValueError):
        print("Error en los tipos-valores de datos")
    return arreglo
arhivoAExtraer = input("Digite el nombre del archivo a leer junto con su extensiÃ³n siendo esta (.txt)\n")
filas = input("Digite la cantidad de elementos por oraciÃ³n en el archivo (.txt)\n")
columnas = input("Digite el numero de oraciones que posee el (.txt)\n")
matriz = leerArchivo(arhivoAExtraer,columnas,filas)
print("Matriz solicitada orden NxM")
matriz_con_corchetas = np.matrix(matriz)
matriz_sin_corchetas = str(matriz_con_corchetas)[1:-1]
print (matriz_sin_corchetas)
print()