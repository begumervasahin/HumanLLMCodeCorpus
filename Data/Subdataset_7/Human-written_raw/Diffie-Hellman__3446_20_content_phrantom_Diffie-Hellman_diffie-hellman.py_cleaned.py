from Crypto.Util.number import getPrime
from random import randint
"
print ()
a1 = 2
b1 = getPrime(1024)
print ("Generador :", +a1)
print ("Nro primo : ", + b1)
b2 = randint(b1/2,b1-1)
b3 = randint(b1/2,b1-1)
b4 = pow(a1,b2,b1)
b5 = pow(a1,b3,b1)
b6 = pow(b5,b2,b1)
b7 = pow(b4,b3,b1)
assert(b6 = = b7)
print ("\nNro publico de b4 : ",+ b4)
print ("Nro publico de b5 : ", + b5)
print ("\nShared secret b4: ", + b6)
print ("Shared secret b5: ", + b7)
"""
Paso 1) El usuario "b2" le tiene que enviar al usuario "b3":
		"a1", "b1" y "b4" (nro publico)
Paso 2) El usuario "b3" le envia al usuario "b2":
		"b5" (nro publico)
Paso 3) Cada uno calcula el shared secret y obtienen la misma llave :-D
"""