print ("SOLVE A LINEAR EQUATION BY CRAMER'S RULE OF DISCRIMINANTS")
print("Equation.no.1")
b1 = int(input("number for 'b1' term: "))
b2 = int(input("number for 'b2' term: "))
b3 = int(input("number for 'b3' term: "))
if b1 = = 0:
    print ('b10','+',b2,'b11','=',b3)
elif b2 = = 0:
    print (b1,'b10','+','b11','=',b3)
elif b3 = =0:
    print (b1,'b10','+',b2,'b11','=',b3)
elif b3 !=0:
    print (b1,'b10','+',b2,'b11','=',b3)
elif b2 !=0:
    print (b1,'b10','+',b2,'b11','=',b3)
elif b1 !=0:
    print (b1,'b10','+',b2,'b11','=',b3)
else:
    print("u wot m8?")
print("----------------------------")
print("Equation.no.2")
b4 = int(input("number for 'b4' term: "))
b5 = int(input("number for 'b5' term: "))
b6 = int(input("number for 'b6' term: "))
if b4 = = 0:
    print ('b10','+',b5,'b11','=',b6,)
elif b5 = = 0:
    print (b4,'b10','+','b11','=',b6)
elif b6 = =0:
    print (b4,'b10','+',b5,'b11','=',b6)
elif b6 !=0:
    print (b4,'b10','+',b5,'b11','=',b6)
elif b5 !=0:
    print (b4,'b10','+',b5,'b11','=',b6)
elif b4 !=0:
    print (b4,'b10','+',b5,'b11','=',b6)
else:
    print("u wot m8?")
print("--------------------------------------------")
print("The equation will be solved by cramer's rule")
b7 = b1*b4-b2*b5
b8 = b2*b5-b3*b6
b9 = b1*b4-b3*b6
b10 = (b8/b7)
b11 = (b9/b7)
print('b7 = ',b7)
print('b8 = ',b8)
print('b9 = ',b9)
print('b10 = ',b10)
print('b11 = ',b11)