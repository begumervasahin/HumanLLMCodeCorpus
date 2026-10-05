import sys
def fonk1(base, exponente, modulo):
    a1 = 1
    b1 = base % modulo
    b2 = exponente
    while b2 > 0:
        if b2 % b3 = = 0:
            b1 = (b1 * b1) % modulo
            b2 = b2
        else:
            a1 = (a1 * b1) % modulo
            b2 = b2 - 1
    return a1
b4 = {}
b5 = {}
b6 = int(input("Introduzca el número primo 'b6': "))
b7 = int(input("Introduzca el número 'b7': "))
print()
b4['a1'] = int(input("Usuario A: Introduzca su 'xA' secreto: "))
print("Usuario A: Calculando 'yA'... ", b8 = "")
b4['b1'] = fonk1(b7, b4['a1'], b6)
print("'yA' =", b4['b1'])
print()
b5['a1'] = int(input("Usuario B: Introduzca su 'xB' secreto: "))
print("Usuario B: Calculando 'yB'... ", b8 = "")
b5['b1'] = fonk1(b7, b5['a1'], b6)
print("'yB' =", b5['b1'])
print()
print("Enviando 'yA' al usuario B... ", b8 = "")
b5['y_prim'] = b4['b1']
print("Hecho!")
print("Enviando 'yB' al usuario A... ", b8 = "")
b4['y_prim'] = b5['b1']
print("Hecho!")
print()
print("Usuario A: Generando clave 'k'... ", b8 = "")
b4['k'] = fonk1(b4['y_prim'], b4['a1'], b6)
print("'k' =", b4['k'])
print("Usuario B: Generando clave 'k'... ", b8 = "")
b5['k'] = fonk1(b5['y_prim'], b5['a1'], b6)
print("'k' =", b5['k'])
print()
if b4['k'] == b5['k']:
    print("¡PERFECTO! ¡Las claves generadas coinciden!")
else:
    print("¡ERROR! ¡Las claves generadas NO coinciden!")
sys.exit(0)