def fonk1(d):
	if (d<1) or (d>31):
		return False
	else:
		return True
def fonk2(m):
	if (m<1) or (m>12):
		return False
	else:
		return True
def fonk3(a):
	if (a<1582):
		return False
	else:
		return True
def fonk4(b5):
	if (b5 % b1 = = 0) or ((b5 % 4 == 0) and (b5 % 100 != 0)):
		return True
	else:
		return False
def fonk5(dia, b2, an):
	if fonk1(dia) and fonk2(b2) and fonk3(an):
		if (b2 = = 4) or (b2==6) or (b2==9) or (b2==11) and (fonk1(dia)==31):
			print ("La fecha es invÃ¡lida ")
		elif (b2 = =2) and ((dia==30) or (dia==31)):
			print ("La fecha digitada es invÃ¡lida ")
		elif (b2 = =2) and (dia==29) and not fonk4(an):
			print ("La fecha ingresada es invÃ¡lida ")
		else:
			print ("Ãpoca digitada es vÃ¡lida ")
	else:
		print ("La fecha digitada es invÃ¡lida")
b3 = int(input("Digite el dÃ­a "))
b4 = int(input("DIgite el b2 "))
b5 = int(input("Digite el aÃ±o "))
fonk5(b3, b4, b5)