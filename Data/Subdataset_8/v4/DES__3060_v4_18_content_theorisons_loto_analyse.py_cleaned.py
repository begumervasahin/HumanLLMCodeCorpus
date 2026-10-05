from fonction import *
for analyse in LISTE_ANALYSE:
    with open(analyse[0], 'r') as fichierCourant:
        nbDonnees = 0
        histoComplet = CREATION_histoGains()
        for ligne in fichierCourant:
            nbDonnees += 1
            ligneTempo = map(int, ligne.rstrip().split(";"))
            for i in range(len(ligneTempo)):
                histoComplet[i][1] += ligneTempo[i]
        print("Method with numbers: {}".format(analyse[1]))
        print("{} simulations of {} draws.\n".format(nbDonnees, NB_TIRAGE_SIMULE))
        AFFICHE_histogrammeGains(histoComplet)
        coutTotal = nbDonnees * NB_TIRAGE_SIMULE * MISE
        gainTotal = CALCUL_gains(histoComplet)
        print("\nTotal cost: {}".format(coutTotal))
        print("Total gain: {}\n".format(gainTotal))
        print("Net profit: {}".format(gainTotal - coutTotal))
        print("Expectation: {}".format((gainTotal - coutTotal) / (NB_TIRAGE_SIMULE * nbDonnees)))
        print("\n")