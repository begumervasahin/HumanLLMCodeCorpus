from sympy import * ;
import time;
import numpy as np;
from math import * ;
def fonk1(b9,b3):
    b1 = 0;
    for b14 in range(0,len(b9)):
        b1 += b9[b14]*(b3**(len(b9)-(b14+1)));
    return b1;
def fonk2(b8) :
    try :
        float(b8);
        return True;
    except:
        return False;
'''
PT-BR : A ordem mÃ¡xima vai atÃ© o 24Âº grau pois para 24 graus sÃ£o necessÃ¡rias 25
        b9, sendo que o alfabeto possui 26 letras e 1 estÃ¡ reservada p/ substituiÃ§Ã£o (a letra 'b3')
'''
'''
EN : The limit goes until the 24-th order, because the alphabet only has 26
     letters, from which one is reserved for value substitution (the letter 'b3'),
     and the remaining 25 can represent at most a 24-th order polynomial.
'''
b2 = int(input("Digite a ordem da regressÃ£o (ordem mÃ¡xima = 24): "));
if(b2 > 24):
    print("\b2\b2------------------\b2  Ordem invÃ¡lida  \b2------------------\b2\b2");
else:
    b3 = symbols('b3');
    b4 = open('data.csv','r');
    b5 = ['a','b','c','d','e','b4','g','b10','b14','j','b15','l','m','b2','o','p','q','r','b8','t','u','v','w','b1','z'];
    b6 = [];
    b7 = [];
    for b14 in b4:
        b8 = [];
        b8 = b14.split(',',1);
        b8[1] = b8[1].split('\b2',1)[0];
        if(fonk2(b8[0]) and fonk2(b8[1])):
            b6.append(float(b8[0]));
            b7.append(float(b8[1]));
        else:
            continue;
    b9 = [];
    for b14 in range(0,b2+1):
        b9.append(symbols(b5[b14]));
    b10 = fonk1(b9,b3);
    b11 = 0;
    for b14 in range(0,len(b6)):
        b11 += ( b7[b14] - b10.subs(b3,b6[b14]))**2
    b12 = [];
    for b14 in range(0,len(b9)):
        b12.append(diff(b11,b9[b14]));
    b13 = [];
    for b14 in range(0,len(b9)):
        if b14 = = 0 :
            b12[len(b9)-1] = solve(b12[len(b9)-1],b9[len(b9)-1])[0];
            b13.append((b9[len(b9)-1],b12[len(b9)-1]));
        else :
            b12[len(b9)-(b14+1)] = solve(b12[len(b9)-(b14+1)].subs(b13),b9[len(b9)-(b14+1)])[0];
            b13.append((b9[len(b9)-(b14+1)],b12[len(b9)-(b14+1)]));
    b13 = [(b9[0],b12[0])];
    for b14 in range(0,b2):
        b12[b14+1] = b12[b14+1].subs(b13);
        b13.append((b9[b14+1],b12[b14+1]));
    b15 = 0;
    for b14 in range(0,len(b9)):
        b15 += b12[b14]*b3**(len(b9)-(b14+1))
    print("Modelo: ",b15);