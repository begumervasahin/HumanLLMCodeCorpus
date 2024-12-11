
a1 = 1
a2 = 1
a3 = 0
b1 = int(input("Enter the number of the fibonacci sequence you want displayed: "))
for x in range(b1-1):
    a3 = a1 + a2
    a2 = a1
    a1 = a3
b2 = list(str(b1))
if b2[len(b2) - 1] == '1' and b2[len(b2) - 2] != 1:
    b3 = 'st'
elif b2[len(b2) - 1] == '2' and b2[len(b2) - 2] != 1:
    b3 = 'nd'
elif b2[len(b2) - 1] == '3' and b2[len(b2) - 2] != 1:
    b3 = 'rd'
else:
    b3 = 'th'
print(f"{a1:,d} is the {b1:,d}{b3} number of the fibonacci sequence.")