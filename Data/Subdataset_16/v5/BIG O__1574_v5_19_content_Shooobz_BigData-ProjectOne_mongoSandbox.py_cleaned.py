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
    while True:
        b8 = input("\nWould you like to search for a user (y/n): ").strip().lower()
        if b8 = = 'y':
            b9 = input("Enter user ID: ").strip()
            fonk2(b9)
        else:
            break
def fonk2(b9):
    if b3.count_documents({"User_id": b9}) == 0:
        print("This user does not exist. Please try another user ID.")
        return
    b10 = b3.find({"User_id": b9})
    b11 = b4.find({"User_id": b9})
    b12 = b5.find({"User_id": b9})
    b13 = b7.find({"User_id": b9})
    b14 = b6.find({"User_id": b9})
    for user in b10:
        print(f"\tName: {user['First name']} {user['Last name']}")
    for org in b11:
        print(f"\tWorks at: {org['organization']}")
    b15 = fonk3(b12, "Interest", "Interest level")
    print(f"\tInterests: {b15}")
    b16 = fonk3(b13, "Skill", "Skill level")
    print(f"\tSkills: {b16}")
    b17 = fonk4(b14)
    print(f"\tWorks on: {b17}")
def fonk3(results, b27, level_key):
    b18 = ""
    for item in results:
        if isinstance(item[b27], list):
            for i in range(len(item[b27])):
                b18 += f"{item[b27][i]} ({item[level_key][i]}), "
        else:
            b18 += f"{item[b27]} ({item[level_key]})"
    return b18.strip(', ')
def fonk4(results):
    b18 = ""
    for project in results:
        if isinstance(project["Project"], list):
            for p in project["Project"]:
                b18 += f"{p}, "
        else:
            b18 += project["Project"]
    return b18.strip(', ')
def fonk5(file_name):
    with open(file_name, b19 = 'r') as file:
        b20 = csv.reader(file)
        b21 = next(b20)
        b22 = [{b21[i]: row[i] for i in range(len(b21))} for row in b20]
    return b22
def fonk6(b18, entries):
    b18.create_index("User_id", b23 = True)
    for b26 in entries:
        try:
            b18.insert_one(b26)
        except pymongo.errors.DuplicateKeyError:
            print(f"Duplicate entry found for User_id: {b26['User_id']}")
def fonk7(csv_files):
    fonk6(b3, fonk5(csv_files[0]))
    fonk6(b4, fonk5(csv_files[1]))
    fonk6(b6, fonk8(csv_files[2], "project"))
    fonk6(b5, fonk8(csv_files[3], "interest"))
    fonk6(b7, fonk8(csv_files[4], "skill"))
def fonk8(file_name, b25):
    with open(file_name, b19 = 'r') as file:
        b20 = csv.reader(file)
        b21 = next(b20)
        b22 = []
        b24 = [("User_id", pymongo.ASCENDING), (b25.capitalize(), pymongo.DESCENDING)]
        if b25 = = "interest":
            b5.create_index(b24, b23 = True)
        elif b25 = = "skill":
            b7.create_index(b24, b23 = True)
        for row in b20:
            b26 = {b21[i]: row[i] for i in range(len(b21))}
            if fonk9(b26, b22, b25):
                b22.append(b26)
    return b22
def fonk9(info, data_list, b25):
    for element in data_list:
        if element["User_id"] == info["User_id"]:
            b27 = b25.capitalize()
            if not isinstance(element[b27], list):
                element[b27] = [element[b27], info[b27]]
                element[f"{b27} level"] = [element[f"{b27} level"], info[f"{b27} level"]]
            else:
                if info[b27] not in element[b27]:
                    element[b27].append(info[b27])
                    element[f"{b27} level"].append(info[f"{b27} level"])
            return False
    return True
def fonk10():
    b1.drop_database("projectOne")
if b28 = = "__main__":
    fonk1()