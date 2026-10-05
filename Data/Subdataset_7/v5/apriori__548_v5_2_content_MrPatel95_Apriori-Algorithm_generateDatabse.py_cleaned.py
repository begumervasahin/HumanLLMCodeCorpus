import random
b1 = {
    "computer_stuff": [
        "Desktop", "Laptop", "Mouse", "Keyboard", "Printer",
        "HDMI", "SSD", "HDD", "Monitor", "Processor"
    ],
    "candies": [
        "AlmondJoy", "KitKat", "HeathBar", "BabyRuth", "Twix",
        "Snickers", "Cotton Candy", "MilkyWay", "Hershey", "Cadbury"
    ],
    "mobile_stuff": [
        "HeadPhones", "Charger", "Splitter", "Lenses", "Battery",
        "Processor", "HomeButton", "Speakers", "Camera", "Screen"
    ],
    "food": [
        "Bread", "Milk", "Eggs", "Tea", "Coffee",
        "Cream", "Bagel", "Sugar", "CreamCheese", "Cheese"
    ],
    "automobile": [
        "SideLight", "HeadLight", "Engine", "SteeringWheel",
        "WindShield", "Oil", "BreakPad", "Wheels", "Tires", "Car"
    ]
}
def fonk1(filename, items):
    with open(filename, 'a') as file:
        file.truncate()
        for _ in range(25):
            b2 = random.sample(items, 10)
            file.write(','.join(b2) + '\n')
for category, items in b1.items():
    fonk1(category + '.txt', items)