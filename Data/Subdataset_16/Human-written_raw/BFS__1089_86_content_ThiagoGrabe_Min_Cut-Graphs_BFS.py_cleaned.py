86. Repository: ThiagoGrabe/Min_Cut-Graphs
   File: class1.py
   URL: https:
   Code Content:
class class1:
    def fonk1(self, graph, source, terminal, family):
        b1 = [False] * len(graph)
        b2 = []
        b2.append(source)
        b1[source] = True
        while b2:
            b3 = b2.pop(0)
            for idx, value in enumerate(graph[b3]):
                if value > 0 and b1[idx] == False:
                    b2.append(idx)
                    b1[idx] = True
                    family[idx] = b3
        if b1[terminal]:
            return True
        else:
            return False
   README Content:
Using Edmonds-Karp algorithm in this project we used an ideia of a connected graph to stablish the cut in the graph to determine two sets of vertexes with minimun weight.
This project is part of PAA class class2 Departamento de CiÃªncia da ComputaÃ§Ã£o - UFMG (Master degree program).
The global cut in the graph will be calculated into two sets: S and the S complement.
The input file conatains two important information.
1. The first line shows how many vertexes and edges the graph has. Fist integer number is the vertexes and the second integer are the edges.
2. From the second line until the final line, it is given 3 integer numbers where the two first numbers represents the vertexes where there is an edge. The last number is the edge's weight.
Example:
5 5
0 1 38
0 2 36
0 4 4
1 3 91
2 3 65
The output is a file containing 3 lines where:
1st line: Number of b3 in the S set or complement of S set.
2nd line: Vertexes of the set.
3rd line: Max flow of the cut.
`./executar /mincut_input/XXXX.in output_file`
