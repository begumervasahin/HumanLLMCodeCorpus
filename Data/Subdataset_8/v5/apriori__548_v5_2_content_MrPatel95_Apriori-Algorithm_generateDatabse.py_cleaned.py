import random
categories = {
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
def generate_data(filename, items):
    with open(filename, 'a') as file:
        file.truncate()
        for _ in range(25):
            selected = random.sample(items, 10)
            file.write(','.join(selected) + '\n')
for category, items in categories.items():
    generate_data(category + '.txt', items)