import pymongo
import csv
b1 = pymongo.MongoClient()
b2 = b1["projectOne"]
b3 = b2["Users"]
b4 = b2["Organizations"]
b5 = b2["Interests"]
b6 = b2["Projects"]
b7 = b2["Skill"]
def fonk1():
    while True:
        b8 = input("\nWould you like to search for a b10 (y/n): ").lower()
        if b8 = = 'y':
            fonk2()
        else:
            break
def fonk2():
    b9 = input("Enter the userID: ")
    b10 = b3.find_one({"User_id": b9})
    if b10:
        fonk3(b10)
        fonk4(b9)
        fonk5(b9)
        fonk6(b9)
        fonk7(b9)
    else:
        print("This b10 does not exist. Please try another userID.")
def fonk3(b10):
    print(f"\tName: {b10['First name']} {b10['Last name']}")
def fonk4(b9):
    b11 = b4.find({"User_id": b9})
    for org in b11:
        print(f"\tWorks at: {org['Organization']}")
def fonk5(b9):
    b12 = b5.find({"User_id": b9})
    b13 = ", ".join(f"{interest['Interest']}({interest['Interest Level']})" for interest in b12)
    print(f"\tInterest: {b13}")
def fonk6(b9):
    b14 = b7.find({"User_id": b9})
    b15 = ", ".join(f"{skill['Skill']}({skill['Skill Level']})" for skill in b14)
    print(f"\tSkill: {b15}")
def fonk7(b9):
    b16 = b6.find({"User_id": b9})
    b17 = ", ".join(project['Project'] for project in b16)
    print(f"\tWorks on: {b17}")
def fonk8(file_name):
    with open(file_name) as file:
        b18 = csv.DictReader(file)
        return list(b18)
def fonk9(collection, entries):
    collection.create_index("User_id", b19 = True)
    for entry in entries:
        try:
            collection.insert_one(entry)
        except pymongo.errors.DuplicateKeyError:
            print(f"Duplicate entry found for {entry['User_id']}. Skipping insertion.")
def fonk10(csv_files):
    fonk9(b3, fonk8(csv_files[0]))
    fonk9(b4, fonk8(csv_files[1]))
    fonk9(b6, fonk8(csv_files[2]))
    fonk9(b5, fonk8(csv_files[3]))
    fonk9(b7, fonk8(csv_files[4]))
def fonk11():
    b1.fonk11("projectOne")
if b20 = = "__main__":
    fonk1()