from fonction import *
for analyse in LISTE_ANALYSE:
    with open(analyse[0], 'r') as fichierCourant:
        a1 = 0
        b1 = CREATION_histoGains()
        for ligne in fichierCourant:
            a1 += 1
            b2 = map(int, ligne.rstrip().split(";"))
            for i in range(len(b2)):
                b1[i][1] += b2[i]
        print("Method with numbers: {}".format(analyse[1]))
        print("{} simulations of {} draws.\n".format(a1, NB_TIRAGE_SIMULE))
        AFFICHE_histogrammeGains(b1)
        b3 = a1 * NB_TIRAGE_SIMULE * MISE
        b4 = CALCUL_gains(b1)
        print("\nTotal cost: {}".format(b3))
        print("Total gain: {}\n".format(b4))
        print("Net profit: {}".format(b4 - b3))
        print("Expectation: {}".format((b4 - b3) / (NB_TIRAGE_SIMULE * a1)))
        print("\n")
exit()