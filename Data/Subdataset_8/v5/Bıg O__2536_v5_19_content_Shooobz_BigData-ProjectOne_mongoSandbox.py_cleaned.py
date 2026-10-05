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
    print(f"\tName: {user['First name']} {user['Last name']}")
def print_organization(user_id):
    organizations_list = organizations.find({"User_id": user_id})
    for org in organizations_list:
        print(f"\tWorks at: {org['Organization']}")
def print_interests(user_id):
    interests_list = interests.find({"User_id": user_id})
    interests_str = ", ".join(f"{interest['Interest']}({interest['Interest Level']})" for interest in interests_list)
    print(f"\tInterest: {interests_str}")
def print_skills(user_id):
    skills_list = skills.find({"User_id": user_id})
    skills_str = ", ".join(f"{skill['Skill']}({skill['Skill Level']})" for skill in skills_list)
    print(f"\tSkill: {skills_str}")
def print_projects(user_id):
    projects_list = projects.find({"User_id": user_id})
    projects_str = ", ".join(project['Project'] for project in projects_list)
    print(f"\tWorks on: {projects_str}")
def read_csv(file_name):
    with open(file_name) as file:
        csv_reader = csv.DictReader(file)
        return list(csv_reader)
def insert_data(collection, entries):
    collection.create_index("User_id", unique=True)
    for entry in entries:
        try:
            collection.insert_one(entry)
        except pymongo.errors.DuplicateKeyError:
            print(f"Duplicate entry found for {entry['User_id']}. Skipping insertion.")
def load_csv_files(csv_files):
    insert_data(users, read_csv(csv_files[0]))
    insert_data(organizations, read_csv(csv_files[1]))
    insert_data(projects, read_csv(csv_files[2]))
    insert_data(interests, read_csv(csv_files[3]))
    insert_data(skills, read_csv(csv_files[4]))
def drop_database():
    client.drop_database("projectOne")
if __name__ == "__main__":
    main()