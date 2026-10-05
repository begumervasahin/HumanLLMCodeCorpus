import queue as b2
def fonk1(b3):
    b1 = b3.qsize()
    while b1>0:
        b2 = b3.get()
        print(b2)
        b3.put(b2)
        b1-=1
b3 = b2.Queue()
print("MENU:\n1.EnQueue\n2.DeQueue\n3.LengthOfQueue\n4.Check Queue Emptiness\n5.Display Queue\n6.EXIT")
b4 = int(input("Enter Your Choise=  "))
while b4<=5:
    if (b4 = =1):
        b5 = int(input("Enter b6 To Be Inserted Into  Queue=  "))
        b3.put(b5)
        print("Value ",b5,"  Inserted")
    elif (b4 = =2):
          if b3.qsize()==0:
              print("Queue Is Empty, Cannot Delete b6  !!! ")
          else:
              print("Removed b6 = ",b3.get())
    elif (b4 = =3):
        b7 = b3.qsize()
        print("Number Of Elements In The Queue b8 = ",b7)
    elif (b4 = =4):
         if (b3.qsize()==0):
            print("Queue Is Empty")
         else:
            print("Queue Is Not Empty")
    elif (b4 = =5):
            fonk1(b3)
            print("End")
    b4 = int(input("Enter Your Next Choise=  "))
print("INVALID INPUT ,Execution Stopped\nYOU HAVE TO RUN AGAIN!!!!!!")