2. Repository: MrPatel95/Apriori-Algorithm
   File: generateDatabse.py
   URL: https:
   Code Content:
import random
computerStuff = ["Desktop", "Laptop", "Mouse", "Keyboard", "Printer", "HDMI", "SSD", "HDD", "Monitor", "Processor"]
candies = ["AlmondJoy", "KitKat", "HeathBar", "BabyRuth", "Twix", "Snickers", "Cotton Candy", "MilkyWay", "Hershey", "Cadbury"]
mobileStuff = ["HeadPhones", "Charger", "Splitter", "Lences", "Battery", "Processor", "HomeButton", "Speakers", "Camera", "Screen"]
food = ["Bread", "Milk", "Eggs", "Tea", "Coffee", "Cream", "Bagel", "Sugar", "CreamCheese", "Cheese"]
automobile = ["SideLight", "HeadLight", "Engine", "SteeringWheel", "WindShield", "Oil", "BreakPad", "Wheels", "Tires", "Car"]
selected = []
file = open('computerStuff.txt' ,'a')
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(computerStuff[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')
file = open('candies.txt' ,'a')
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(candies[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')
file = open('mobileStuff.txt' ,'a')
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(mobileStuff[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')
file = open('food.txt' ,'a')
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(food[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')
file = open('automobile.txt' ,'a')
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(automobile[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')
   README Content:
This is a Data Mining and Machine Learning algorithm called Apriori Algorithm. It takes input and generates association rules.
* Clone this repo and fire up **generateDatabse.py file**.
* This file will create the five sample data sources for testing purposes.
* Ones you see the .txt data source files in your prject folder, you are ready to go.
* Now fire up **AprioriAlgorithm.py** file which is the actual code for this algorithm.
Need to have **python 3.6** installed on your machine. Other version support will be provided as soon as possible.
* The program takes **data source**, **Minimum Support in percentage** and **Minimum Confidence in percentage** as input.
* **Data Source:** This is to select where the input is coming from. For this test, the data is coming from one of the five files that were created using generateDatabse.py.
* **Minimum Support:** A minimum support is applied to find all frequent itemsets in a database.
* **Minimum Confidence:** A minimum confidence is applied to these frequent itemsets in order to form rules.
* **Result:** The result will show the association rules in the given dataset with the given minimum support and minimum confidence if there are any. If there are no association rules in the the set with the given support and confidence conditions, try to plug in some different (*if you didn't get any results, try feeding some lower values*) values of them.
* You are welcomed to modify **generateDatabse.py** file and try to come up with some new data set.
* You can use any data set which is a text file, comma seperated items and one transaction per line.
* [Python 3.6](https:
Fork the repo and try to come up with some optimized version of the algorithm.
* [Jeet Patel](https:
It is crucial to stay social ;)
* [LinkedIn](https:
* [Instagram](https:
