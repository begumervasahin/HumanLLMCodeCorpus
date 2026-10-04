
class Patient:
    def __init__(self, name, contact, age, days, balance):
        self.name = name
        self.contact = contact
        self.age = age
        self.days = days
        self.balance = balance
    def __str__(self):
        return (f"Name: {self.name}, Contact: {self.contact}, Age: {self.age}, "
                f"Days Admitted: {self.days}, Balance: ${self.balance:.2f}")
    def get_name(self):
        return self.name
def load_patient_data(file_path):
    patient_list = []
    with open(file_path, "r") as fp:
        fp.readline()
        for line in fp:
            line = line.strip()
            if not line:
                continue
            name, contact, age, days, balance = line.split()
            patient = Patient(
                name=name,
                contact=contact,
                age=int(age),
                days=int(days),
                balance=float(balance)
            )
            patient_list.append(patient)
    return patient_list
def binary_search_patient(patient_list, target_name):
    first, last = 0, len(patient_list) - 1
    iterations = 0
    while first <= last:
        iterations += 1
        mid = (first + last)
        mid_name = patient_list[mid].get_name()
        if target_name > mid_name:
            first = mid + 1
        elif target_name < mid_name:
            last = mid - 1
        else:
            print(f"Patient found at index {mid}")
            print(f"Number of iterations: {iterations}")
            print(patient_list[mid])
            return True
    print("Patient not found.")
    return False
def main():
    patient_list = load_patient_data("Patient_Info-sorted.dat")
    target_name = input("Enter a patient name to search: ")
    binary_search_patient(patient_list, target_name)
if __name__ == "__main__":
    main()