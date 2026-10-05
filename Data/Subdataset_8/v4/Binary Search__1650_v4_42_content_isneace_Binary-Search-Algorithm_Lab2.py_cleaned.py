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
with open("Patient_Info-sorted.dat", "r") as file:
    file.readline()
    for line in file:
        line = line.strip()
        words = line.split()
        patient = Patient(str(words[0]), str(words[1]), int(words[2]), int(words[3]), float(words[4]))
        patient_list.append(patient)
found = False
value = input("Enter a Patient name to search: ")
first = 0
last = len(patient_list) - 1
count = 0
while first <= last:
    count += 1
    mid = (first + last)
    if value > patient_list[mid].get_name():
        first = mid + 1
    elif value < patient_list[mid].get_name():
        last = mid - 1
    elif value == patient_list[mid].get_name():
        found = True
        print(found)
        print("Found at index:", mid)
        print("Number of iterations:", count)
        print("Patient contact:", patient_list[mid].get_contact())
        print("Patient Age:", patient_list[mid].get_age())
        print("Patient Days:", patient_list[mid].get_days())
        print("Patient Balance:", patient_list[mid].get_balance())
        break
    else:
        print(found)
        print("Value not found")
        break