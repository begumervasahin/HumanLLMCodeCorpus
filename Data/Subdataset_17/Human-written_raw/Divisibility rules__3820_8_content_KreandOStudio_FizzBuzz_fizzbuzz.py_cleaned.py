fizz = None
buzz = None
fizzbuzz = True
correcto = True
print "!!!Bienvenidos a FizzBuzz!!! "
while fizzbuzz:
    try:
        num = int(raw_input("Introduzca un nÃºmero del 1 al 100: "))
        if num > 0 and num <= 100:
            correcto = True
            for i in range(1, num + 1):
                if i == 3:
                    print "Fizz"
                elif i == 5:
                    print "Buzz"
                elif i > 5:
                    fizz = i % 3
                    buzz = i % 5
                    if fizz == 0 and buzz == 0:
                        print "FizzBuzz"
                    elif fizz == 0:
                        print "Fizz"
                    elif buzz == 0:
                        print "Buzz"
                    else:
                        print i
                else:
                    print i
        else:
            print "Por favor, introduzca un nÃºmero vÃ¡lido!"
            correcto = False
    except ValueError:
        print "Por favor, introduzca solo nÃºmeros."
        correcto = False
    while  correcto:
        pregunta = raw_input("Â¿Desea jugar de nuevo? (S/N): ")[0]
        pregunta = pregunta.upper()
        if pregunta == "S":
            correcto = False
        elif pregunta == "N":
            correcto = False
            fizzbuzz = False
        else:
            print "OpciÃ³n incorrecta!"