import pymongo
import csv
class MongoDBManager:
    def __init__(self, db_name):
        self.client = pymongo.MongoClient()
        self.db = self.client[db_name]
        self.users = self.db["Users"]
        self.organizations = self.db["Organizations"]
        self.interests = self.db["Interests"]
        self.projects = self.db["Projects"]
        self.skills = self.db["Skills"]
    def look_up_user(self, user_id):
        user_id = str(user_id)
        if self.users.count_documents({"User_id": user_id}) == 0:
            print("This user does not exist. Please try another userID.")
        else:
            self._print_user_details(user_id)
    def _print_user_details(self, user_id):
        user_results = self.users.find({"User_id": user_id})
        organization_results = self.organizations.find({"User_id": user_id})
        interests_results = self.interests.find({"User_id": user_id})
        skills_results = self.skills.find({"User_id": user_id})
        projects_results = self.projects.find({"User_id": user_id})
        for user in user_results:
            print(f"\tName: {user['First name']} {user['Last name']}")
        for organization in organization_results:
            print(f"\tWorks at: {organization['Organization']}")
        self._print_collection("Interest", interests_results)
        self._print_collection("Skill", skills_results)
        self._print_collection("Project", projects_results)
    def _print_collection(self, collection_name, results):
        collection = []
        for item in results:
            if isinstance(item[collection_name], list):
                collection += [f"{element} ({level})" for element, level in zip(item[collection_name], item[f"{collection_name} level"])]
            else:
                collection.append(f"{item[collection_name]} ({item[f'{collection_name} level']})")
        print(f"\t{collection_name}: {', '.join(collection)}")
    def read_file(self, file_name):
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            return [{headers[i]: row[i] for i in range(len(headers))} for row in csv_reader]
    def insert_data(self, collection, entries):
        collection.create_index("User_id", unique=True)
        for data in entries:
            try:
                collection.insert_one(data)
            except pymongo.errors.DuplicateKeyError:
                print(f"Duplicate entry: {data}")
    def load_files(self, csv_files):
        self.insert_data(self.users, self.read_file(csv_files[0]))
        self.insert_data(self.organizations, self.read_file(csv_files[1]))
        self.insert_data(self.projects, self._read_int_or_skill(csv_files[2], "Project"))
        self.insert_data(self.interests, self._read_int_or_skill(csv_files[3], "Interest"))
        self.insert_data(self.skills, self._read_int_or_skill(csv_files[4], "Skill"))
    def _read_int_or_skill(self, file_name, tag):
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            data_collection = []
            for row in csv_reader:
                data = {headers[i]: row[i] for i in range(len(headers))}
                self._find_matching_id(data, data_collection, tag)
            return data_collection
    def _find_matching_id(self, info, collection, tag):
        for element in collection:
            if element["User_id"] == info["User_id"]:
                self._update_existing_entry(element, info, tag)
                return
        collection.append(info)
    def _update_existing_entry(self, existing_entry, new_info, tag):
        if tag in ["Interest", "Skill"]:
            attribute = tag.lower()
            level = f"{attribute} level"
            if not isinstance(existing_entry[attribute], list):
                existing_entry[attribute] = [existing_entry[attribute], new_info[attribute]]
                existing_entry[level] = [existing_entry[level], new_info[level]]
            elif new_info[attribute] not in existing_entry[attribute]:
                existing_entry[attribute].append(new_info[attribute])
                existing_entry[level].append(new_info[level])
        elif tag == "Project":
            if not isinstance(existing_entry["Project"], list):
                existing_entry["Project"] = [existing_entry["Project"], new_info["Project"]]
            elif new_info["Project"] not in existing_entry["Project"]:
                existing_entry["Project"].append(new_info["Project"])
    def drop_db(self):
        self.client.drop_database("projectOne")
def main():
    db_manager = MongoDBManager("projectOne")
    while True:
        search_user = input("\nWould you like to search for a user (y/n): ").strip().lower()
        if search_user == 'y':
            user_id = input("Enter the User ID: ").strip()
            db_manager.look_up_user(user_id)
        else:
            break
    while True:
        load_data = input("\nDo you want to load data from files? (yes/no): ").strip().lower()
        if load_data == "yes":
            csv_files = [
                "users.csv",
                "organizations.csv",
                "projects.csv",
                "interests.csv",
                "skills.csv"
            ]
            db_manager.load_files(csv_files)
        else:
            print("Exiting...")
            break
if __name__ == "__main__":
    main()