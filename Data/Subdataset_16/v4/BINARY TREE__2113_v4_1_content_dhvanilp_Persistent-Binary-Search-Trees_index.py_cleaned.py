from PersistentBST import PBST
def fonk1():
    print("\n\tARCHEIO")
    b1 = PBST()
    b2 = "master"
    b3 = None
    b4 = ["master"]
    while True:
        print("\nCurrent Branch:", b2)
        print("\n1. List Files\n2. View File\n3. New File\n4. Delete File\n5. Edit File\n6. List Branches\n7. New "
              "Branch\n8. Switch Branch\n9. Exit\n")
        b5 = input("$ ").strip()
        print()
        if b5 = = "1":
            print("Files:")
            b1.inFix(b2)
        elif b5 = = "2":
            b6 = input("Enter b6 of b7 to be opened: ").strip()
            b7 = b1.search(b6, b2)
            if b7 is None:
                print("File does not exist!")
            else:
                print(b7.getData())
        elif b5 = = "3":
            b6 = input("Enter b6 of new b7: ").strip()
            b1.insert(b6, b2)
        elif b5 = = "4":
            b6 = input("Enter b6 of b7 to be deleted: ").strip()
            b1.delete(b6, b2)
        elif b5 = = "5":
            b6 = input("Enter b6 of b7 to be edited: ").strip()
            b1.edit(b6, b2)
        elif b5 = = "6":
            print("Branches:")
            for branch in b4:
                print(branch)
        elif b5 = = "7":
            b8 = input("Enter b6 of new branch: ").strip()
            if b8 in b4:
                print("Branch already exists")
            else:
                b4.append(b8)
                b3, b2 = b2, b8
                b1.newBranch(b2, b3)
        elif b5 = = "8":
            b8 = input("Enter b6 of branch to switch to: ").strip()
            if b8 not in b4:
                print("Branch doesn't exist")
            else:
                b3, b2 = b2, b8
        elif b5 in ["9", "exit"]:
            print("Exiting...")
            break
        elif b5 = = "debug":
            print()
        else:
            print("Invalid Input")
if b9 = = "__main__":
    fonk1()