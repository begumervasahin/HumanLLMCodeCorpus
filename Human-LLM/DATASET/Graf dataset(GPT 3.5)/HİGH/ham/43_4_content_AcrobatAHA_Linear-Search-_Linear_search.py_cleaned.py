while True:
    print('Enter ** YES ** for Run the Searching program :: ',b1 = '')
    b2 = eval(input())
    if b2 = ='YES':
        def fonk1(mylist,search_Num):
            for i in range (0,len(mylist),1):
                if mylist[i] == search_Num:
                    b3 = True
                    return b3
        if b4 = ='__main__':
            print('Enter  anything you  want to see in your list: ',b1 = '')
            b5 = [eval(b6)for b6 in input().split()]
            print('\b2\b2\t **********************************************************\b2\nyour list is : ',b1 = '')
            print(b5)
            b6 = eval(input('\b2\b2    Search what are you looking for => '))
            b3 = False
            b7 = fonk2(b5,b6)
            if b7:
                print('\b2\t',b6,'is b3 in the index number ',b5.index(b6))
            else:
                print('\b2\t\t',b6,'isn\'t in the list.Better luck next time.\b2\t(If you want to search another thing than please search again Otherwise type 0 for exit)')
    else:
        break
        def fonk2(mylist,search_Num):
            for i in range (0,len(mylist),1):
                if mylist[i] == search_Num:
                    b3 = True
                    return b3
    if b4 = ='__main__':
        print('Enter  anything you  want to see in your list: ',b1 = '')
        b5 = [eval(b6)for b6 in input().split()]
        print('\b2\b2\t **********************************************************\b2\nyour list is : ',b1 = '')
        print(b5)
        b6 = eval(input('\b2\b2    Search what are you looking for => '))
        b3 = False
        b7 = fonk2(b5,b6)
        if b7:
            print('\b2\t',b6,'is b3 in the index number ',b5.index(b6))
        else:
            print('\b2\t\t',b6,'isn\'t in the list.Better luck next time.\b2\t(If you want to search another thing than please search again Otherwise type 0 for exit)')