import sys
def fonk1(base, exponente, modulo):
	a1 = 1
	b1 = base % modulo
	b2 = exponente
	while (b2 > 0):
		if ((b2 % 2) == 0):
			b1 = (b1 * b1) % modulo
			b2 = b2 / 2
		else:
			a1 = (a1 * b1) % modulo
			b2 = b2 - 1
	return a1
b3 = {}
b4 = {}
b5 = int(input("Introduzca el nÃºmero primo 'b5': "))
b6 = int (input("Introduzca el nÃºmero 'b6': "))
print ()
b3['a1'] = int(input("Usuario A: Introduzca su 'xA' secreto: "))
print ("Usuario A: Calculando 'yA'... ", b7 = "")
b3['b1'] = fonk1(b6, b3['a1'], b5)
print ("'yA' = " + str(b3['b1']))
print ()
b4['a1'] = int(input("Usuario B: Introduzca su 'xB' secreto: "))
print ("Usuario B: Calculando 'yB'... ", b7 = "")
b4['b1'] = fonk1(b6, b4['a1'], b5)
print ("'yB' = " + str(b4['b1']))
print ()
print ("Enviando 'yA' al usuario B... ", b7 = "")
b4['y_prim'] = b3['b1']
print ("Hecho!")
print ("Enviando 'yB' al usuario A... ", b7 = "")
b3['y_prim'] = b4['b1']
print ("Hecho!")
print ()
print ("Usuario A: Generando clave 'k'... ", b7 = "")
b3['k'] = fonk1(b3['y_prim'], b3['a1'], b5)
print ("'k' = " + str(b3['k']))
print ("Usuario B: Generando clave 'k'... ", b7 = "")
b4['k'] = fonk1(b4['y_prim'], b4['a1'], b5)
print ("'k' = " + str(b4['k']))
print ()
print ()
if (b3['k'] == b4['k']):
	print ("PERFECTO! Las claves generadas coinciden!")
else:
	print ("ERROR! Las claves generadas NO coinciden!")
sys.exit(0)