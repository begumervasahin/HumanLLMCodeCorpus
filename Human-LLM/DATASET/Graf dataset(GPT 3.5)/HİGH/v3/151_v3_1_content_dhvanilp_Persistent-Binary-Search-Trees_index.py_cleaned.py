from PersistentBST import PersistentBST
def fonk1(b4):
    print("\nCurrent Branch:", b4)
    print("\n1. List Files\n2. View File\n3. New File\n4. Delete File\n5. Edit File\n6. List Branches\n7. New Branch\n8. Switch Branch\n9. Exit\n")
def fonk2(b5, b4):
    print("Files: ")
    b5.inFix(b4)
def fonk3(b5, b4):
    b1 = input("Enter b1 of b2 to be opened: ")
    b2 = b5.search(b1, b4)
    if b2 is None:
        print("File does not exist!")
    else:
        print(b2.getData())
def fonk4(b5, b4):
    b1 = input("Enter b1 of new b2: ")
    b5.insert(b1, b4)
def fonk5(b5, b4):
    b1 = input("Enter b1 of b2 to be deleted: ")
    b5.delete(b1, b4)
def fonk6(b5, b4):
    b1 = input("Enter b1 of b2 to be edited: ")
    b5.edit(b1, b4)
def fonk7(b6):
    print("Branches:")
    for branch in b6:
        print(branch)
def fonk8(b5, b6, b4):
    b3 = input("Enter b1 of new branch: ")
    if b3 in b6:
        print("Branch already exists")
    else:
        b6.append(b3)
        previous_branch, b4 = b4, b3
        b5.newBranch(b4, previous_branch)
def fonk9(b6, b4):
    b3 = input("Enter b1 of branch to switch to: ")
    if b3 not in b6:
        print("Branch doesn't exist")
    else:
        b4 = b3
    return b4
def fonk10():
    print("\n\tARCHEIO")
    b5 = PersistentBST()
    b4 = "master"
    b6 = ["master"]
    while True:
        fonk1(b4)
        b7 = input("$ ")
        print()
        if b7 = = "1":
            fonk2(b5, b4)
        elif b7 = = "2":
            fonk3(b5, b4)
        elif b7 = = "3":
            fonk4(b5, b4)
        elif b7 = = "4":
            fonk5(b5, b4)
        elif b7 = = "5":
            fonk6(b5, b4)
        elif b7 = = "6":
            fonk7(b6)
        elif b7 = = "7":
            fonk8(b5, b6, b4)
        elif b7 = = "8":
            b4 = fonk9(b6, b4)
        elif b7.lower() in ("exit", "9"):
            print("Exiting...")
            break
        elif b7.lower() == "debug":
            print()
        else:
            print("Invalid Input")
if b8 = = "__main__":
    fonk10()