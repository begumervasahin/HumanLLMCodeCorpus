class class1:
    def fonk1(s,b1 = "-",b2="-"):
        s.b1 = b1
        s.b2 = b2
        s.b3 = None
class class2:
    def fonk2(s):
        s.b4 = class1()
    def fonk3(s,b11):
        b5 = len(b11[0])
        b6 = s.b4
        a1 = 0
        while(a1<b5):
            b7 = class1(b11[0][a1])
            b6.b3 = b7
            b6 = b6.b3
            a1 = a1+1
    def fonk4(s):
        b6 = s.b4.b3
        print()
        while(b6!=None):
            print(b6.b2,b8 = "")
            b6 = b6.b3
        print()
    def fonk5(s,b,b13):
        a2 = 0
        b6 = s.b4.b3
        while(b6!=None):
            if(b6.b1 = =b):
                b6.b2 = b
                a2 = 1
            b6 = b6.b3
        if(a2 = =0):
            b13.pop(0)
        b6 = s.b4.b3
        while(b6!=None):
            print(b6.b2,b8 = "")
            b6 = b6.b3
        print(b13)
    def fonk6(s):
        import time
        b6 = s.b4.b3
        print("ANSWER IS...")
        time.sleep(2.0)
        while(b6!=None):
            print(b6.b1,b8 = "")
            b6 = b6.b3
def fonk7():
 b9 = class2()
 print("Type 'view' to view answer")
 print("Type 'exit' to EXIT")
 b10 = ["python","jumble","easy","difficult","computer","hangman","failure","brilliant","worthy","xylophone","awkward","gypsy","jinx","burgular","bankrupt","crisis","hyphen","memento","mystery","pajama","pixel","rogue","rhythmic","twelfth","jealous","zombie","yatch","yak","zippy","unknown","battleground","player","psycho","beast","buzzard","boycott","coffin","witchcraft","rickshaw","mnemonic","pneumonia","peekaboo","diarrhoea","jaundice","gossip","despacito"]
 import random
 b11 = []
 b11.append(random.choice(b10))
 b9.fonk3(b11)
 b9.fonk4()
 b12 = None
 b13 = ["H","A","N","G","M","A","N"]
 while((b12!="exit" and b12!="view") and len(b13)!=0):
     b12 = input()
     if(b12!="exit" and b12!="view"):
         b9.fonk5(b12,b13)
     elif(b12 = ="view"):
         b9.fonk6()
         break
     elif(b12 = ="exit"):
         print("Exiting...")
         break
fonk7()
b14 = None
while(b14!="no"):
    print()
    print("1.PLAY")
    b14 = (input("Do you want to play again"))
    if(b14 = ="yes" or b14=="Yes" or b14=="YES"):
        fonk7()
    else:
        break