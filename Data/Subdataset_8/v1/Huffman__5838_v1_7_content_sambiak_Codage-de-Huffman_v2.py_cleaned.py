import queue as Q
class Paire:
    def __init__(self, element, priorité):
        self.element = element
        self.priorité = priorité
    def __lt__(self, other):
        return int.__lt__(self.priorité, other.priorité)
    def __gt__(self, other):
        return int.__gt__(self.priorité, other.priorité)
    def __eq__(self, other):
        return int.__eq__(self.priorité, other.priorité) and self.element == other.element
    def __le__(self, other):
        return int.__le__(self.priorité, other.priorité)
    def __ge__(self, other):
        return int.__ge__(self.priorité, other.priorité)
    def __str__(self):
        return "(" + self.element.__str__() + self.priorité.__str__() + ")"
    def __repr__(self):
        return self.__str__()
class File_de_prio:
    def __init__(self):
        self.données = []
    def qsize(self):
        return len(self.données)
    def get(self):
        return self.données.pop()
    def put(self, elem):
        for i, el in enumerate(self.données):
            if elem > el:
                self.données = self.données[:i] + [elem] + self.données[i:]
                return None
        self.données =  self.données + [elem]
    def __str__(self):
        return self.données.__str__()
class Arbre:
    def __init__(self, valeur):
        self.noeud = valeur
        self.gauche = None
        self.droite = None
    def __str__(self):
        return "(" + self.gauche.__str__() + self.noeud.__str__() + self.droite.__str__() + ")"
def creer_arbre(densité_lettres):
    file_de_prio = File_de_prio()
    for lettre in densité_lettres.keys():
        file_de_prio.put(Paire(Arbre(lettre), densité_lettres[lettre]))
    while file_de_prio.qsize() > 1:
        gauche = file_de_prio.get()
        droite = file_de_prio.get()
        nouveau_arbre = Arbre(None)
        nouveau_arbre.gauche = gauche.element
        nouveau_arbre.droite = droite.element
        file_de_prio.put(Paire(nouveau_arbre, gauche.priorité + droite.priorité))
    return file_de_prio.get().element
def creer_densite(texte):
    densité_lettres = {}
    for lettre in texte:
        if lettre in densité_lettres:
            densité_lettres[lettre] += 1
        else:
            densité_lettres[lettre] = 1
    return densité_lettres
def creer_dict(arbre, parcours, dico):
    if arbre.noeud is not None:
        dico[arbre.noeud] = parcours
    if arbre.gauche is not None:
        creer_dict(arbre.gauche, parcours + "0", dico)
    if arbre.droite is not None:
        creer_dict(arbre.droite, parcours + "1", dico)
if __name__ == "__main__":
    dens = creer_densite("chabadabada")
    print(dens)
    arbre = creer_arbre(dens)
    dico = {}
    creer_dict(arbre, "", dico)
    print(dico)