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
        search_input = input("\nWould you like to search for a user (y/n): ").lower()
        if search_input == 'y':
            userID = input("Enter the userID: ")
            look_up_user(userID)
        else:
            break
def look_up_user(userID):
    user_result = users.find_one({"User_id": userID})
    if not user_result:
        print("This user does not exist. Please try another userID.")
    else:
        print_user_info(user_result)
        print_organization(userID)
        print_interests(userID)
        print_skills(userID)
        print_projects(userID)
def print_user_info(user_result):
    print(f"\tName: {user_result['First name']} {user_result['Last name']}")
def print_organization(userID):
    organization_result = organizations.find({"User_id": userID})
    for org in organization_result:
        print(f"\tWorks at: {org['organization']}")
def print_interests(userID):
    interests_results = interests.find({"User_id": userID})
    interest_collection = ", ".join([f"{i['Interest']}({i['Interest level']})" for i in interests_results])
    print(f"\tInterest: {interest_collection}")
def print_skills(userID):
    skill_results = skills.find({"User_id": userID})
    skill_collection = ", ".join([f"{sk['Skill']}({sk['Skill level']})" for sk in skill_results])
    print(f"\tSkill: {skill_collection}")
def print_projects(userID):
    projects_results = projects.find({"User_id": userID})
    project_collection = ", ".join([p['Project'] for p in projects_results])
    print(f"\tWorks on: {project_collection}")
def read_file(file_name):
    with open(file_name) as f:
        csv_file = csv.DictReader(f)
        return list(csv_file)
def insert_data(collection_name, entries):
    collection_name.create_index("User_id", unique=True)
    for data in entries:
        try:
            collection_name.insert_one(data)
        except pymongo.errors.DuplicateKeyError:
            print(f"Duplicate entry found for {data['User_id']}. Skipping insertion.")
def load_files(csvfiles):
    insert_data(users, read_file(csvfiles[0]))
    insert_data(organizations, read_file(csvfiles[1]))
    insert_data(projects, read_file(csvfiles[2]))
    insert_data(interests, read_file(csvfiles[3]))
    insert_data(skills, read_file(csvfiles[4]))
def drop_db():
    client.drop_database("projectOne")
if __name__ == "__main__":
    main()