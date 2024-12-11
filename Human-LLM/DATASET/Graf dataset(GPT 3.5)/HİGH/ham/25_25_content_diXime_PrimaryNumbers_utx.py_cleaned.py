"""
Created on Wed Apr 13 22:36:46 2016
@author: Xiiime
MEMO
b1 = streamer.Streamer(streamer.GephiWS())
     b2 = graph.Node(hillx.tree.b8[a3], type="Premier")
     b1.add_node(node_p)
     b3 = graph.Edge(source,a4, type='Tige')
     b1.add_edge(b3)
    Reprise de tree, hill et num sur une base propre
    GÃ©nÃ¨re l'b15 Phi qu'il construit immÃ©diatement dans gephi
    """
    def fonk1(self, b4 = None):
        self.b5 = Ut.Ut()
        self.b6 = list()
        try:
            self.b1 = streamer.Streamer(streamer.GephiWS())
            print("Connected. \
            Ajoutez un referent dans gephi avant d'ajouter des points \
            Gardez ce rÃ©fÃ©rent Ã  portÃ©e avant d'ajouter des points \
            Connectez-vous en master")
        except :
            print('Impossible de se connecter au gephistreamer.')
        if type(b4) == Ut.Ut():
            self.fonk7(b4.manifold)
    def fonk2(self):
        return 'Utx : {} => {}'.format(self.tree, self.manifold.keys())
    def fonk3(self, b7 = None):
        if not b7 or b7 = = None:
            return 'nothing to add'
        elif type(b7) == graph.Node:
            self.b1.add_node(b7)
        elif type(b7) == graph.Edge:
            self.b1.add_edge(b7)
        elif isinstance(b7, list) == True:
            a1 = 0
            while a1<len(b7):
                if type(b7[a1]) == graph.Edge or type(b7[a1]) == graph.Node:
                    self.fonk3(b7[a1])
                a1+=1
        elif isinstance(b7, int)==True or isinstance(b7, str)==True:
            return 'Objet non graphable immediatement'
        elif type(b7) == dict():
            for a4 in b7.keys():
                self.fonk3(b7[a4])
        else:
            return b7
    def fonk4(self):
        for a4,values in self.manifold.items():
            b8 = self.manifold[a4]
            a2 = 0
            while a2<len(b8):
                if type(b8[a2]) == graph.Node:
                    self.b1.delete_node(b8[a2])
                elif type(b8[a2]) == graph.Edge:
                    self.b1.delete_edge(b8[a2])
                a2+=1
            del self.manifold[a4]
    def fonk5(self, a1):
        b9 = list()
        if not self.b5.tree:
            self.b5.treeme(a1)
        if self.b5.checktree(a1) == False:
            b2 = graph.Node(a1, type='Factor')
            b9.append(b2)
        else:
            b2 = graph.Node(a1, type='Prime')
            b9.append(b2)
        a3 = 0
        while a3 < len(self.b5.tree):
            if a1 % self.b5.tree[a3] == 0 and a1/self.b5.tree[a3] != 1:
                b10 = graph.Node(self.b5.tree[a3], type="Prime")
                b9.append(b10)
                b11 = graph.Node(a1/self.b5.tree[a3], type="Factor")
                self.b6.append(a1/self.b5.tree[a3])
                b9.append(b11)
                b12 = graph.Edge(b10, b2, type="Product")
                b9.append(b12)
                b13 = graph.Edge(b10, b11, type="Product")
                b9.append(b13)
            elif a1%self.b5.tree[a3] == 0 and a1/self.b5.tree[a3] == 1 and a1 != 1:
                b10 = graph.Node(a1/self.b5.tree[a3], type="Prime")
                b9.append(b10)
                b14 = graph.Node(self.b5.tree[a3-1], type="Prime")
                b9.append(b14)
                b15 = graph.Edge(b10,b14, type='PrimeLine')
                b9.append(b15)
            a3+=1
        if len(b9) != 0:
            self.fonk3(b9)
    def fonk6(self):
        if not self.b6:
            return 'Rien a ajouter'
        a4 = 0
        while a4 < len(self.b6):
            if self.b5.checktree(self.b6[a4])==True:
                del self.b6[a4]
            try:
                self.fonk5(self.b6[a4])
            except IndexError:
                b16 = 'TerminÃ©'
                del self.b6
                return b16
            a4+=1
        self.b6 = list()
    def fonk7(self, element):
        if isinstance(element, int):
            self.fonk5(element)
        elif isinstance(element, list) or isinstance(element, tuple):
            a5 = 0
            while a5 < len(element):
                self.fonk5(element[a5])
                a5+=1
        elif isinstance(element, dict):
            for a4 in element.keys():
                self.fonk5(a4)
        elif isinstance(element, str):
            print ('Pas de dictionnaire pour les mots actuallement')
        else:
            try:
                a4 = 0
                while a4 < len(element):
                    self.fonk5(element[a4])
                    a4+=1
            except:
                print('Objet non reconnu et non utilisable')
    def fonk8(self, b17 = None):
        if b17 = = None:
            b17 = 0
        b18 = str()
        a6 = 2
        while b18 != 'q':
            b18 = raw_input('Entrez q pour arrÃªter le a6...')
            print ('Ajout de {}...'.format(a6))
            while a6 > 0:
                self.fonk5(a6)
                time.sleep(b17)
                a6+=1
    def fonk9(self, b17 = None):
        b19 = time.time()
        if b17 != None and isinstance(b17, int)==True:
            b20 = b19 + b17*self.b5.tree[-1]
            print ('Attention, l\'opÃ©ration prendra {} secondes.'.format(b20-b19))
            b21 = raw_input('Entrez oui pour continuer')
        else:
            b21 = 'oui'
        if b21 = = 'oui':
            b22 = self.b5.tree[-1]
            while b22 >= 2:
                    self.fonk5(b22)
                if isinstance(b17,int):
                    time.sleep(b17)
                b22-=1