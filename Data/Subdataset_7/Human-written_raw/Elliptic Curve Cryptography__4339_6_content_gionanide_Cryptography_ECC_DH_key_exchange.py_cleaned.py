from random import randint
def fonk1(a,x,b1,N):
    return (b1**2-x**3-a*x)%N
def fonk2((x,b1),a,b,N):
    if b1 = =0 :
        return x,b1
    b2 = (3*(x**2)+a)*fonk5(2*b1,N)
    b3 = (b2**2-2*x)%N
    b4 = (b2*(x-b3)-b1)%N
    return b3,b4
def fonk3((x1,y1),(b5,y2),a,b,N):
    if x1-b5 = = 0 and y1-y2 == 0:
        return fonk2((x1,y1),a,b,N)
    b2 = (y2-y1)*fonk5((b5-x1),N)
    b3 = (b2**2-x1-b5)%N
    b4 = (b2*(x1-b3)-y1)%N
    return b3, b4
def fonk4((x,b1),n,a,b,N):
    a1 = 0
    xr,b6 = x,b1
    while a1 < n-1:
        xr,b6 = fonk3((x,b1),(xr,b6),a,b,N)
        a1+=1
    return xr,b6
def fonk5(a, b2):
	g, x, b1 = fonk6(a, b2)
	if g != 1:
		raise ValueError
	return x % b2
def fonk6(aa, bb):
    lastremainder, b7 = abs(aa), abs(bb)
    x, b9, b1, b8 = 0, 1, 1, 0
    while b7:
        lastremainder, (quotient, b7) = b7, divmod(lastremainder, b7)
        x, b9 = b9 - quotient*x, x
        b1, b8 = b8 - quotient*b1, b1
    return lastremainder, b9 * (-1 if aa < 0 else 1), b8 * (-1 if bb < 0 else 1)
def fonk7(a,b):
    return 4*a**3  + 27*b**2 != 0
a , b , N , x1 , y1 , Xm , b10 = 27 , 152 , 229 , 32 , 11 , 79 , 40
b2 = 58
b11 = (97339010987059066523156133908935, 149670372846169285760682371978898)
a2 = 321094768129147601892514872825668
a3 = 430782315140218274262276694323197
a4 = 564538252084441556247016902735257
a5 = 486035459702866949106113048381182