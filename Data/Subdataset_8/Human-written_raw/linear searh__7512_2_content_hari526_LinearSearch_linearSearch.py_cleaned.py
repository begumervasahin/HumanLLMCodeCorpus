def linearSearch(myItem,myList):
    found= False
    position=0
    while position < len(myList) and not found:
        if myList[position]== myItem:
            found = True
        position= position+1
    return found
if __name__== "__main__":
    shopping = ["apples","bananas","chocolate","pasta"]
    item = input( "what item do you want to search : ")
    isitFound = linearSearch(item,shopping)
    if isitFound:
        print("Item is in the list !")
    else:
        print("Item is not in the list !")