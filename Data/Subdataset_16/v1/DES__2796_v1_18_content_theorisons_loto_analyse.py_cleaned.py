from fonction import *
def fonk1():
    for analyse in LISTE_ANALYSE:
        b1 = open(analyse[0], 'r')
        a1 = 0
        b2 = CREATION_histoGains()
        for ligne in b1:
            a1 += 1
            b3 = list(map(int, ligne.rstrip().split(";")))
            for i in range(len(b3)):
                b2[i][1] += b3[i]
        b1.close()
        b4 = analyse[1]
        print(f"Méthode avec nombres {b4}")
        print(f"{a1} simulations de {NB_TIRAGE_SIMULE} tirages.\n")
        AFFICHE_histogrammeGains(b2)
        b5 = a1 * NB_TIRAGE_SIMULE * MISE
        b6 = CALCUL_gains(b2)
        b7 = b6 - b5
        b8 = b7 / (NB_TIRAGE_SIMULE * a1)
        print(f"\nSoit un coût de {b5}")
        print(f"Pour un gain de {b6}\n")
        print(f"Au final : {b7}")
        print(f"Espérance : {b8}")
        print("\n")
if b9 = = "__main__":
    fonk1()