from fonction import *
def process_file(file_path):
    nb_donnees = 0
    histo_complet = CREATION_histoGains()
    with open(file_path, 'r', encoding="utf-8") as fichier_courant:
        for ligne in fichier_courant:
            nb_donnees += 1
            ligne_tempo = list(map(int, ligne.rstrip().split(";")))
            for i, value in enumerate(ligne_tempo):
                histo_complet[i][1] += value
    return nb_donnees, histo_complet
def display_results(methode, nb_donnees, histo_complet):
    print(f"Méthode avec nombres {methode}")
    print(f"{nb_donnees} simulations de {NB_TIRAGE_SIMULE} tirages.\n")
    AFFICHE_histogrammeGains(histo_complet)
    cout_total = nb_donnees * NB_TIRAGE_SIMULE * MISE
    gain_total = CALCUL_gains(histo_complet)
    resultat_final = gain_total - cout_total
    esperance = resultat_final / (NB_TIRAGE_SIMULE * nb_donnees)
    print(f"\nSoit un coût de {cout_total}")
    print(f"Pour un gain de {gain_total}\n")
    print(f"Au final : {resultat_final}")
    print(f"Espérance : {esperance}\n")
def main():
    for analyse in LISTE_ANALYSE:
        file_path, methode = analyse
        nb_donnees, histo_complet = process_file(file_path)
        display_results(methode, nb_donnees, histo_complet)
if __name__ == "__main__":
    main()