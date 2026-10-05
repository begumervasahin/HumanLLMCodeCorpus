
print("Bienvenido a la máquina de Atwood. Este dispositivo consta de dos objetos, m1 y m2, conectados por una cuerda inelástica y una polea ideal de masa despreciable.")
m1 = input("Digite la masa del objeto 1 en kilogramos. Tenga en cuenta que este objeto es el más pesado: ")
m2 = input("Digite la masa del objeto 2 en kilogramos: ")
gravity = 9.81
acceleration = (gravity * (float(m1) - float(m2)) / (float(m1) + float(m2)))
print("Recuerde que la aceleración debido a la gravedad es de 9.81 m/s².")
print("Dado lo anterior, la aceleración resultante es: " + str(acceleration) + " m/s².")
tension_newtons = (gravity * 2 * (float(m1) * float(m2)) / (float(m1) + float(m2)))
print("La tensión en la cuerda, expresada en Newtons, es: " + str(tension_newtons) + " metros * kg / seg².")
tension_dynes = (gravity * 0.01 * 2 * (float(m1) * float(m2)) * 0.001 / (float(m1) + float(m2)) * 0.001)
print("La tensión, expresada en dinas, es: " + str(tension_dynes) + " cm * gr / seg².")