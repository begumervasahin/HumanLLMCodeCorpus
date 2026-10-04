'''
Developer: Abhishek Manoj Sharma
Date: September 27, 2017
Class: class1
'''
from job_search_agent import Agent
from random import randint
from operator import itemgetter
import webbrowser
b19 class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, keyword_input, b6):
        b2 = Agent()
        self.b1 = b2.searchJobs(keyword_input, b6)
        self.fonk3(keyword_input, b6)
    def fonk3(self, keyword_input, b6):
        while True:
            print("\n--------------------\nType the corresponding number and press enter")
            print(f"1. Start a new search")
            print(f"2. Run previous search again - Keywords: {keyword_input}, Value of b6: {b6}")
            print(f"3. Cluster previous search - Keywords: {keyword_input}, Value of b6: {b6}")
            print(f"4. Quit")
            try:
                b3 = int(input("Enter the number: "))
                if b3 = = 1:
                    b4 = input("\n---------------\nEnter search b11: ")
                    b5 = input("Enter the value of b6: ")
                    if b5.isdigit():
                        b2 = Agent()
                        self.b1 = b2.searchJobs(b4, b5)
                        keyword_input, b6 = b4, int(b5)
                    else:
                        print("Invalid value of b6, try again")
                elif b3 = = 2:
                    b2 = Agent()
                    self.b1 = b2.searchJobs(keyword_input, b6)
                elif b3 = = 3:
                    print("Clustering")
                    self.fonk4(b6)
                elif b3 = = 4:
                    print("Quitting program")
                    break
                else:
                    print("Invalid b3 selected. Try again")
            except ValueError:
                print("Invalid input. Please enter a number.")
            self.fonk3(keyword_input, b6)
    def fonk4(self, b6):
        b7 = [self.b1.pop(randint(0, len(self.b1) - 1)) for _ in range(int(b6))]
        for row in self.b1:
            b8 = (f"{row[0]} {row[1]} {row[2]} {row[3]}").lower().split(" ")
            row.append(self.fonk5(b7, b8))
        self.fonk7(self.b1, b7, b6)
    def fonk5(self, b7, b8):
        b9 = [
            self.fonk6(b8, (f"{item[0]} {item[1]} {item[2]} {item[3]}").lower().split(" "))
            for item in b7
        ]
        return min(enumerate(b9), b10 = itemgetter(1))[0]
    def fonk6(self, b11, b12):
        b11 = [keyword.lower() for keyword in b11]
        b12 = [detail.lower() for detail in b12]
        b13 = len(set(b11) & set(b12))
        b14 = len(set(b11) | set(b12))
        return 1 - b13 / float(b14)
    def fonk7(self, b1, b7, b6):
        b15 = with open("cluster.html", "w") as f:
            f.write(b15)
            for i, centroid in enumerate(b7):
                b16 = [centroid] + [job for job in b1 if job[7] == i]
                b17 = "".join(
                    f"<tr>{''.join(f'<td><a b18 = "{cell}" target="_blank">{cell}</a></td>' if j == 4 else f'<td>{cell}</td>' for j, cell in enumerate(job[:5]))}</tr>"
                    for job in b16
                )
                f.write(f"""
                <table b19 = "GeneratedTable">
                <thead>
                    <tr>
                    <th>Company Name</th>
                    <th>Position</th>
                    <th>Location</th>
                    <th>Description</th>
                    <th>Link</th>
                    </tr>
                </thead>
                <tbody>
                    {b17}
                </tbody>
                </table><br>
                """)
            f.write("</body></html>")
        webbrowser.open("cluster.html")
        print("Cluster result opened as webpage in browser")
