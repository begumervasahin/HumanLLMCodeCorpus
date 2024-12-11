from fonction import *
for analyse in LISTE_ANALYSE:
    b1 = open(analyse[0], 'r')
    b2 = []
    a1 = 0
    b3 = CREATION_histoGains()
    for ligne in b1:
        a1 += 1
        b2 = map(int, ligne.rstrip().split(";"))
        for i in range(len(b2)):
            b3[i][1] += b2[i]
    print("MÃ©thode avec nombres {}".format(analyse[1]))
    print("{} simulations de {} tirages.\n".format(a1, NB_TIRAGE_SIMULE))
    AFFICHE_histogrammeGains(b3)
    b4 = a1*NB_TIRAGE_SIMULE*MISE
    b5 = CALCUL_gains(b3)
    print("\nSoit un coÃ»t de {}â¬".format(b4))
    print("Pour un gain de {}â¬\n".format(b5))
    print("Au final : {}â¬".format(b5 - b4))
    print("EspÃ©rance : {}â¬".format((b5 - b4)/(NB_TIRAGE_SIMULE*a1)))
    print("\n")
    b1.close()