import pymongo
import csv
b1 = pymongo.MongoClient()
b2 = b1["projectOne"]
b3 = b2["Users"]
b4 = b2["Organizations"]
b5 = b2["Interests"]
b6 = b2["Projects"]
b7 = b2["Skills"]
def fonk1():
    b1 = pymongo.MongoClient()
    b2 = b1["projectOne"]
    b3 = b2["Users"]
    b4 = b2["Organizations"]
    b5 = b2["Interests"]
    b6 = b2["Projects"]
    b7 = b2["Skills"]
    while True:
        b8 = input("\nWould you like to search for a user (y/n):  ").strip().lower()
        if b8 = = 'y':
            b9 = input("Enter the User ID: ").strip()
            fonk2(b9)
        else:
            break
def fonk2(b9):
    b9 = str(b9)
    if b3.count_documents({"User_id": b9}) == 0:
        print("This user does not exist. Please try another userID.")
    else:
        b10 = b3.find({"User_id": b9})
        b11 = b4.find({"User_id": b9})
        b12 = b5.find({"User_id": b9})
        b13 = b7.find({"User_id": b9})
        b14 = b6.find({"User_id": b9})
        for u in b10:
            print(f"\tName: {u['First name']} {u['Last name']}")
        for o in b11:
            print(f"\tWorks at: {o['Organization']}")
        b15 = ""
        for i in b12:
            if isinstance(i["Interest"], list):
                b15 += ", ".join([f"{interest} ({level})" for interest, level in zip(i["Interest"], i["Interest level"])])
            else:
                b15 = f"{i['Interest']} ({i['Interest level']})"
        print(f"\tInterest: {b15}")
        b16 = ""
        for sk in b13:
            if isinstance(sk["Skill"], list):
                b16 += ", ".join([f"{skill} ({level})" for skill, level in zip(sk["Skill"], sk["Skill level"])])
            else:
                b16 = f"{sk['Skill']} ({sk['Skill level']})"
        print(f"\tSkill: {b16}")
        b17 = ""
        for p in b14:
            if isinstance(p["Project"], list):
                b17 += ", ".join(p["Project"])
            else:
                b17 = p["Project"]
        print(f"\tWorks on: {b17}")
def fonk3(file_name):
    with open(file_name, 'r') as r_file:
        b18 = csv.reader(r_file)
        b19 = next(b18)
        b20 = []
        for rows in b18:
            b21 = {b19[i]: rows[i] for i in range(len(b19))}
            b20.append(b21)
    return b20
def fonk4(collection_name, entries):
    collection_name.create_index("User_id", b22 = True)
    for b23 in entries:
        try:
            collection_name.insert_one(b23)
        except pymongo.errors.DuplicateKeyError:
            print(f"Duplicate entry: {b23}")
            pass
def fonk5(b27):
    fonk4(b3, fonk3(b27[0]))
    fonk4(b4, fonk3(b27[1]))
    fonk4(b6, fonk6(b27[2], "project"))
    fonk4(b5, fonk6(b27[3], "interest"))
    fonk4(b7, fonk6(b27[4], "skill"))
def fonk6(file_name, b24):
    with open(file_name, 'r') as r_file:
        b18 = csv.reader(r_file)
        b19 = next(b18)
        b20 = []
        for rows in b18:
            b23 = {b19[i]: rows[i] for i in range(len(b19))}
            if fonk7(b23, b20, b24):
                b20.append(b23)
    return b20
def fonk7(info, arr, b24):
    for elements in arr:
        if elements["User_id"] == info["User_id"]:
            if b24 = = "interest":
                if not isinstance(elements["Interest"], list):
                    elements["Interest"] = [elements["Interest"], info["Interest"]]
                    elements["Interest level"] = [elements["Interest level"], info["Interest level"]]
                else:
                    if info["Interest"] not in elements["Interest"]:
                        elements["Interest"].append(info["Interest"])
                        elements["Interest level"].append(info["Interest level"])
            elif b24 = = "skill":
                if not isinstance(elements["Skill"], list):
                    elements["Skill"] = [elements["Skill"], info["Skill"]]
                    elements["Skill level"] = [elements["Skill level"], info["Skill level"]]
                else:
                    if info["Skill"] not in elements['Skill']:
                        elements["Skill"].append(info["Skill"])
                        elements["Skill level"].append(info["Skill level"])
            elif b24 = = "project":
                if not isinstance(elements["Project"], list):
                    elements["Project"] = [elements["Project"], info["Project"]]
                else:
                    if info["Project"] not in elements['Project']:
                        elements["Project"].append(info["Project"])
            return False
    return True
def fonk8():
    b1.drop_database("projectOne")
if b25 = = "__main__":
    fonk1()
    while True:
        b26 = input("\nDo you want to load b23 from files? (yes/no): ").strip().lower()
        if b26 = = "yes":
            b27 = [
                "b3.csv",
                "b4.csv",
                "b6.csv",
                "b5.csv",
                "b7.csv"
            ]
            fonk5(b27)
        else:
            print("Exiting...")
            break