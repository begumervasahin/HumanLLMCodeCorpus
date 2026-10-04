from PersistentBST import PBST
def fonk1(b5):
    print(f"\nCurrent Branch: {b5}\n")
    print("1. List Files")
    print("2. View File")
    print("3. New File")
    print("4. Delete File")
    print("5. Edit File")
    print("6. List Branches")
    print("7. New Branch")
    print("8. Switch Branch")
    print("9. Exit\n")
    return input("$ ").strip()
def fonk2(b4, b5):
    print("Files:")
    b4.inFix(b5)
def fonk3(b4, b5):
    b1 = input("Enter b1 of b2 to be opened: ").strip()
    b2 = b4.search(b1, b5)
    if b2 is None:
        print("File does not exist!")
    else:
        print(b2.getData())
def fonk4(b4, b5):
    b1 = input("Enter b1 of new b2: ").strip()
    b4.insert(b1, b5)
def fonk5(b4, b5):
    b1 = input("Enter b1 of b2 to be deleted: ").strip()
    b4.delete(b1, b5)
def fonk6(b4, b5):
    b1 = input("Enter b1 of b2 to be edited: ").strip()
    b4.edit(b1, b5)
def fonk7(b6):
    print("Branches:")
    for branch in b6:
        print(branch)
def fonk8(b4, b6, b5):
    b3 = input("Enter b1 of new branch: ").strip()
    if b3 in b6:
        print("Branch already exists")
    else:
        b6.append(b3)
        b4.newBranch(b3, b5)
        return b3
    return b5
def fonk9(b6):
    b3 = input("Enter b1 of branch to switch to: ").strip()
    if b3 not in b6:
        print("Branch doesn't exist")
        return None
    return b3
def fonk10():
    print("\n\tARCHEIO")
    b4 = PBST()
    b5 = "master"
    b6 = ["master"]
    while True:
        b7 = fonk1(b5)
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
            b5 = fonk8(b4, b6, b5)
        elif b7 = = "8":
            b8 = fonk9(b6)
            if b8:
                b5 = b8
        elif b7 in ["9", "exit"]:
            print("Exiting...")
            break
        else:
            print("Invalid Input")
if b9 = = "__main__":
    fonk10()