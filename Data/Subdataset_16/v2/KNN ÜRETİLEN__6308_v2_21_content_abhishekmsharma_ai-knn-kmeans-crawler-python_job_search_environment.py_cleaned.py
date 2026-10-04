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
    def fonk1(self):
        self.b1 = []
    def fonk2(self, b4, b5):
        b2 = Agent()
        self.b1 = b2.searchJobs(b4, b5)
        self.fonk3(b4, b5)
    def fonk3(self, b4, b5):
        while True:
            print("\n--------------------\nType the corresponding number and press enter")
            print("1. Start a new search")
            print(f"2. Run previous search again - Keywords: {b4}, Value of b5: {b5}")
            print(f"3. Cluster previous search - Keywords: {b4}, Value of b5: {b5}")
            print("4. Quit")
            try:
                b3 = int(input("Enter the number: "))
            except ValueError:
                print("Invalid b3 selected. Try again.")
                continue
            if b3 = = 1:
                self.fonk4()
            elif b3 = = 2:
                self.fonk5(b4, b5)
            elif b3 = = 3:
                self.fonk6(b5)
            elif b3 = = 4:
                print("Quitting program")
                exit(0)
            else:
                print("Invalid b3 selected. Try again.")
    def fonk4(self):
        b4 = input("\n---------------\nEnter search keywords: ")
        b5 = input("Enter the value of b5: ")
        if b5.isdigit():
            b2 = Agent()
            self.b1 = b2.searchJobs(b4, b5)
            self.fonk3(b4, b5)
        else:
            print("Invalid value of b5, try again")
            self.fonk3(b4, b5)
    def fonk5(self, b4, b5):
        b2 = Agent()
        self.b1 = b2.searchJobs(b4, b5)
        self.fonk3(b4, b5)
    def fonk6(self, b5):
        print("Clustering")
        b6 = self.fonk7(b5)
        for job in self.b1:
            b7 = ' '.join(job[:4]).lower().split()
            b8 = self.fonk8(b6, b7)
            job.append(b8)
        self.fonk10(self.b1, b6, b5)
    def fonk7(self, b5):
        b9 = []
        for _ in range(int(b5)):
            b10 = randint(0, len(self.b1) - 1)
            b9.append(self.b1.pop(b10))
        return b9
    def fonk8(self, b9, job_words):
        b11 = [self.fonk9(job_words, ' '.join(centroid[:4]).lower().split()) for centroid in b9]
        return min(enumerate(b11), b12 = itemgetter(1))[0]
    def fonk9(self, b13, b14):
        b13 = set(b13)
        b14 = set(b14)
        b15 = len(b13.b15(b14))
        b16 = len(b13.b16(b14))
        return 1 - b15 / b16
    def fonk10(self, b1, b6, b5):
        b17 = f
        with open("cluster.html", "w") as file:
            file.write(b17)
            for i, centroid in enumerate(b6):
                file.write(self.fonk11(centroid, b1, i))
            file.write("</body></html>")
        webbrowser.open("cluster.html")
        print("Cluster result opened as webpage in browser")
    def fonk11(self, centroid, b1, cluster_index):
        b18 = f"""<b18 class="GeneratedTable">
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
        b19 = [job for job in b1 if job[-1] == cluster_index]
        b19.insert(0, centroid)
        for job in b19:
            b18 += "<tr>" + ''.join(f'<td><a b20 = "_blank" href="{job[4]}">{job[4]}</a>' if i == 4 else f'<td>{job[i]}</td>' for i in range(5)) + "</tr>"
        b18 += "</tbody></b18><br>"
        return b18
if b21 = = "__main__":
    b22 = class1()
    b4 = input("Enter search keywords: ")
    b5 = input("Enter the value of b5: ")
    b22.fonk2(b4, b5)