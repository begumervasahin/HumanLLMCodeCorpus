class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return not self.items
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@company.com"
        self.bonus = 0
    def set_pay(self, pay):
        self.pay = pay
    def set_bonus(self, bonus):
        self.bonus = bonus
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return (
            f"\nEmployee name: {self.get_full_name()}"
            f"\nEmployee pay: {self.pay}"
            f"\nEmployee bonus: {self.bonus:.2f}"
        )
def calculate_bonus(pay, pay_rate):
    return pay * pay_rate
def read_employee_data(file_path):
    with open(file_path, "r") as file:
        return [line.strip().split() for line in file]
def main():
    pay_rate = 0.2
    total_bonus = 0
    employee_queue = Queue()
    employee_data = read_employee_data("/Users/danieltshibangu/Desktop/dirany.txt")
    for data_attr in employee_data:
        first_name, last_name, pay = data_attr
        employee = Employee(first_name, last_name, float(pay))
        employee.set_bonus(calculate_bonus(float(pay), pay_rate))
        total_bonus += employee.bonus
        employee_queue.enqueue(employee)
        pay_rate -= 0.01
    print("The total number of employees:", employee_queue.size())
    print("The total bonus amount:", format(total_bonus, '.2f'))
    print("\nDisplays all the objects in the queue:")
    while not employee_queue.is_empty():
        print(employee_queue.dequeue())
if __name__ == "__main__":
    main()