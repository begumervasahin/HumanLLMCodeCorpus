from queue import PriorityQueue
class Node:
    data = ' '
    frequence=0
    leftChild=None
    rightChild=None
    def __init__(self,data,frequence,leftChild=None,rightChild=None):
        self.data=data
        self.frequence=frequence
        self.leftChild=leftChild
        self.rightChild=rightChild
    def __lt__(self,other):
        return self.frequence < other.frequence
    def __repr__(self):
        return "Noeud : de valeur ({}), de frÃ©quence ({}), avec comme leftChild(),avec comme rightChild ()\n".format(self.data,self.frequence)
liste = PriorityQueue()
def init_liste(string):
    tableauVerification=[]
    boolean=True
    boolean1=True
    for val in str(string):
        print (val)
        if not val in str(tableauVerification):
            tableauVerification.append([val,string.count(val)])
            liste.put(Node(val,string.count(val)))
        elif (val==' ' and boolean==True):
            liste.put(Node(val,string.count(val)))
            tableauVerification.append([val,string.count(val)])
            boolean=False
        elif (val==',' and boolean1==True):
            liste.put(Node(val,string.count(val)))
            tableauVerification.append([val,string.count(val)])
            boolean1=False
    return liste
def creationArbre(liste):
    while liste.qsize()>1:
        noeudGauche=liste.get()
        noeudDroit=liste.get()
        frequence=noeudGauche.frequence + noeudDroit.frequence
        noeud=Node(None,frequence,noeudGauche,noeudDroit)
        liste.put(noeud)
    return noeud
tableHachage={}
def creationTableHachage(val,code,tableHachage):
    if val.leftChild==None and val.rightChild==None:
        tableHachage.update({val.data : code})
        return tableHachage
    if val.leftChild!=None:
        creationTableHachage(val.leftChild,code+"0",tableHachage)
    if val.rightChild!=None:
        creationTableHachage(val.rightChild,code+"1",tableHachage)
def encodage(string,tableHachage):
    chaineCoder=""
    for i in string:
        chaineCoder=chaineCoder+str(tableHachage[i])
    return chaineCoder
i=0
def decodage(string,noeud):
    global i
    if noeud.leftChild==None and noeud.rightChild==None:
        char=noeud.data
        return char
    if string[i]=="0":
        i+=1
        return decodage(string,noeud.leftChild)
    elif string[i]=="1":
        i+=1
        return decodage(string,noeud.rightChild)
f = open('texteEncode.txt', 'r')
string = f.read()
f.close()
liste=init_liste(string)
noeud= creationArbre(liste)
print(noeud)
creationTableHachage(noeud,"",tableHachage)
print (tableHachage)
encode=encodage(string,tableHachage)
print (encode)
f = open('texteEncode.txt', 'w')
f.write(str(encode))
f.close()
string = encodage(string,tableHachage)
stringc=""
while i<len(string):
    stringc+=decodage(string,noeud)
print(stringc)
f.close()