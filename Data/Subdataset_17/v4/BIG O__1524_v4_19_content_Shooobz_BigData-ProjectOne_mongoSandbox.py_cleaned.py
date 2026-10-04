import pymongo
import csv
client = pymongo.MongoClient()
db = client["projectOne"]
users = db["Users"]
organizations = db["Organizations"]
interests = db["Interests"]
projects = db["Projects"]
skills = db["Skill"]
def main():
    while True:
        val = input("\nWould you like to search for a user (y/n): ").strip().lower()
        if val == 'y':
            user_id = input("Enter user ID: ").strip()
            look_up_user(user_id)
        else:
            break
def look_up_user(user_id):
    if users.count_documents({"User_id": user_id}) == 0:
        print("This user does not exist. Please try another user ID.")
        return
    user_results = users.find({"User_id": user_id})
    organization_results = organizations.find({"User_id": user_id})
    interest_results = interests.find({"User_id": user_id})
    skill_results = skills.find({"User_id": user_id})
    project_results = projects.find({"User_id": user_id})
    for user in user_results:
        print(f"\tName: {user['First name']} {user['Last name']}")
    for org in organization_results:
        print(f"\tWorks at: {org['organization']}")
    interest_collection = ""
    for interest in interest_results:
        if isinstance(interest["Interest"], list):
            for i in range(len(interest["Interest"])):
                interest_collection += f"{interest['Interest'][i]} ({interest['Interest level'][i]}), "
        else:
            interest_collection = f"{interest['Interest']} ({interest['Interest level']})"
    print(f"\tInterests: {interest_collection}")
    skill_collection = ""
    for skill in skill_results:
        if isinstance(skill["Skill"], list):
            for i in range(len(skill["Skill"])):
                skill_collection += f"{skill['Skill'][i]} ({skill['Skill level'][i]}), "
        else:
            skill_collection = f"{skill['Skill']} ({skill['Skill level']})"
    print(f"\tSkills: {skill_collection}")
    project_collection = ""
    for project in project_results:
        if isinstance(project["Project"], list):
            for p in project["Project"]:
                project_collection += f"{p}, "
        else:
            project_collection = project["Project"]
    print(f"\tWorks on: {project_collection}")
def read_file(file_name):
    with open(file_name, mode='r') as file:
        csv_file = csv.reader(file)
        headers = next(csv_file)
        data_collection = []
        for row in csv_file:
            data_entry = {headers[i]: row[i] for i in range(len(headers))}
            data_collection.append(data_entry)
    return data_collection
def insert_data(collection, entries):
    collection.create_index("User_id", unique=True)
    for data in entries:
        try:
            collection.insert_one(data)
        except Exception as e:
            print(f"Error inserting data: {data}, Error: {e}")
def load_files(csv_files):
    insert_data(users, read_file(csv_files[0]))
    insert_data(organizations, read_file(csv_files[1]))
    insert_data(projects, read_int_or_skill(csv_files[2], "project"))
    insert_data(interests, read_int_or_skill(csv_files[3], "interest"))
    insert_data(skills, read_int_or_skill(csv_files[4], "skill"))
def read_int_or_skill(file_name, tag):
    with open(file_name, mode='r') as file:
        csv_file = csv.reader(file)
        headers = next(csv_file)
        data_collection = []
        if tag == "interest":
            interests.create_index([("User_id", pymongo.ASCENDING), ("Interest", pymongo.DESCENDING)], unique=True)
        elif tag == "skill":
            skills.create_index([("User_id", pymongo.ASCENDING), ("Skill", pymongo.DESCENDING)], unique=True)
        for row in csv_file:
            data = {headers[i]: row[i] for i in range(len(headers))}
            if find_matching_id(data, data_collection, tag):
                data_collection.append(data)
    return data_collection
def find_matching_id(info, data_list, tag):
    for element in data_list:
        if element["User_id"] == info["User_id"]:
            if tag == "interest":
                if not isinstance(element["Interest"], list):
                    element["Interest"] = [element["Interest"], info["Interest"]]
                    element["Interest level"] = [element["Interest level"], info["Interest level"]]
                else:
                    if info["Interest"] not in element["Interest"]:
                        element["Interest"].append(info["Interest"])
                        element["Interest level"].append(info["Interest level"])
            elif tag == "skill":
                if not isinstance(element["Skill"], list):
                    element["Skill"] = [element["Skill"], info["Skill"]]
                    element["Skill level"] = [element["Skill level"], info["Skill level"]]
                else:
                    if info["Skill"] not in element["Skill"]:
                        element["Skill"].append(info["Skill"])
                        element["Skill level"].append(info["Skill level"])
            elif tag == "project":
                if not isinstance(element["Project"], list):
                    element["Project"] = [element["Project"], info["Project"]]
                else:
                    if info["Project"] not in element["Project"]:
                        element["Project"].append(info["Project"])
            return False
    return True
def drop_db():
    client.drop_database("projectOne")
if __name__ == "__main__":
    main()