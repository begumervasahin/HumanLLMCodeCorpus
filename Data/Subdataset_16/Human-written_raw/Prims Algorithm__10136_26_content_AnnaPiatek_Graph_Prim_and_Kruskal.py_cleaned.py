from graphvizual import *
import graphviz as gv
class b1:
    def fonk1(self,path):
        b1 = Graph(format='png')
        b2 = [['E','D',1],['B','C',2],['D','B',3],['C','D',3],['B','E',4],['A','B',5]]
        for item in b2:
            b3 = str(item[0])
            b4 = str(item[1])
            b5 = str(item[2])
            b1.edge(b3, b4, b5, b6 = 'black')
        b1 = apply_styles(b1, styles)
        b7 = b1.render(filename=str(10))
        b1.render(b8 = True)
        b9 = []
        b1 = Graph(format='png')
        for b10 in range(1,len(path)+1):
            b1 = Graph(format='png')
            b9.append([str(path[b10 - 1][0]), str(path[b10 - 1][1]), str(path[b10 - 1][2])])
            for item in b2:
                b3 = str(item[0])
                b4 = str(item[1])
                b5 = str(item[2])
                if [b3,b4,b5] in b9:
                    b1.edge(b3, b4, b5, b6 = 'red')
                elif [b4,b3,b5] in b9:
                    b1.edge(b3,b4,b5, b6 = 'red')
                else:
                    b1.edge(b3,b4,b5, b6 = 'black')
            b1 = apply_styles(b1, styles)
            b10 = b1.render(filename=str(b10))
            b1.render(b8 = True)
if b11 = = "__main__":
    b12 = Graph_0()
    b13 = b1()
    b12.add_edge('A', 'B', 5)
    b12.add_edge('B', 'E', 4)
    b12.add_edge('E', 'D', 1)
    b12.add_edge('D', 'B', 3)
    b12.add_edge('B', 'C', 2)
    b12.add_edge('C', 'D', 3)
    b12.add_edge('C', 'A', 6)
    '''Prim'''
    '''Kruskal'''
    print(b12.branches_building())
    print(b13.fonk1(b12.branches_building()))