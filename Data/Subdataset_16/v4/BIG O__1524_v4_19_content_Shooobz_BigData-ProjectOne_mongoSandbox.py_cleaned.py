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
    b15 = ""
    for interest in b12:
        if isinstance(interest["Interest"], list):
            for i in range(len(interest["Interest"])):
                b15 += f"{interest['Interest'][i]} ({interest['Interest level'][i]}), "
        else:
            b15 = f"{interest['Interest']} ({interest['Interest level']})"
    print(f"\tInterests: {b15}")
    b16 = ""
    for skill in b13:
        if isinstance(skill["Skill"], list):
            for i in range(len(skill["Skill"])):
                b16 += f"{skill['Skill'][i]} ({skill['Skill level'][i]}), "
        else:
            b16 = f"{skill['Skill']} ({skill['Skill level']})"
    print(f"\tSkills: {b16}")
    b17 = ""
    for project in b14:
        if isinstance(project["Project"], list):
            for p in project["Project"]:
                b17 += f"{p}, "
        else:
            b17 = project["Project"]
    print(f"\tWorks on: {b17}")
def fonk3(file_name):
    with open(file_name, b18 = 'r') as file:
        b19 = csv.reader(file)
        b20 = next(b19)
        b21 = []
        for row in b19:
            b22 = {b20[i]: row[i] for i in range(len(b20))}
            b21.append(b22)
    return b21
def fonk4(collection, entries):
    collection.create_index("User_id", b23 = True)
    for b25 in entries:
        try:
            collection.insert_one(b25)
        except Exception as e:
            print(f"Error inserting b25: {b25}, Error: {e}")
def fonk5(csv_files):
    fonk4(b3, fonk3(csv_files[0]))
    fonk4(b4, fonk3(csv_files[1]))
    fonk4(b6, fonk6(csv_files[2], "project"))
    fonk4(b5, fonk6(csv_files[3], "interest"))
    fonk4(b7, fonk6(csv_files[4], "skill"))
def fonk6(file_name, b24):
    with open(file_name, b18 = 'r') as file:
        b19 = csv.reader(file)
        b20 = next(b19)
        b21 = []
        if b24 = = "interest":
            b5.create_index([("User_id", pymongo.ASCENDING), ("Interest", pymongo.DESCENDING)], b23 = True)
        elif b24 = = "skill":
            b7.create_index([("User_id", pymongo.ASCENDING), ("Skill", pymongo.DESCENDING)], b23 = True)
        for row in b19:
            b25 = {b20[i]: row[i] for i in range(len(b20))}
            if fonk7(b25, b21, b24):
                b21.append(b25)
    return b21
def fonk7(info, data_list, b24):
    for element in data_list:
        if element["User_id"] == info["User_id"]:
            if b24 = = "interest":
                if not isinstance(element["Interest"], list):
                    element["Interest"] = [element["Interest"], info["Interest"]]
                    element["Interest level"] = [element["Interest level"], info["Interest level"]]
                else:
                    if info["Interest"] not in element["Interest"]:
                        element["Interest"].append(info["Interest"])
                        element["Interest level"].append(info["Interest level"])
            elif b24 = = "skill":
                if not isinstance(element["Skill"], list):
                    element["Skill"] = [element["Skill"], info["Skill"]]
                    element["Skill level"] = [element["Skill level"], info["Skill level"]]
                else:
                    if info["Skill"] not in element["Skill"]:
                        element["Skill"].append(info["Skill"])
                        element["Skill level"].append(info["Skill level"])
            elif b24 = = "project":
                if not isinstance(element["Project"], list):
                    element["Project"] = [element["Project"], info["Project"]]
                else:
                    if info["Project"] not in element["Project"]:
                        element["Project"].append(info["Project"])
            return False
    return True
def fonk8():
    b1.drop_database("projectOne")
if b26 = = "__main__":
    fonk1()