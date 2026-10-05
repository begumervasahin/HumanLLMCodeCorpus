
print("Bienvenido a la máquina de Atwood. Consiste en dos masas, m1 y m2, conectadas por una cuerda inelástica y una polea ideal de masa despreciable.")
m1 = input("Digite la masa del objeto 1 en kilogramos. Considere que este objeto es el más pesado: ")
m2 = input("Digite la masa del objeto 2 en kilogramos: ")
GRAVITY = 9.81
acceleration = (GRAVITY * (float(m1) - float(m2)) / (float(m1) + float(m2)))
print("Recuerde que la gravedad es 9.81 m/s².")
print("Considerando los datos anteriores, la aceleración es equivalente a: " + str(acceleration) + " m/s².")
tension_newtons = (GRAVITY * 2 * (float(m1) * float(m2)) / (float(m1) + float(m2)))
print("La tensión de la cuerda en Newtons es: " +  str(tension_newtons) + " metros * kg / seg².")
tension_dynes = (GRAVITY * 0.01 * 2 * (float(m1) * float(m2)) * 0.001 / (float(m1) + float(m2)) * 0.001)
print("La tensión en dinas es: " + str(tension_dynes) + " cm * gr / seg².")