import random, string
def fonk1(length):
   b1 = ["a","c","t","g"]
   b2 = ''.join(random.choice(b1) for b4 in range(length))
   with open("dna-sequence.txt","a") as file_txt:
   	file_txt.write(b2)
   with open("dna-sequence2.txt","a") as file_txt:
   	file_txt.write(''.join(random.choice(b1) for b4 in range(length)))
def fonk2(b8, b9, b10, b11):
    b3 = [[0 for x in range(b11+1)] for x in range(b10+1)]
    for b4 in range(b10+1):
        for b7 in range(b11+1):
            if b4 = = 0 or b7 == 0:
                b3[b4][b7] = 0
            elif b8[b4-1] == b9[b7-1]:
                b3[b4][b7] = b3[b4-1][b7-1] + 1
            else:
                b3[b4][b7] = max(b3[b4-1][b7], b3[b4][b7-1])
    b5 = b3[b10][b11]
    b6 = [""] * (b5+1)
    b6[b5] = ""
    b4 = b10
    b7 = b11
    while b4 > 0 and b7 > 0:
        if b8[b4-1] == b9[b7-1]:
            b6[b5-1] = b8[b4-1]
            b4-=1
            b7-=1
            b5-=1
        elif b3[b4-1][b7] > b3[b4][b7-1]:
            b4-=1
        else:
            b7-=1
    print ("LCS of " + b8 + " and " + b9 + " is " + "".join(b6) )
    if(len(b6)>500):
    	print("Matching")
    else:
    	print("Not matching")
fonk1(1000)
b8 = (open("dna-sequence.txt","r").read())
b9 = (open("dna-sequence2.txt","r").read())
b10 = len(b8)
b11 = len(b9)
fonk2(b8, b9, b10, b11)