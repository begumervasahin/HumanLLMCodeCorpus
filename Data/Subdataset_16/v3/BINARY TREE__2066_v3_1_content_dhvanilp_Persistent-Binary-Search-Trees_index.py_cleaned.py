class class1:
    def fonk1(self, b2, b1 = ''):
        self.b2 = b2
        self.b1 = b1
    def fonk2(self):
        return self.b1
    def fonk3(self, b1):
        self.b1 = b1
class class2:
    def fonk4(self, b3, b1 = ''):
        self.b3 = b3
        self.b1 = class1(b3, b1)
        self.b4 = None
        self.b5 = None
class class3:
    def fonk5(self):
        self.b6 = {'master': None}
    def fonk6(self, b3, b7 = 'master'):
        b8 = self.b6.get(b7)
        while b8:
            if b3 < b8.b3:
                b8 = b8.b4
            elif b3 > b8.b3:
                b8 = b8.b5
            else:
                return b8.b1
        return None
    def fonk7(self, b3, b7 = 'master'):
        if b7 not in self.b6:
            print("Branch doesn't exist")
            return
        b8 = self.b6[b7]
        b9 = None
        while b8:
            b9 = b8
            if b3 < b8.b3:
                b8 = b8.b4
            elif b3 > b8.b3:
                b8 = b8.b5
            else:
                print("File already exists!")
                return
        b10 = class2(b3)
        if b9 is None:
            self.b6[b7] = b10
        else:
            if b3 < b9.b3:
                b9.b4 = b10
            else:
                b9.b5 = b10
    def fonk8(self, b3, b7 = 'master'):
        if b7 not in self.b6:
            print("Branch doesn't exist")
            return
        self.b6[b7], b11 = self.fonk9(self.b6[b7], b3)
        if b11:
            print("File b11")
        else:
            print("File not found")
    def fonk9(self, b8, b3):
        if b8 is None:
            return b8, False
        if b3 < b8.b3:
            b8.b4, b11 = self.fonk9(b8.b4, b3)
        elif b3 > b8.b3:
            b8.b5, b11 = self.fonk9(b8.b5, b3)
        else:
            if b8.b4 is None:
                return b8.b5, True
            elif b8.b5 is None:
                return b8.b4, True
            b12 = self.fonk10(b8.b5)
            b8.b3, b8.b1 = b12.b3, b12.b1
            b8.b5, b13 = self.fonk9(b8.b5, b12.b3)
            return b8, True
        return b8, b11
    def fonk10(self, b8):
        b14 = b8
        while b14.b4:
            b14 = b14.b4
        return b14
    def fonk11(self, b3, b7 = 'master'):
        b15 = self.fonk6(b3, b7)
        if b15 is None:
            print("File does not exist!")
        else:
            b16 = input("Enter new b1 for the b15: ")
            b15.fonk3(b16)
    def fonk12(self, b7 = 'master'):
        if b7 not in self.b6:
            print("Branch doesn't exist")
            return
        self.fonk13(self.b6[b7])
        print()
    def fonk13(self, b8):
        if b8:
            self.fonk13(b8.b4)
            print(b8.b3, b17 = " ")
            self.fonk13(b8.b5)
    def fonk14(self, new_branch, base_branch):
        if base_branch not in self.b6:
            print("Base b7 doesn't exist")
            return
        self.b6[new_branch] = self.b6[base_branch]
if b18 = = "__main__":
    b19 = class3()
    b20 = "master"
    b6 = ["master"]
    print("\n\tARCHEIO")
    while True:
        print(f"\nCurrent Branch: {b20}")
        print("\n1. List Files\n2. View File\n3. New File\n4. Delete File\n5. Edit File\n6. List Branches\n7. New Branch\n8. Switch Branch\n9. Exit\n")
        b21 = input("$ ").strip()
        print()
        if b21 = = "1":
            print("Files: ")
            b19.fonk12(b20)
        elif b21 = = "2":
            b2 = input("Enter b2 of b15 to be opened: ").strip()
            b15 = b19.fonk6(b2, b20)
            if b15 is None:
                print("File does not exist!")
            else:
                print(b15.fonk2())
        elif b21 = = "3":
            b2 = input("Enter b2 of new b15: ").strip()
            b19.fonk7(b2, b20)
        elif b21 = = "4":
            b2 = input("Enter b2 of b15 to be b11: ").strip()
            b19.fonk8(b2, b20)
        elif b21 = = "5":
            b2 = input("Enter b2 of b15 to be edited: ").strip()
            b19.fonk11(b2, b20)
        elif b21 = = "6":
            print("Branches:")
            for b7 in b6:
                print(b7)
        elif b21 = = "7":
            b22 = input("Enter b2 of new b7: ").strip()
            if b22 in b6:
                print("Branch already exists")
                continue
            b6.append(b22)
            b19.fonk14(b22, b20)
        elif b21 = = "8":
            b22 = input("Enter b2 of b7 to switch to: ").strip()
            if b22 not in b6:
                print("Branch doesn't exist")
                continue
            b20 = b22
        elif b21 = = "exit" or b21 == "9":
            print("Exiting...")
            break
        else:
            print("Invalid Input")