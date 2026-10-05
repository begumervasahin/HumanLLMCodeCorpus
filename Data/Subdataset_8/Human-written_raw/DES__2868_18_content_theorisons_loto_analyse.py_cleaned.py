from fonction import *
for analyse in LISTE_ANALYSE:
    fichierCourant = open(analyse[0], 'r')
    ligneTempo = []
    nbDonnees = 0
    histoComplet = CREATION_histoGains()
    for ligne in fichierCourant:
        nbDonnees += 1
        ligneTempo = map(int, ligne.rstrip().split(";"))
        for i in range(len(ligneTempo)):
            histoComplet[i][1] += ligneTempo[i]
    print("MÃ©thode avec nombres {}".format(analyse[1]))
    print("{} simulations de {} tirages.\n".format(nbDonnees, NB_TIRAGE_SIMULE))
    AFFICHE_histogrammeGains(histoComplet)
    coutTotal = nbDonnees*NB_TIRAGE_SIMULE*MISE
    gainTotal = CALCUL_gains(histoComplet)
    print("\nSoit un coÃ»t de {}â¬".format(coutTotal))
    print("Pour un gain de {}â¬\n".format(gainTotal))
    print("Au final : {}â¬".format(gainTotal - coutTotal))
    print("EspÃ©rance : {}â¬".format((gainTotal - coutTotal)/(NB_TIRAGE_SIMULE*nbDonnees)))
    print("\n")
    fichierCourant.close()