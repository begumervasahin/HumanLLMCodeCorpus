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
        b8 = input("\nWould you like to search for a user (y/n): ").lower()
        if b8 = = 'y':
            b9 = input("Enter the b9: ")
            fonk2(b9)
        else:
            break
def fonk2(b9):
    b10 = b3.find_one({"User_id": b9})
    if not b10:
        print("This user does not exist. Please try another b9.")
    else:
        fonk3(b10)
        fonk4(b9)
        fonk5(b9)
        fonk6(b9)
        fonk7(b9)
def fonk3(b10):
    print(f"\tName: {b10['First name']} {b10['Last name']}")
def fonk4(b9):
    b11 = b4.find({"User_id": b9})
    for org in b11:
        print(f"\tWorks at: {org['organization']}")
def fonk5(b9):
    b12 = b5.find({"User_id": b9})
    b13 = ", ".join([f"{i['Interest']}({i['Interest level']})" for i in b12])
    print(f"\tInterest: {b13}")
def fonk6(b9):
    b14 = b7.find({"User_id": b9})
    b15 = ", ".join([f"{sk['Skill']}({sk['Skill level']})" for sk in b14])
    print(f"\tSkill: {b15}")
def fonk7(b9):
    b16 = b6.find({"User_id": b9})
    b17 = ", ".join([p['Project'] for p in b16])
    print(f"\tWorks on: {b17}")
def fonk8(file_name):
    with open(file_name) as f:
        b18 = csv.DictReader(f)
        return list(b18)
def fonk9(collection_name, entries):
    collection_name.create_index("User_id", b19 = True)
    for data in entries:
        try:
            collection_name.insert_one(data)
        except pymongo.errors.DuplicateKeyError:
            print(f"Duplicate entry found for {data['User_id']}. Skipping insertion.")
def fonk10(csvfiles):
    fonk9(b3, fonk8(csvfiles[0]))
    fonk9(b4, fonk8(csvfiles[1]))
    fonk9(b6, fonk8(csvfiles[2]))
    fonk9(b5, fonk8(csvfiles[3]))
    fonk9(b7, fonk8(csvfiles[4]))
def fonk11():
    b1.drop_database("projectOne")
if b20 = = "__main__":
    fonk1()