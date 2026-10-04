
class Patient:
    def __init__(self, name, contact, age, days, balance):
        self.name = name
        self.contact = contact
        self.age = age
        self.days = days
        self.balance = balance
    def get_name(self):
        return self.name
    def get_contact(self):
        return self.contact
    def get_age(self):
        return self.age
    def get_days(self):
        return self.days
    def get_balance(self):
        return self.balance
    def update_name(self, name):
        self.name = name
    def update_contact(self, contact):
        self.contact = contact
    def update_age(self, age):
        self.age = age
    def update_days(self, days):
        self.days = days
    def update_balance(self, balance):
        self.balance = balance
patient_list = []
with open("Patient_Info-sorted.dat", "r") as fp:
    fp.readline()
    for line in fp:
        line = line.strip()
        if not line:
            break
        word = line.split()
        patient = Patient(
            name=str(word[0]),
            contact=str(word[1]),
            age=int(word[2]),
            days=int(word[3]),
            balance=float(word[4])
        )
        patient_list.append(patient)
def binary_search_patient(patient_list, target_name):
    first = 0
    last = len(patient_list) - 1
    count = 0
    while first <= last:
        count += 1
        mid = (first + last)
        mid_name = patient_list[mid].get_name()
        if target_name > mid_name:
            first = mid + 1
        elif target_name < mid_name:
            last = mid - 1
        else:
            print("Patient found at index", mid)
            print("Number of iterations:", count)
            print("Patient contact:", patient_list[mid].get_contact())
            print("Patient age:", patient_list[mid].get_age())
            print("Patient days admitted:", patient_list[mid].get_days())
            print("Patient balance:", patient_list[mid].get_balance())
            return True
    print("Patient not found.")
    return False
target_name = input("Enter a patient name to search: ")
binary_search_patient(patient_list, target_name)