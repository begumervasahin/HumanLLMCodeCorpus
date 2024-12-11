def fonk1(n):
    a1 = 0
    a2 = 1
    for i in range(n):
        yield a1
        a1,a2 = a2,a1+a2
def fonk2():
    b1 = int(input("Enter b1 in the Fibonacci sequence: "))
    return b1
for n in fonk1(fonk3()):
    print(n)
--------------------------------------------------------------------
def fonk3():
    b1 = int(input("Enter b1 in the Fibonacci sequence: "))
    return b1
a1 = 0
a2 = 1
a3 = 0
while True:
  b2 = fonk3()
  if b2 <= 0:
    print("Enter a positive value")
    continue
  else:
    break
print("Fibonacci sequence upto",b2,":")
while a3 < b2:
  if b2 = = 1:
    print(a1)
  else:
    print(a1,b3 = ', ')
    a1,a2 = a2,a1+a2
  a3 += 1