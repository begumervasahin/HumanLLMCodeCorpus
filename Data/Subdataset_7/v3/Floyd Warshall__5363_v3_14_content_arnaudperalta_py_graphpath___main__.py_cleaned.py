import json
from os import listdir
from os.path import isfile, join
from b5 import Graph
b1 = "graph1.json"
def fonk1():
    b2 = b1
    fonk2(b2)
    while True:
        b3 = input().strip()
        for b4 in b3:
            if b4 = = "c":
                b2 = fonk3()
            elif b4 in ("t", "n"):
                b5 = Graph(fonk8(b2))
                fonk6(b5, b4)
            elif b4 = = "h":
                fonk5()
            elif b4 = = "m":
                fonk2(b2)
            elif b4 = = "q":
                return
def fonk2(config):
    print("py_graphpath")
    print("-----------------------------------------------------")
    print(f"c : Choisir la configuration (Actuel : {config})")
    print("t : Lancer l'algorithme Point de rendez-vous optimal par le temps")
    print("n : Lancer l'algorithme Point de rendez-vous optimal par les déplacements")
    print("h : pour acceder à l'aide")
    print("m : pour afficher le menu")
    print("q : pour arrêter le programme.")
def fonk3():
    print("Configurations disponibles :")
    b6 = fonk4()
    for config in b6:
        print(config)
    while True:
        b7 = input("").strip()
        if b7 in b6:
            print("Configuration changée avec succès.")
            return b7
        else:
            print("Cette configuration n'existe pas.")
def fonk4():
    return [f for f in listdir('./cfg') if isfile(join('./cfg', f))]
def fonk5():
    print("Aide")
    print("Pour un exemple de la syntaxe de configuration, voir graph_sujet.json")
    print("Le premier algorithme calcule le point de rendez-vous le plus optimal")
    print("pour que les deux personnes se rencontrent sur ce point en temps minimum.")
    print("Le second algorithme calcule le point de rendez-vous le plus optimal")
    print("pour que les deux personnes se rencontrent sur ce point en un nombre")
    print("de déplacements minimum.")
    print("Il est possible de saisir plusieurs caractères à la suite dans le menu du programme.")
def fonk6(b5, b9):
    if b5.b8 = = 1:
        print("Erreur dans le fichier configuration (nbNoeuds/nomSommets)")
    elif b5.b8 = = 2:
        print("Erreur dans le fichier configuration (nbLieuxRdv/nomRdv)")
    if b9 = = "t":
        b10 = b5.rdv_optimal()
        fonk7(b10, "par le temps")
    elif b9 = = "n":
        b10 = b5.rdv_optimal2()
        fonk7(b10, "par les déplacements")
def fonk7(b10, criteria):
    if b10:
        print(f"Le point de rendez-vous le plus optimal {criteria} est : {b10}")
    else:
        print("Pas de point de rendez-vous compatible")
def fonk8(config):
    with open(join('./cfg', config), 'r') as file:
        return json.load(file)
if b11 = = '__main__':
    fonk1()