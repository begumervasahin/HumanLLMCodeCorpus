class class1:
    def fonk1(self,b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2():
    b4 = int(input())
    if(b4 = =-1):
        return None
    b5 = class1(b4)
    b6 = fonk2()
    b7 = fonk2()
    b5.b2 = b6
    b5.b3 = b7
    return b5
def fonk3(b5):
    if(b5 = =None):
        return
    if(b5.b1!=-1):
        print(b5.b1,b8 = ":")
    if(b5.b2!=None):
        print(b5.b2.b1,b8 = ",")
    else:
        print("-1",b8 = ",")
    if(b5.b3!=None):
        print(b5.b3.b1,b8 = "")
    else:
        print("-1",b8 = "")
    print()
    fonk3(b5.b2)
    fonk3(b5.b3)
b5 = fonk2()
fonk3(b5)
def fonk4(b5):
    if(b5 = =None):
        return 0
    b9 = fonk4(b5.b2)
    b10 = fonk4(b5.b3)
    return b9+b10+1
b9 = fonk4(b5)
b9
def fonk5(b5):
    if(b5 = =None):
        return
    print(b5.b1,b8 = " ")
    fonk5(b5.b2)
    fonk5(b5.b3)
    return
fonk5(b5)
def fonk6(b5):
    if(b5 = =None):
        return
    fonk6(b5.b2)
    print(b5.b1,b8 = " ")
    fonk6(b5.b3)
    return
fonk6(b5)
def fonk7(b5):
    if(b5 = =None):
        return
    fonk7(b5.b2)
    fonk7(b5.b3)
    print(b5.b1,b8 = " ")
    return
fonk7(b5)
def fonk8(b5):
    if(b5 = =None):
        return 0
    b11 = fonk8(b5.b2)
    b12 = fonk8(b5.b3)
    if(b11>b12):
        return b11+1
    else:
        return b12+1
b9 = fonk8(b5)
b9
def fonk9(b5,b13):
    if(b5 = =None):
        return
    if(b13 = =0):
        print(b5.b1)
    fonk9(b5.b2,b13-1)
    fonk9(b5.b3,b13-1)
    return
fonk9(b5,2)
def fonk10(b5,count):
    if(b5 = =None):
        return
    if(b5.b2 = =None and b5.b3==None):
        b5.b1 = count
        return b5
    else:
        b5.b1 = count
    fonk10(b5.b2,count+1)
    fonk10(b5.b3,count+1)
fonk10(b5,0)
fonk3(b5)
def fonk11(b5):
    if(b5 = =None):
        return
    if(b5.b2 = =None and b5.b3==None):
        return None
    b5.b2 = fonk11(b5.b2)
    b5.b3 = fonk11(b5.b3)
    return b5
def fonk12(b5):
    if(b5 = =None):
        return
    if(b5.b2!=None and b5.b3!=None):
        b14 = b5.b2
        b5.b2 = b5.b3
        b5.b3 = b14
    fonk12(b5.b2)
    fonk12(b5.b3)
    return b5
b15 = fonk12(b5)
fonk3(b15)
class class2:
    def fonk13(self,b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
import queue
b16 = queue.Queue()
def fonk14():
    b4 = int(input())
    if(b4 = =-1 or b4<0):
        return None
    b5 = class2(b4)
    b16.put(b5)
    while(not(b16.empty())):
        b17 = b16.get()
        print("enter the b2 child of :",b17.b1)
        b2 = int(input())
        if(b2!=-1):
            b18 = class2(b2)
            b17.b2 = b18
            b16.put(b18)
        print("enter the b3 child of :",b17.b1)
        b3 = int(input())
        if(b3!=-1):
            b19 = class2(b3)
            b17.b3 = b19
            b16.put(b19)
    return b5
def fonk15(b5):
    if(b5 = =None):
        return None
    b16.put(b5)
    while(not(b16.empty())):
        b17 = b16.get()
        print(b17.b1,b8 = ":")
        if(b17.b2!=None):
            print(b17.b2.b1,b8 = ",")
            b16.put(b17.b2)
        if(b17.b3!=None):
            print(b17.b3.b1,b8 = "")
            b16.put(b17.b3)
        print()
b5 = fonk14()
fonk15(b5)
def fonk16(post,inor):
    if(len(post)==0):
        return None
    b4 = post[len(post)-1]
    post.pop()
    b5 = class2(b4)
    a1 = -1
    for i in range(0,len(inor)):
        if(inor[i]==b5):
            a1 = i
            break
    b20 = inor[0:a1]
    b21 = inor[a1+1:]
    b22 = post[0:len(b20)]
    b23 = post[len(b20):]
    b2 = fonk16(b22,b20)
    b3 = fonk16(b23,b21)
    b5.b2 = b2
    b5.b3 = b3
    return b5
def fonk17(b5,m,n):
    if(b5 = =None):
        return None