import sys
def fonk1(b5,start,end):
    if(len(b5)==1):
        return b5
    elif(start<end):
        b1 = fonk3(b5,start,end)
        fonk1(b5,start,b1-1)
        fonk1(b5,b1+1,end)
    return b5
def fonk2(b5):
    return fonk1(b5,0,len(b5)-1)
def fonk3(b5,start,end):
    b2 = start
    b3 = start-1
    while(b2<end):
        if(b5[b2]<=b5[end]):
            b3+=1
            b5[b2],b5[b3]=b5[b3],b5[b2]
        b2+=1
    b5[end],b5[b3+1]=b5[b3+1],b5[end]
    return b3+1
def fonk4(b5,start,end):
    if(len(b5)==1):
        return b5
    if(start<end):
        b1 = fonk5(b5,start,end)
        fonk4(b5,start,b1)
        fonk4(b5,b1+1,end)
    return b5
def fonk5(b5,start,end):
    b4 = True
    b2 = start-1
    b3 = end+1
    while(b4):
        b2+=1
        while(b5[b2]<b5[start]):
            b2+=1
        b3-=1
        while(b5[b3]>b5[start]):
            b3-=1
        if(b2>=b3):
            b4 = False
            return b3
        else:
            b5[b2],b5[b3]=b5[b3],b5[b2]
def fonk6(b5):
    return fonk4(b5,0,len(b5)-1)
b5 = [15,4,68,24,75,16,42]
b6 = fonk6(b5)
print(b6)
b7 = fonk2(b5)
print(b7)