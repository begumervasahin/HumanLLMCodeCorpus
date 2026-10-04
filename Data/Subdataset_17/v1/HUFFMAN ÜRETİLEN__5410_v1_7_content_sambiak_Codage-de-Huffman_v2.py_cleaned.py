class Paire:
    def __init__(self, element, priorite):
        self.element = element
        self.priorite = priorite
    def __lt__(self, other):
        return self.priorite < other.priorite
    def __gt__(self, other):
        return self.priorite > other.priorite
    def __eq__(self, other):
        return self.priorite == other.priorite and self.element == other.element
    def __le__(self, other):
        return self.priorite <= other.priorite
    def __ge__(self, other):
        return self.priorite >= other.priorite
    def __str__(self):
        return f"({self.element}, {self.priorite})"
    def __repr__(self):
        return self.__str__()
class FileDePrio:
    def __init__(self):
        self.donnees = []
    def qsize(self):
        return len(self.donnees)
    def get(self):
        return self.donnees.pop()
    def put(self, elem):
        for i, el in enumerate(self.donnees):
            if elem > el:
                self.donnees = self.donnees[:i] + [elem] + self.donnees[i:]
                return
        self.donnees.append(elem)
    def __str__(self):
        return str(self.donnees)
class Arbre:
    def __init__(self, valeur):
        self.noeud = valeur
        self.gauche = None
        self.droite = None
    def __str__(self):
        return f"({self.gauche}, {self.noeud}, {self.droite})"
def creer_arbre(densite_lettres):
    file_de_prio = FileDePrio()
    for lettre, densite in densite_lettres.items():
        file_de_prio.put(Paire(Arbre(lettre), densite))
    while file_de_prio.qsize() > 1:
        gauche = file_de_prio.get()
        droite = file_de_prio.get()
        nouveau_arbre = Arbre(None)
        nouveau_arbre.gauche = gauche.element
        nouveau_arbre.droite = droite.element
        file_de_prio.put(Paire(nouveau_arbre, gauche.priorite + droite.priorite))
    return file_de_prio.get().element
def creer_densite(texte):
    densite_lettres = {}
    for lettre in texte:
        if lettre in densite_lettres:
            densite_lettres[lettre] += 1
        else:
            densite_lettres[lettre] = 1
    return densite_lettres
def creer_dict(arbre, parcours, dico):
    if arbre.noeud is not None:
        dico[arbre.noeud] = parcours
        return
    if arbre.gauche is not None:
        creer_dict(arbre.gauche, parcours + "0", dico)
    if arbre.droite is not None:
        creer_dict(arbre.droite, parcours + "1", dico)
if __name__ == "__main__":
    texte = "chabadabada"
    densite = creer_densite(texte)
    print("Densité:", densite)
    arbre = creer_arbre(densite)
    print("Arbre:", arbre)
    dico = {}
    creer_dict(arbre, "", dico)
    print("Dictionnaire des codes:", dico)