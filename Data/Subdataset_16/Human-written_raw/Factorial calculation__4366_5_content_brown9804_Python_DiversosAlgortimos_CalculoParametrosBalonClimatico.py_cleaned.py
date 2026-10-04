def fonk1(t):
	b1 = -0.48*(t**3) + 36*(t**2) - 760*t + 4100
	return b1
def fonk2(t):
	b2 = -0.12*t*t*t*t + 12*t*t*t -380*t*t + 4100*t + 220
	return b2
def fonk3(t):
	b3 = t/3600
	return b3
def fonk4(inicio, final, incremen):
	a1 = 0
	a2 = 0
	for indice in range (inicio, final +1, incremen):
		b1 = fonk1(indice)
		b2 = fonk2(indice)
		b4 = fonk3(b1)
		if b2 > a1:
			a1 = b2
			a2 = indice
		print("{0:2}h   {1:8.2f}m       {2:3.2f}m/s".format(indice, b2, b4))
	print("La altura mÃ¡xima se alcanzÃ³ a las", a2, "horas \n Esta altura mÃ¡xima fue de ", a1, "metros")
b5 = int(input("Ingrese el tiempo inicial para calcular la velocidad y la altitud para este balÃ³n climÃ¡tico "))
b6 = int(input("Digite el tiempo final "))
b7 = int(input("Digite el incremento de horas "))
if (b5>=0) and (b6<48):
		fonk4(b5, b6, b7)
else:
	while (b5<0) and (b6>48):
		print("Debe digitar un tiempo inicial mayor o igual a cero y el tiempo final debe ser menor a las 48 horas")
		b5 = int(input("Ingrese el tiempo inicial para calcular la velocidad y la altitud para este balÃ³n climÃ¡tico"))
		b6 = int(input("Digite el tiempo final "))