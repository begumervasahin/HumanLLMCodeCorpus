from PersistentBST import PersistentBinarySearchTree
def fonk1(b5, b6):
    print("\nCurrent Branch:", b5)
    print("\n1. List Files\n2. View File\n3. New File\n4. Delete File\n5. Edit File\n6. List Branches\n7. New Branch\n8. Switch Branch\n9. Exit\n")
def fonk2(b4, b5):
    print("Files: ")
    b4.inFix(b5)
def fonk3(b4, b5):
    b1 = input("Enter b1 of b2 to be opened: ")
    b2 = b4.search(b1, b5)
    if b2 is None:
        print("File does not exist!")
    else:
        print(b2.getData())
def fonk4(b4, b5):
    b1 = input("Enter b1 of new b2: ")
    b4.insert(b1, b5)
def fonk5(b4, b5):
    b1 = input("Enter b1 of b2 to be deleted: ")
    b4.delete(b1, b5)
def fonk6(b4, b5):
    b1 = input("Enter b1 of b2 to be edited: ")
    b4.edit(b1, b5)
def fonk7(b6):
    print("Branches:")
    for branch in b6:
        print(branch)
def fonk8(b4, b5, b6):
    b3 = input("Enter b1 of new branch: ")
    if b3 in b6:
        print("Branch already exists")
        return
    b6.append(b3)
    b4.newBranch(b3, b5)
    return b3
def fonk9(b5, b6):
    b3 = input("Enter b1 of branch to switch to: ")
    if b3 not in b6:
        print("Branch doesn't exist")
        return b5
    return b3
def fonk10():
    print("\n\tARCHEIO")
    b4 = PersistentBinarySearchTree()
    b5 = "master"
    b6 = ["master"]
    while True:
        fonk1(b5, b6)
        b7 = input("$ ").lower()
        print()
        if b7 = = "1":
            fonk2(b4, b5)
        elif b7 = = "2":
            fonk3(b4, b5)
        elif b7 = = "3":
            fonk4(b4, b5)
        elif b7 = = "4":
            fonk5(b4, b5)
        elif b7 = = "5":
            fonk6(b4, b5)
        elif b7 = = "6":
            fonk7(b6)
        elif b7 = = "7":
            b5 = fonk8(b4, b5, b6)
        elif b7 = = "8":
            b5 = fonk9(b5, b6)
        elif b7 = = "exit" or b7 == "9":
            print("Exiting...")
            break
        elif b7 = = "debug":
            print()
        else:
            print("Invalid Input")
if b8 = = "__main__":
    fonk10()