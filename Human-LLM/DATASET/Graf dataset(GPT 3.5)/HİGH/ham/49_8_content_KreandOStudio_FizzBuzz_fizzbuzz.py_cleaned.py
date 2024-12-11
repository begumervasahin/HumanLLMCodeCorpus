b1 = None
b2 = None
b3 = True
b4 = True
print "!!!Bienvenidos a FizzBuzz!!! "
while b3:
    try:
        b5 = int(raw_input("Introduzca un nÃºmero del 1 al 100: "))
        if b5 > 0 and b5 <= 100:
            b4 = True
            for b6 in range(1, b5 + 1):
                if b6 = = 3:
                    print "Fizz"
                elif b6 = = 5:
                    print "Buzz"
                elif b6 > 5:
                    b1 = b6 % 3
                    b2 = b6 % 5
                    if b1 = = 0 and b2 == 0:
                        print "FizzBuzz"
                    elif b1 = = 0:
                        print "Fizz"
                    elif b2 = = 0:
                        print "Buzz"
                    else:
                        print b6
                else:
                    print b6
        else:
            print "Por favor, introduzca un nÃºmero vÃ¡lido!"
            b4 = False
    except ValueError:
        print "Por favor, introduzca solo nÃºmeros."
        b4 = False
    while  b4:
        b7 = raw_input("Â¿Desea jugar de nuevo? (S/N): ")[0]
        b7 = b7.upper()
        if b7 = = "S":
            b4 = False
        elif b7 = = "N":
            b4 = False
            b3 = False
        else:
            print "OpciÃ³n incorrecta!"