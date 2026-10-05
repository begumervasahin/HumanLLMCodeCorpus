class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
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
    def set_bonus(self, amount):
        self.bonus = amount
    def get_bonus(self):
        return self.bonus
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return (f"\nEmployee name: {self.full_name()}\n"
                f"Employee pay: {self.pay}\n"
                f"Employee bonus: {self.bonus:.2f}")
def main():
    pay_rate = 0.2
    total_bonus = 0
    employee_queue = Queue()
    with open('/Users/danieltshibangu/Desktop/dirany.txt', 'r') as dirany_file:
        for line_data in dirany_file:
            data_attr = line_data.split()
            first_name, last_name, pay = data_attr[0], data_attr[1], float(data_attr[2])
            employee = Employee(first_name, last_name, pay)
            employee.set_bonus(pay * pay_rate)
            total_bonus += employee.get_bonus()
            employee_queue.enqueue(employee)
            pay_rate -= 0.01
    print("The total number of employees:", employee_queue.size())
    print("The total bonus amount:", f"{total_bonus:.2f}")
    print("\nDisplays all the objects in the queue:")
    while not employee_queue.is_empty():
        print(employee_queue.dequeue())
if __name__ == "__main__":
    main()