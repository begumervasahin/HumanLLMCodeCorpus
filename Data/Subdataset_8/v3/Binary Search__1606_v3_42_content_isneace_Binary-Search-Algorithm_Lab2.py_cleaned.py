class Patient:
    def __init__(self, name, contact, age, days, balance):
        self.name = name
        self.contact = contact
        self.age = age
        self.days = days
        self.balance = balance
    def update(self, name=None, contact=None, age=None, days=None, balance=None):
        if name is not None:
            self.name = name
        if contact is not None:
            self.contact = contact
        if age is not None:
            self.age = age
        if days is not None:
            self.days = days
        if balance is not None:
            self.balance = balance
    def __str__(self):
        return f"Name: {self.name}, Contact: {self.contact}, Age: {self.age}, Days: {self.days}, Balance: {self.balance}"
def binary_search(patients, name):
    first = 0
    last = len(patients) - 1
    count = 0
    while first <= last:
        count += 1
        mid = (first + last)
        mid_name = patients[mid].name
        if name > mid_name:
            first = mid + 1
        elif name < mid_name:
            last = mid - 1
        else:
            print("Found:", patients[mid])
            print("Found at index:", mid)
            print("Number of iterations:", count)
            return
    print("Not found")
def load_patients_from_file(file_path):
    patients = []
    with open(file_path, "r") as file:
        file.readline()
        for line in file:
            data = line.strip().split()
            name, contact, age, days, balance = data
            patient = Patient(name, contact, int(age), int(days), float(balance))
            patients.append(patient)
    return patients
def main():
    file_path = "Patient_Info-sorted.dat"
    patients = load_patients_from_file(file_path)
    search_name = input("Enter a patient name to search: ")
    binary_search(patients, search_name)
if __name__ == "__main__":
    main()