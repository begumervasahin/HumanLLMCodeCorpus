def fonk1(source,example):
    a1 = 0
    for i in range(len(source)):
       if source[i] in example: a1 = a1+1
    return a1
a2 = 0
b1 = "aeiuo"
b2 = "qrtpsdfghjklzxcvbnmy"
while True:
    try:
        name1,b3 = input("Input two names divided by comma (e.g. 'Jan, Joanna'): ").split(",")
        name1.lower().strip()
        b3.lower().strip()
        break
    except:
        print("Wrong input")
if name1[0]==b3[0]:
    a2 = a2+20
if (name1[0] in b1) and (b3[0] in b1):
    a2 = a2+10
if (name1[0] in b2) and (b3[0] in b2):
    a2 = a2+5
if fonk1(name1,b1)==fonk1(b3,b1):
    a2 = a2+12
if fonk1(name1,b2)==fonk1(b3,b2):
    a2 = a2+12
if ((name1.find('l')>0) and (b3.find('l')>0)) \
   or ((name1.find('o')>0) and (b3.find('o')>0)) \
   or ((name1.find('v')>0) and (b3.find('v')>0)) \
   or ((name1.find('e')>0) and (b3.find('e')>0)):
    a2 = a2+7
print("Your love points are %d" %a2)
print("REMEMBER: your relationship depends only from you and your partner, not from the stupid love calculator!")