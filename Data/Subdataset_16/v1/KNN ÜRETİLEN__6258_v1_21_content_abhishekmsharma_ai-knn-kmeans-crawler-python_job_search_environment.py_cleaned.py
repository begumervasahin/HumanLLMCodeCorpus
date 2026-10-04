'''
Developer: Abhishek Manoj Sharma
Date: September 27, 2017
Class: class1
'''
from job_search_agent import Agent
from random import randint
from operator import itemgetter
import webbrowser
class class1:
    b1 = []
    def fonk1(self, b22, b23):
        b2 = Agent()
        self.b1 = b2.searchJobs(b22, b23)
        self.fonk2(b22, b23)
    def fonk2(self, b22, b23):
        print("\n--------------------\nType the corresponding number and press enter")
        print("1. Start b2 new search")
        print("2. Run previous search again - Keywords:", b22, ", Value of b23:", b23)
        print("3. Cluster previous search - Keywords:", b22, ", Value of b23:", b23)
        print("4. Quit")
        b3 = input("Enter the number: ")
        try:
            b3 = int(b3)
            if b3 = = 1:
                b4 = input("\n---------------\nEnter search b12: ")
                b5 = input("Enter the value of b23: ")
                if b5.isdigit():
                    b2 = Agent()
                    self.b1 = b2.searchJobs(b4, b5)
                    self.fonk2(b4, b5)
                else:
                    print("Invalid value of b23, try again")
                    self.fonk2(b22, b23)
            elif b3 = = 2:
                b2 = Agent()
                self.b1 = b2.searchJobs(b22, b23)
                self.fonk2(b22, b23)
            elif b3 = = 3:
                print("Clustering")
                self.fonk3(b23)
                self.fonk2(b22, b23)
            elif b3 = = 4:
                print("Quitting program")
                exit(0)
            else:
                print("Invalid b3 selected.\nTry again")
                self.fonk2(b22, b23)
        except ValueError:
            print("Invalid b3 selected.\nTry again")
            self.fonk2(b22, b23)
    def fonk3(self, b23):
        b6 = []
        for i in range(0, int(b23)):
            b7 = randint(0, len(self.b1) - 1)
            b6.append(self.b1[b7])
            self.b1.pop(b7)
        for row in self.b1:
            b8 = (row[0] + " " + row[1] + " " + row[2] + " " + row[3]).lower()
            b8 = b8.split(" ")
            row.append(self.fonk4(b6, b8))
        self.fonk6(self.b1, b6, b23)
    def fonk4(self, b6, jobs_words):
        b9 = []
        for item in b6:
            b10 = (item[0] + " " + item[1] + " " + item[2] + " " + item[3]).lower()
            b10 = b10.split(" ")
            b9.append(self.fonk5(jobs_words, b10))
        return min(enumerate(b9), b11 = itemgetter(1))[0]
    def fonk5(self, b12, b13):
        b12 = [word.lower() for word in b12]
        b13 = [word.lower() for word in b13]
        b14 = len(set(b12).b14(set(b13)))
        b15 = len(set(b12).b15(set(b13)))
        return 1 - b14 / float(b15)
    def fonk6(self, b1, b6, b23):
        b16 = + str(b23) +
        with open("cluster.html", "w") as f:
            f.write(b16)
            for i in range(len(b6)):
                b17 = """<table class="GeneratedTable">
                <thead>
                    <tr>
                        <th>Company Name</th>
                        <th>Position</th>
                        <th>Location</th>
                        <th>Description</th>
                        <th>Link</th>
                    </tr>
                </thead>
                <tbody>"""
                f.write(b17)
                b18 = [b6[i]]
                for item in b1:
                    if item[-1] == i:
                        b18.append(item)
                for item in b18:
                    f.write("<tr>")
                    for b19 in range(5):
                        f.write("<td>")
                        if b19 = = 4:
                            f.write(f'<b2 b20 = "_blank" href="{item[b19]}">{item[b19]}</b2>')
                        else:
                            f.write(item[b19])
                        f.write("</td>")
                    f.write("</tr>")
                f.write("</tbody></table><br>")
            f.write("</body></html>")
        webbrowser.open("cluster.html")
        print("Cluster result opened as webpage in browser")
b21 = class1()
b22 = input("Enter search b12: ")
b23 = input("Enter the value of b23: ")
b21.fonk1(b22, b23)