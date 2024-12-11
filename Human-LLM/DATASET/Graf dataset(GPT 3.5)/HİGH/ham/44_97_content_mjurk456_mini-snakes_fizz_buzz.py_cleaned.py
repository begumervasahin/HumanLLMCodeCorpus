a1 = 0
a2 = 0
a3 = 1
a4 = 0
a5 = 0
a6 = 0
a7 = 0
while True:
    try:
        a1,a2 = [int(a) for a in input("Input start and stop values for counting dividing them with a space: ").split()]
        break
    except ValueError:
        print("One or all values are wrong. Input should be like 12 10")
if a1>a2:
    a3 = -1
for i in range(a1,a2+a3,a3):
    if (i%b1 = =0) and (i%b3!=0) and (i!=0):
        print("fizz",b2 = " ")
        a4 = a4+1
    elif (i%b3 = =0) and (i%b1!=0) and (i!=0):
        print("buzz",b2 = " ")
        a5 = a5+1
    elif (i%b1 = =0) and (i%b3==0) and (i!=0):
        print("fizzbuzz",b2 = " ")
        a6 = a6+1
    else:
        print(i,b2 = " ")
        a7 = a7+1
print("\nFizzes in range: ", a4)
print("Buzzes in range: ", a5)
print("Fizzbuzes in range: ",a6)
print("Normal numbers in range: ",a7)