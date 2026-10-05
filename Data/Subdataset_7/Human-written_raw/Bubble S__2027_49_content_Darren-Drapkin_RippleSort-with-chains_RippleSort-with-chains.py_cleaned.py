b1 = ["","","ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
b2 = ["", "","FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
b3 = [0,0]
 def fonk1():
    for index in range(2,len(b1)+1):
        if gender[index]=="FEMALE":
            a1 = 0
            b3[index] = b3[a1]
            b3[a1] = index
        if gender[index]=="MALE":
            a1 = 1
            b3[index] = b3[a1]
            b3[a1] = index
def fonk2():
    for index in range(2,len(b1)+1):
        b4 = false
        b5 = b3[0]
        for index1 in range(2,len(b1)+1-index):
            b6 = b5
            b5 = b3[b5]
            b7 = b3[b5]
            if b1[b5]>= b1[b7]:
                b4 = true
                b8 = b3[b6]
                b3[b6] = b3[b5]
                b3[currrent] = b3[b7]
                b3[b7] = b8
                b5 = b7
        b4 = false
        if not b4 :
            return