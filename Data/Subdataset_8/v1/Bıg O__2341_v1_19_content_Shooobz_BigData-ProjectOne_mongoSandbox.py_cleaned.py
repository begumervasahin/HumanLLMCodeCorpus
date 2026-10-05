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
        val = input("\nWould you like to search for a user (y/n): ")
        if val.lower() == 'y':
            userID = input("Enter the userID: ")
            lookUpUser(userID)
        else:
            break
def lookUpUser(userID):
    user_result = users.find_one({"User_id": userID})
    if not user_result:
        print("This user does not exist. Please try another userID.")
    else:
        print(f"\tName: {user_result['First name']} {user_result['First name']}")
        organization_result = organizations.find({"User_id": userID})
        for org in organization_result:
            print(f"\tWorks at: {org['organization']}")
        interests_results = interests.find({"User_id": userID})
        interest_collection = ", ".join([f"{i['Interest']}({i['Interest level']})" for i in interests_results])
        print(f"\tInterest: {interest_collection}")
        skill_results = skills.find({"User_id": userID})
        skill_collection = ", ".join([f"{sk['Skill']}({sk['Skill level']})" for sk in skill_results])
        print(f"\tSkill: {skill_collection}")
        projects_results = projects.find({"User_id": userID})
        project_collection = ", ".join([p['Project'] for p in projects_results])
        print(f"\tWorks on: {project_collection}")
def readFile(file_name):
    with open(file_name) as f:
        csv_file = csv.DictReader(f)
        return list(csv_file)
def insertData(collection_name, entries):
    collection_name.create_index("User_id", unique=True)
    for data in entries:
        try:
            collection_name.insert_one(data)
        except pymongo.errors.DuplicateKeyError:
            print(f"Duplicate entry found for {data['User_id']}. Skipping insertion.")
def loadFiles(csvfiles):
    insertData(users, readFile(csvfiles[0]))
    insertData(organizations, readFile(csvfiles[1]))
    insertData(projects, readFile(csvfiles[2]))
    insertData(interests, readFile(csvfiles[3]))
    insertData(skills, readFile(csvfiles[4]))
def dropDB():
    client.drop_database("projectOne")
if __name__ == "__main__":
    main()