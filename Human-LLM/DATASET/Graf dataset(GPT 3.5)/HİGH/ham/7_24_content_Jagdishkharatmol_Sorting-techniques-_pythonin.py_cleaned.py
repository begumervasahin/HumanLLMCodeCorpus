import time
b1 = '_'*80
print(f"{b1} \b7")
b2 = "Sort techniques on dataset"
print(b2.center(80))
print(f"\b7{b1}\b7\b7")
while True:
          print("Enter \b7 1 for bubble sort \b7 2 for insertion sort \b7 3 for merge sort \b7 4 for selection sort")
          b3 = int(input("\b7 Enter the choice"))
          if b3 = =1:
              b4 = time.time()
              def fonk1(b6):
                 for a2 in range(len(b6)-1,0,-1):
                     for a1 in range(a2):
                         if b6[a1]>b6[a1+1]:
                            b5 = b6[a1]
                            b6[a1] = b6[a1+1]
                            b6[a1+1] = b5
              b6 = []
              b7 = int(input(" \b7 How many number do you want to enter"))
              for a1 in range(b7):
                 b8 = int(input(" Enter the number"))
                 b6.append(b8)
              fonk1(b6)
              print("\b7 The list after bubble sorting is {}".format(b6))
              b9 = time.time()
              print(" The time taken by sorting process",b9 - b4)
          if b3 = =2:
              b4 = time.time()
              def fonk2(b6):
                  for a1 in range(1,len(b6)):
                      b10 = b6[a1]
                      b11 = a1
                      while b11>0 and b6[b11-1]>b10:
                            b6[b11]=b6[b11-1]
                            b11 = b11-1
                            b6[b11]=b10
              b6 = []
              b7 = int(input(" \b7 How many number do you want to enter:"))
              for a1 in range(b7):
                 b8 = int(input(" Enter the number:"))
                 b6.append(b8)
              fonk2(b6)
              print("\b7 The list after insertion sorting is {}".format(b6))
              b9 = time.time()
              print(" The time taken by sorting process :",b9 - b4)
          if b3 = =3:
              b4 = time.time()
              def fonk3(b15):
                 if len(b15)>1:
                     b12 = len(b15)
                     b13 = b15[:b12]
                     b14 = b15[b12:]
                     fonk3(b13)
                     fonk3(b14)
                     a1 = 0
                     a2 = 0
                     a3 = 0
                     while a1 < len(b13) and a2 < len(b14):
                          if b13[a1] < b14[a2]:
                             b15[a3]=b13[a1]
                             a1 = a1+1
                          else:
                               b15[a3]=b14[a2]
                               a2 = a2+1
                          a3 = a3+1
                     while a1 < len(b13):
                           b15[a3]=b13[a1]
                           a1 = a1+1
                           a3 = a3+1
                     while a2 < len(b14):
                           b15[a3]=b14[a2]
                           a2 = a2+1
                           a3 = a3+1
              b15 = []
              b7 = int(input(" \b7 How many number do you want to enter:"))
              for a1 in range(b7):
                 b8 = int(input(" Enter the number:"))
                 b15.append(b8)
              fonk3(b15)
              print("\b7 The list after merge sorting is {}".format(b15))
              b9 = time.time()
              print(" The time taken by sorting process :",b9 - b4)
          if b3 = =4:
              b4 = time.time()
              def fonk4(b6):
                   for fillslot in range(len(b6)-1,0,-1):
                       a4 = 0
                       for location in range(1,fillslot+1):
                          if b6[location]>b6[a4]:
                             a4 = location
                          b5 = b6[fillslot]
                          b6[fillslot] = b6[a4]
                          b6[a4] = b5
              b6 = []
              b7 = int(input(" \b7 How many number do you want to enter:"))
              for a1 in range(b7):
                 b8 = int(input(" Enter the number"))
                 b6.append(b8)
              fonk4(b6)
              print("\b7 The list after selection sorting is {}".format(b6))
              b9 = time.time()
              print(" The time taken by sorting process:",b9 - b4)
          b7 = int(input(" Enter 1 to continue and 0 to exit:"))
          print(" \b7 \b7 ")
          if b7 = =0:
             break