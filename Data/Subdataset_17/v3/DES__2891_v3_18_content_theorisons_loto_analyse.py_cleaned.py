from fonction import *
def process_file(file_path):
    nb_donnees = 0
    histo_complet = CREATION_histoGains()
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            nb_donnees += 1
            values = map(int, line.rstrip().split(";"))
            for i, value in enumerate(values):
                histo_complet[i][1] += value
    return nb_donnees, histo_complet
def display_results(method, num_data, histogram):
    print(f"Méthode avec nombres {method}")
    print(f"{num_data} simulations de {NB_TIRAGE_SIMULE} tirages.\n")
    AFFICHE_histogrammeGains(histogram)
    total_cost = num_data * NB_TIRAGE_SIMULE * MISE
    total_gain = CALCUL_gains(histogram)
    final_result = total_gain - total_cost
    expectation = final_result / (NB_TIRAGE_SIMULE * num_data)
    print(f"\nSoit un coût de {total_cost}")
    print(f"Pour un gain de {total_gain}\n")
    print(f"Au final : {final_result}")
    print(f"Espérance : {expectation}\n")
def main():
    for analysis in LISTE_ANALYSE:
        file_path, method = analysis
        num_data, histogram = process_file(file_path)
        display_results(method, num_data, histogram)
if __name__ == "__main__":
    main()