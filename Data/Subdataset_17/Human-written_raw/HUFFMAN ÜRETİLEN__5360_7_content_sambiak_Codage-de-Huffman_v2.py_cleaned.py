import queue as Q
class Paire():
    def __init__(self, element, prioritÃ©):
        self.element = element
        self.prioritÃ© = prioritÃ©
    def __lt__(self, other):
        return int.__lt__(self.prioritÃ©, other.prioritÃ©)
    def __gt__(self, other):
        return int.__gt__(self.prioritÃ©, other.prioritÃ©)
    def __eq__(self, other):
        return int.__eq__(self.prioritÃ©, other.prioritÃ©) and self.element == other.element
    def __le__(self, other):
        return  int.__le__(self.prioritÃ©, other.prioritÃ©)
    def __ge__(self, other):
        return  int.__ge__(self.prioritÃ©, other.prioritÃ©)
    def __str__(self):
        return "(" + self.element.__str__() + self.prioritÃ©.__str__() + ")"
    def __repr__(self):
        return self.__str__()
class File_de_prio():
    def __init__(self):
        self.donnes = []
    def qsize(self):
        return len(self.donnes)
    def get(self):
        return self.donnes.pop()
    def put(self, elem):
        for i, el in enumerate(self.donnes):
            if elem > el:
                self.donnes = self.donnes[:i ] + [elem] + self.donnes[i :]
                return None
        self.donnes =  self.donnes + [elem]
    def __str__(self):
        return self.donnes.__str__()
class Arbre():
    def __init__(self, valeur):
        self.noeud = valeur
        self.gauche = None
        self.droite = None
    def __str__(self):
        return  "(" + self.gauche.__str__() + self.noeud.__str__() + self.droite.__str__() + ")"
def creer_arbre(densitÃ©_lettres):
    file_de_prio = File_de_prio()
    for lettre in densitÃ©_lettres.keys():
        file_de_prio.put(Paire(Arbre(lettre), densitÃ©_lettres[lettre]))
    print(file_de_prio)
    while file_de_prio.qsize() > 1:
        gauche = file_de_prio.get()
        droite = file_de_prio.get()
        nouveau_arbre = Arbre(None)
        nouveau_arbre.gauche = gauche.element
        nouveau_arbre.droite = droite.element
        file_de_prio.put(Paire(nouveau_arbre, gauche.prioritÃ© + droite.prioritÃ©))
    return file_de_prio.get().element
def creer_densite(texte):
    densitÃ©_lettres = {}
    for lettre in texte:
        if lettre in densitÃ©_lettres:
            densitÃ©_lettres[lettre] += 1
        else:
            densitÃ©_lettres[lettre] = 1
    return densitÃ©_lettres
def creer_dict(arbre, parcours, dico):
    if arbre.noeud != None:
        print("h",parcours)
        dico[arbre.noeud] = parcours
        print(dico[arbre.noeud])
        return None
    if arbre.gauche != None:
        parcours = parcours + "0"
        creer_dict(arbre.gauche, parcours, dico)
        print("p",parcours)
        parcours = parcours[:-1]
        print("p", parcours)
    if arbre.droite != None:
        parcours = parcours + "1"
        creer_dict(arbre.droite, parcours, dico)
if __name__ == "__main__":
    dens = creer_densite("chabadabada")
    print(dens)
    arbre = creer_arbre(dens)
    dico = {}
    creer_dict(arbre, "", dico)
    print(dico)