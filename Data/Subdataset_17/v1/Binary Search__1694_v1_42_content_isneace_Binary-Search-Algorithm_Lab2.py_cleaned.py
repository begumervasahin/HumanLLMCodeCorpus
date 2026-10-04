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
def load_patient_data(file_name):
    patient_list = []
    with open(file_name, "r") as fp:
        fp.readline()
        for line in fp:
            line = line.strip()
            if line:
                word = line.split()
                patient = Patient(str(word[0]), str(word[1]), int(word[2]), int(word[3]), float(word[4]))
                patient_list.append(patient)
    return patient_list
def binary_search_patient(patient_list, name):
    first = 0
    last = len(patient_list) - 1
    count = 0
    while first <= last:
        count += 1
        mid = (first + last)
        mid_name = patient_list[mid].get_name()
        if name > mid_name:
            first = mid + 1
        elif name < mid_name:
            last = mid - 1
        else:
            return mid, count
    return -1, count
def main():
    patient_list = load_patient_data("Patient_Info-sorted.dat")
    name = input("Enter a Patient name to search: ")
    index, count = binary_search_patient(patient_list, name)
    if index != -1:
        patient = patient_list[index]
        print("Patient found at index", index)
        print("Number of iterations:", count)
        print("Patient contact:", patient.get_contact())
        print("Patient age:", patient.get_age())
        print("Patient days:", patient.get_days())
        print("Patient balance:", patient.get_balance())
    else:
        print("Patient not found.")
        print("Number of iterations:", count)
if __name__ == "__main__":
    main()