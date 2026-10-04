class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = float(pay)
        self.email = first + '.' + last + '@company.com'
        self.bonus = 0
    def get_pay(self):
        return self.pay
    def set_pay(self, pay):
        self.pay = pay
    def set_bonus(self, amount):
        self.bonus = amount
    def get_bonus(self):
        return self.bonus
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    def __str__(self):
        return '\nEmployee name: ' + self.full_name() +\
               '\nEmployee pay: ' + str(self.pay) +\
               '\nEmployee bonus: ' + str(format(self.bonus, '.2f'))
def main():
    pay_rate = 0.2
    total_bonus = 0
    employee_queue = Queue()
    with open('/Users/danieltshibangu/Desktop/dirany.txt', 'r') as dirany_file:
        for line in dirany_file:
            data_attr = line.split()
            if len(data_attr) < 3:
                continue
            employee = Employee(data_attr[0], data_attr[1], data_attr[2])
            employee.set_bonus(employee.get_pay() * pay_rate)
            total_bonus += employee.get_bonus()
            employee_queue.enqueue(employee)
            pay_rate -= 0.01
    print("The total number of employees:", employee_queue.size())
    print("The total bonus amount:", format(total_bonus, '.2f'))
    print("\nDisplays all the objects in the queue:")
    while not employee_queue.is_empty():
        print(employee_queue.dequeue())
if __name__ == "__main__":
    main()