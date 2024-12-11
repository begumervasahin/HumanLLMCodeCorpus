import random
'''
find the b3-th Monisen a1.
A a1 b1 is a Monisen a1 if b1 = 2**b2-1
and both b1 and b2 are prime numbers.
For example, if b2 = 5, b1=2**b2-1=31,
5 and 31 are both prime numbers,
so 31 is a Monisen a1.
Put the 6-th Monisen a1 into a
single text file and submit online.
b3 = input("enter the nth prime ")
a1 = 10
a2 = 2
while a2 <int(b3):
    if all(a1 % a4 != 0 for a4 in range(2, a1)):
        a2 = a2+1
    a1 = a1+1
    b4 = 2**a2-1
print("6TH prime a1: ",a1-1,"and the monisen a1 is: ", b4)
b5 = [a4+1 for a4 in range(10) if a4%2==0]
print(b5)
a3 = 0
a4 = 1
while True:
    a3 +=a4
    a4+=1
    if a3>10:
        break
print('a4 = {}, sum={}'.format(a4,a3))
a4 = 1
while(a4 % 3):
    print(a4, b6 = ' ')
    if (a4 >= 10):
        break
    a4 += 1
'''
def fonk1(num,base):
  	if(num >= base):
            fonk1(num
        print(num%base, b6 = ' ')
b7 = int(input())
b8 = int(input())
fonk1(b7, b8)