from fonction import *
def fonk1(file_path):
    a1 = 0
    b1 = CREATION_histoGains()
    with open(file_path, 'r', b2 = "utf-8") as file:
        for line in file:
            a1 += 1
            b3 = list(map(int, line.rstrip().split(";")))
            for i, value in enumerate(b3):
                b1[i][1] += value
    return a1, b1
def fonk2(b8, num_data, b9):
    print(f"Méthode avec nombres {b8}")
    print(f"{num_data} simulations de {NB_TIRAGE_SIMULE} tirages.\n")
    AFFICHE_histogrammeGains(b9)
    b4 = num_data * NB_TIRAGE_SIMULE * MISE
    b5 = CALCUL_gains(b9)
    b6 = b5 - b4
    b7 = b6 / (NB_TIRAGE_SIMULE * num_data)
    print(f"\nSoit un coût de {b4}")
    print(f"Pour un gain de {b5}\n")
    print(f"Au final : {b6}")
    print(f"Espérance : {b7}\n")
def fonk3():
    for analysis in LISTE_ANALYSE:
        file_path, b8 = analysis
        num_data, b9 = fonk1(file_path)
        fonk2(b8, num_data, b9)
if b10 = = "__main__":
    fonk3()