
print("Bienvenido a la máquina de Atwood. Consiste en dos masas, m1 y m2, conectadas por una cuerda inelástica y una polea ideal de masa despreciable.")
m1 = input("Digite la masa del objeto 1 en kilogramos. Considere que este objeto es el más pesado: ")
m2 = input("Digite la masa del objeto 2 en kilogramos: ")
g = 9.81
aceleracion = (g * (float(m1) - float(m2)) / (float(m1) + float(m2)))
print("Recuerde que la gravedad es 9.81 m/s².")
print("Considerando los datos anteriores, la aceleración es equivalente a: " + str(aceleracion) + " m/s².")
tension = (g * 2 * (float(m1) * float(m2)) / (float(m1) + float(m2)))
print("La tensión de la cuerda en Newtons es: " +  str(tension) + " metros * kg / seg².")
tension_dinas = (g * 0.01 * 2 * (float(m1) * float(m2)) * 0.001 / (float(m1) + float(m2)) * 0.001)
print("La tensión en dinas es: " + str(tension_dinas) + " cm * gr / seg².")