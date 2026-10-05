import random
b1 = [
    "Desktop", "Laptop", "Mouse", "Keyboard", "Printer",
    "HDMI", "SSD", "HDD", "Monitor", "Processor"
]
b2 = [
    "AlmondJoy", "KitKat", "HeathBar", "BabyRuth", "Twix",
    "Snickers", "Cotton Candy", "MilkyWay", "Hershey", "Cadbury"
]
b3 = [
    "HeadPhones", "Charger", "Splitter", "Lenses", "Battery",
    "Processor", "HomeButton", "Speakers", "Camera", "Screen"
]
b4 = [
    "Bread", "Milk", "Eggs", "Tea", "Coffee",
    "Cream", "Bagel", "Sugar", "CreamCheese", "Cheese"
]
b5 = [
    "SideLight", "HeadLight", "Engine", "SteeringWheel",
    "WindShield", "Oil", "BreakPad", "Wheels", "Tires", "Car"
]
def fonk1(filename, items):
    with open(filename, 'a') as file:
        file.truncate()
        for _ in range(25):
            b6 = random.sample(items, 10)
            file.write(','.join(b6) + '\n')
fonk1('computerStuff.txt', b1)
fonk1('b2.txt', b2)
fonk1('mobileStuff.txt', b3)
fonk1('b4.txt', b4)
fonk1('b5.txt', b5)