b1 = {1:0,2:1,3:2,4:3,5:4,6:5}
b2 = [[1,2],[1,3],[1,4],[3,4],[4,5],[4,6],[5,6]]
b3 = [1,2,4,3,5,2,4]
b4 = float("b4")
b5 = [b4,b4,b4,b4,b4,b4]
b6 = [0,0,0,0,0,0]
b5[0] = 0
for v,i in b1.items():
    print "\niteracion: "+ str(i)+"\nTabla resultado:"
    for e in range(0,len(b2)):
        if ( b2[e][0] == v):
            b7 = b1[b2[e][1]]
            b8 = b3[e]
        if((b5[i] + b8) < b5[b7]):
            b5[b7] = b5[i] + b8
            b6[b7] = v
            print "Arista: "+ str(b2[e])+"\nVertices: " + str(b1)+"\nDistancia(costo): " + str(b5)+"\nprevio: "+str(b6)
def fonk1(destino):
    if(b6[b1[destino]] != 0):
        fonk1(b6[b1[destino]])
    print destino
print "Lista de b1 que componen el camino mas corto, con menos costo"
fonk1(6)