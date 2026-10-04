import pymongo
import csv
client = pymongo.MongoClient()
db = client["projectOne"]
users = db["Users"]
organizations = db["Organizations"]
interests = db["Interests"]
projects = db["Projects"]
skills = db["Skills"]
def main():
    client = pymongo.MongoClient()
    db = client["projectOne"]
    users = db["Users"]
    organizations = db["Organizations"]
    interests = db["Interests"]
    projects = db["Projects"]
    skills = db["Skills"]
    while True:
        val = input("\nWould you like to search for a user (y/n):  ").strip().lower()
        if val == 'y':
            user_id = input("Enter the User ID: ").strip()
            look_up_user(user_id)
        else:
            break
def look_up_user(user_id):
    user_id = str(user_id)
    if users.count_documents({"User_id": user_id}) == 0:
        print("This user does not exist. Please try another userID.")
    else:
        user_results = users.find({"User_id": user_id})
        organization_results = organizations.find({"User_id": user_id})
        interests_results = interests.find({"User_id": user_id})
        skills_results = skills.find({"User_id": user_id})
        projects_results = projects.find({"User_id": user_id})
        for u in user_results:
            print(f"\tName: {u['First name']} {u['Last name']}")
        for o in organization_results:
            print(f"\tWorks at: {o['Organization']}")
        interest_collection = ""
        for i in interests_results:
            if isinstance(i["Interest"], list):
                interest_collection += ", ".join([f"{interest} ({level})" for interest, level in zip(i["Interest"], i["Interest level"])])
            else:
                interest_collection = f"{i['Interest']} ({i['Interest level']})"
        print(f"\tInterest: {interest_collection}")
        skill_collection = ""
        for sk in skills_results:
            if isinstance(sk["Skill"], list):
                skill_collection += ", ".join([f"{skill} ({level})" for skill, level in zip(sk["Skill"], sk["Skill level"])])
            else:
                skill_collection = f"{sk['Skill']} ({sk['Skill level']})"
        print(f"\tSkill: {skill_collection}")
        project_collection = ""
        for p in projects_results:
            if isinstance(p["Project"], list):
                project_collection += ", ".join(p["Project"])
            else:
                project_collection = p["Project"]
        print(f"\tWorks on: {project_collection}")
def read_file(file_name):
    with open(file_name, 'r') as r_file:
        csv_file = csv.reader(r_file)
        headers = next(csv_file)
        data_collection = []
        for rows in csv_file:
            data_entry = {headers[i]: rows[i] for i in range(len(headers))}
            data_collection.append(data_entry)
    return data_collection
def insert_data(collection_name, entries):
    collection_name.create_index("User_id", unique=True)
    for data in entries:
        try:
            collection_name.insert_one(data)
        except pymongo.errors.DuplicateKeyError:
            print(f"Duplicate entry: {data}")
            pass
def load_files(csv_files):
    insert_data(users, read_file(csv_files[0]))
    insert_data(organizations, read_file(csv_files[1]))
    insert_data(projects, read_int_or_skill(csv_files[2], "project"))
    insert_data(interests, read_int_or_skill(csv_files[3], "interest"))
    insert_data(skills, read_int_or_skill(csv_files[4], "skill"))
def read_int_or_skill(file_name, tag):
    with open(file_name, 'r') as r_file:
        csv_file = csv.reader(r_file)
        headers = next(csv_file)
        data_collection = []
        for rows in csv_file:
            data = {headers[i]: rows[i] for i in range(len(headers))}
            if find_matching_id(data, data_collection, tag):
                data_collection.append(data)
    return data_collection
def find_matching_id(info, arr, tag):
    for elements in arr:
        if elements["User_id"] == info["User_id"]:
            if tag == "interest":
                if not isinstance(elements["Interest"], list):
                    elements["Interest"] = [elements["Interest"], info["Interest"]]
                    elements["Interest level"] = [elements["Interest level"], info["Interest level"]]
                else:
                    if info["Interest"] not in elements["Interest"]:
                        elements["Interest"].append(info["Interest"])
                        elements["Interest level"].append(info["Interest level"])
            elif tag == "skill":
                if not isinstance(elements["Skill"], list):
                    elements["Skill"] = [elements["Skill"], info["Skill"]]
                    elements["Skill level"] = [elements["Skill level"], info["Skill level"]]
                else:
                    if info["Skill"] not in elements['Skill']:
                        elements["Skill"].append(info["Skill"])
                        elements["Skill level"].append(info["Skill level"])
            elif tag == "project":
                if not isinstance(elements["Project"], list):
                    elements["Project"] = [elements["Project"], info["Project"]]
                else:
                    if info["Project"] not in elements['Project']:
                        elements["Project"].append(info["Project"])
            return False
    return True
def drop_db():
    client.drop_database("projectOne")
if __name__ == "__main__":
    main()
    while True:
        play_again = input("\nDo you want to load data from files? (yes/no): ").strip().lower()
        if play_again == "yes":
            csv_files = [
                "users.csv",
                "organizations.csv",
                "projects.csv",
                "interests.csv",
                "skills.csv"
            ]
            load_files(csv_files)
        else:
            print("Exiting...")
            break