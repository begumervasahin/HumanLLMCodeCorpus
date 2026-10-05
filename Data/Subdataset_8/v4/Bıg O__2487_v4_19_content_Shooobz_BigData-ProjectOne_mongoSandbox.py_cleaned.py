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
            search_user()
        else:
            break
def search_user():
    user_id = input("Enter the userID: ")
    user = users.find_one({"User_id": user_id})
    if user:
        print_user_info(user)
        print_organization(user_id)
        print_interests(user_id)
        print_skills(user_id)
        print_projects(user_id)
    else:
        print("This user does not exist. Please try another userID.")
def print_user_info(user):
    print(f"\tName: {user['First name']} {user['First name']}")
def print_organization(user_id):
    organizations_list = organizations.find({"User_id": user_id})
    for org in organizations_list:
        print(f"\tWorks at: {org['organization']}")
def print_interests(user_id):
    interests_list = interests.find({"User_id": user_id})
    interests_str = ", ".join(f"{interest['Interest']}({interest['Interest level']})" for interest in interests_list)
    print(f"\tInterest: {interests_str}")
def print_skills(user_id):
    skills_list = skills.find({"User_id": user_id})
    skills_str = ", ".join(f"{skill['Skill']}({skill['Skill level']})" for skill in skills_list)
    print(f"\tSkill: {skills_str}")
def print_projects(user_id):
    projects_list = projects.find({"User_id": user_id})
    projects_str = ", ".join(project['Project'] for project in projects_list)
    print(f"\tWorks on: {projects_str}")
def read_file(file_name):
    with open(file_name) as f:
        csv_file = csv.DictReader(f)
        return list(csv_file)
def insert_data(collection, entries):
    collection.create_index("User_id", unique=True)
    for entry in entries:
        try:
            collection.insert_one(entry)
        except pymongo.errors.DuplicateKeyError:
            print(f"Duplicate entry found for {entry['User_id']}. Skipping insertion.")
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