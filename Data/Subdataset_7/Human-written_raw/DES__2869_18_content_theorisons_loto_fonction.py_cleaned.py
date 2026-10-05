from constantes import *
import random as r
def fonk1(grilleJoueur, tirageOfficiel, histoGains, gains):
    a1 = 0
    b1 = False
    for g in range(0, NB_BOULES_NORMALES, 1):
        for t in range(0, NB_BOULES_NORMALES, 1):
            if grilleJoueur[g] == tirageOfficiel[t]:
                a1 += 1
    if grilleJoueur[NB_BOULES_NORMALES] == tirageOfficiel[NB_BOULES_NORMALES]:
        b1 = True
    if (a1 = = 5 and b1):
        histoGains[0][1] += 1
        gains += histoGains[0][0]
    elif (a1 = = 5):
        histoGains[1][1] += 1
        gains += histoGains[1][0]
    elif (a1 = = 4 and b1):
        histoGains[2][1] += 1
        gains += histoGains[2][0]
    elif (a1 = = 4):
        histoGains[3][1] += 1
        gains += histoGains[3][0]
    elif (a1 = = 3 and b1):
        histoGains[4][1] += 1
        gains += histoGains[4][0]
    elif (a1 = = 3):
        histoGains[5][1] += 1
        gains += histoGains[5][0]
    elif (a1 = = 2 and b1):
        histoGains[6][1] += 1
        gains += histoGains[6][0]
    elif (a1 = = 2):
        histoGains[7][1] += 1
        gains += histoGains[7][0]
    elif (a1 = = 1 and b1):
        histoGains[8][1] += 1
        gains += histoGains[8][0]
    elif (b1):
        histoGains[8][1] += 1
        gains += histoGains[8][0]
    return(histoGains, gains)
def fonk2():
    b2 = [
        [JACKPOT, 0],
        [100000, 0],
        [1000, 0],
        [500, 0],
        [50, 0],
        [20, 0],
        [10, 0],
        [5, 0],
        [MISE, 0],
    ]
    return(b2)
def fonk3(tirageOfficiel, histoBoules):
    for b9 in range(0, NB_BOULES_NORMALES, 1):
        histoBoules[0][tirageOfficiel[b9]-1][1] += 1
    histoBoules[1][tirageOfficiel[NB_BOULES_NORMALES]-1][1] += 1
    return(histoBoules)
def fonk4():
    b3 = [
        [[b9, 0] for b9 in range(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL + 1, 1)],
        [[b9, 0] for b9 in range(NUM_BOULE_MIN, NUM_BOULE_MAX_COMP + 1, 1)]
    ]
    return(b3)
def fonk5(histoBoules):
    b4 = []
    b4 += [[[b9[0], b9[1]] for b9 in histoBoules[0]]]
    b4 += [[[b9[0], b9[1]] for b9 in histoBoules[1]]]
    b4[0].sort(b5 = gestionTrieHisto, reverse=True)
    b4[1].sort(b5 = gestionTrieHisto, reverse=True)
    return(b4)
def fonk6(val):
    return(val[1])
def fonk7(b4):
    b6 = []
    b7 = []
    for b9 in range(0, NB_BOULES_NORMALES, 1):
        b6 += [b4[0][b9][0]]
    b6 += [b4[1][0][0]]
    for b9 in range(NUM_BOULE_MAX_NORMAL-1, NUM_BOULE_MAX_NORMAL - 1 - NB_BOULES_NORMALES, -1):
        b7 += [b4[0][b9][0]]
    b7 += [b4[1][NUM_BOULE_MAX_COMP-1][0]]
    return(b6, b7)
def fonk8():
    a2 = 0
    b8 = []
    for b9 in range(0, NB_BOULES_NORMALES, 1):
        a2 = r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL)
        while fonk9(b8, a2):
            a2 = r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL)
        b8 += [a2]
    b8 += [r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_COMP)]
    return(b8)
def fonk9(grille, numero):
    for b9 in grille:
        if b9 = = numero:
            return(True)
    return(False)
def fonk10(nomFichier):
    b10 = []
    b11 = open(nomFichier, "r")
    for ligne in b11:
        b10 += [[
            map(int, ligne.rstrip().split(";")[:6]),
            ligne.rstrip().split(";")[6]
        ]]
    b11.close()
    return(b10)
def fonk11(histoGains):
    a3 = 0
    for b9 in histoGains:
        a3 += b9[0]*b9[1]
    return(a3)
def fonk12(histoGains, nomFichier):
    b12 = open(nomFichier, "a")
    b12.write("{};{};{};{};{};{};{};{};{}\n".format(
        histoGains[0][1],
        histoGains[1][1],
        histoGains[2][1],
        histoGains[3][1],
        histoGains[4][1],
        histoGains[5][1],
        histoGains[6][1],
        histoGains[7][1],
        histoGains[8][1])
    )
    b12.close()
def fonk13(histoGains, b13 = ""):
    print("{}{} -> {}".format(b13, histoGains[0][0], histoGains[0][1]))
    print("{} {} -> {}".format(b13, histoGains[1][0], histoGains[1][1]))
    print("{}   {} -> {}".format(b13, histoGains[2][0], histoGains[2][1]))
    print("{}    {} -> {}".format(b13, histoGains[3][0], histoGains[3][1]))
    print("{}     {} -> {}".format(b13, histoGains[4][0], histoGains[4][1]))
    print("{}     {} -> {}".format(b13, histoGains[5][0], histoGains[5][1]))
    print("{}     {} -> {}".format(b13, histoGains[6][0], histoGains[6][1]))
    print("{}      {} -> {}".format(b13, histoGains[7][0], histoGains[7][1]))
    print("{}    {} -> {}".format(b13, histoGains[8][0], histoGains[8][1]))
def fonk14(grille):
    b14 = sorted(grille[:NB_BOULES_NORMALES]) + \
        [grille[NB_BOULES_NORMALES]]
    print("{} {} {} {} {} + {} ".format(b14[0], b14[1],
                                        b14[2], b14[3], b14[4], b14[5]))