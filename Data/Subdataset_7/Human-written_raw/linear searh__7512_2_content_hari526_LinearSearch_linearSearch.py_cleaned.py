def fonk1(myItem,myList):
    b1 = False
    a1 = 0
    while a1 < len(myList) and not b1:
        if myList[a1]== myItem:
            b1 = True
        a1 = a1+1
    return b1
if b2 = = "__main__":
    b3 = ["apples","bananas","chocolate","pasta"]
    b4 = input( "what b4 do you want to search : ")
    b5 = fonk1(b4,b3)
    if b5:
        print("Item is in the list !")
    else:
        print("Item is not in the list !")