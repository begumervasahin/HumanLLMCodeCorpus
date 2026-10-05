while True:
    print('Enter ** YES ** for Run the Searching program :: ',end='')
    n=eval(input())
    if n=='YES':
        def linearSearch(mylist,search_Num):
            for i in range (0,len(mylist),1):
                if mylist[i] == search_Num:
                    found = True
                    return found
        if __name__=='__main__':
            print('Enter  anything you  want to see in your list: ',end='')
            li =[eval(num)for num in input().split()]
            print('\n\n\t **********************************************************\n\nyour list is : ',end='')
            print(li)
            num = eval(input('\n\n    Search what are you looking for => '))
            found = False
            Trace=linearSearch(li,num)
            if Trace:
                print('\n\t',num,'is found in the index number ',li.index(num))
            else:
                print('\n\t\t',num,'isn\'t in the list.Better luck next time.\n\t(If you want to search another thing than please search again Otherwise type 0 for exit)')
    else:
        break
        def linearSearch(mylist,search_Num):
            for i in range (0,len(mylist),1):
                if mylist[i] == search_Num:
                    found = True
                    return found
    if __name__=='__main__':
        print('Enter  anything you  want to see in your list: ',end='')
        li =[eval(num)for num in input().split()]
        print('\n\n\t **********************************************************\n\nyour list is : ',end='')
        print(li)
        num = eval(input('\n\n    Search what are you looking for => '))
        found = False
        Trace=linearSearch(li,num)
        if Trace:
            print('\n\t',num,'is found in the index number ',li.index(num))
        else:
            print('\n\t\t',num,'isn\'t in the list.Better luck next time.\n\t(If you want to search another thing than please search again Otherwise type 0 for exit)')