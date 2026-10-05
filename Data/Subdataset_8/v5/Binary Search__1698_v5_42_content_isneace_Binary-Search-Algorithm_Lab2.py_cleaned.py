class Patient:
    def __init__(self, name, contact, age, days, balance):
        self.name = name
        self.contact = contact
        self.age = age
        self.days = days
        self.balance = balance
    def __str__(self):
        return f"Name: {self.name}, Contact: {self.contact}, Age: {self.age}, Days: {self.days}, Balance: {self.balance}"
def read_patient_info(filename):
    patient_list = []
    with open(filename, "r") as file:
        file.readline()
        for line in file:
            line = line.strip()
            words = line.split()
            patient = Patient(str(words[0]), str(words[1]), int(words[2]), int(words[3]), float(words[4]))
            patient_list.append(patient)
    return patient_list
def binary_search_patient(patient_list, value):
    first = 0
    last = len(patient_list) - 1
    count = 0
    while first <= last:
        count += 1
        mid = (first + last)
        if value > patient_list[mid].name:
            first = mid + 1
        elif value < patient_list[mid].name:
            last = mid - 1
        elif value == patient_list[mid].name:
            return mid, count, True, patient_list[mid]
    return None, count, False, None
def main():
    patient_list = read_patient_info("Patient_Info-sorted.dat")
    value = input("Enter a Patient name to search: ")
    index, iterations, found, patient = binary_search_patient(patient_list, value)
    if found:
        print(found)
        print("Found at index:", index)
        print("Number of iterations:", iterations)
        print(patient)
    else:
        print(found)
        print("Value not found")
if __name__ == "__main__":
    main()