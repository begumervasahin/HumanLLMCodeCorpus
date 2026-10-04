class Patient:
    def __init__(self, name, contact, age, days, balance):
        self.name = name
        self.contact = contact
        self.age = age
        self.days = days
        self.balance = balance
    def __str__(self):
        return f"Name: {self.name}, Contact: {self.contact}, Age: {self.age}, Days: {self.days}, Balance: {self.balance:.2f}"
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
def load_patient_data(file_name):
    patient_list = []
    with open(file_name, "r") as fp:
        fp.readline()
        for line in fp:
            line = line.strip()
            if line:
                fields = line.split()
                patient = Patient(
                    name=fields[0],
                    contact=fields[1],
                    age=int(fields[2]),
                    days=int(fields[3]),
                    balance=float(fields[4])
                )
                patient_list.append(patient)
    return patient_list
def binary_search_patient(patient_list, name):
    first, last = 0, len(patient_list) - 1
    iterations = 0
    while first <= last:
        iterations += 1
        mid = (first + last)
        mid_name = patient_list[mid].get_name()
        if name > mid_name:
            first = mid + 1
        elif name < mid_name:
            last = mid - 1
        else:
            return mid, iterations
    return -1, iterations
def display_patient_info(patient, index, iterations):
    print(f"Patient found at index {index}.")
    print(f"Number of iterations: {iterations}")
    print(patient)
def main():
    file_name = "Patient_Info-sorted.dat"
    patient_list = load_patient_data(file_name)
    name = input("Enter the patient's name to search: ")
    index, iterations = binary_search_patient(patient_list, name)
    if index != -1:
        patient = patient_list[index]
        display_patient_info(patient, index, iterations)
    else:
        print("Patient not found.")
        print(f"Number of iterations: {iterations}")
if __name__ == "__main__":
    main()