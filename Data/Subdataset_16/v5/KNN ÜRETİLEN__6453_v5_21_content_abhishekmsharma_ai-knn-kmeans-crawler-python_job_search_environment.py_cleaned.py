from job_search_agent import Agent
from random import randint
from operator import itemgetter
import webbrowser
b15 class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, b5, b4):
        b2 = Agent()
        self.b1 = b2.searchJobs(b5, b4)
        self.fonk3(b5, b4)
    def fonk3(self, b5, b4):
        while True:
            print("\n--------------------\nType the corresponding number and press enter")
            print("1. Start a new search")
            print(f"2. Run previous search again - Keywords: {b5}, Value of b4: {b4}")
            print(f"3. Cluster previous search - Keywords: {b5}, Value of b4: {b4}")
            print("4. Quit")
            try:
                b3 = int(input("Enter the number: "))
                if b3 = = 1:
                    b5, b4 = self.fonk4()
                elif b3 = = 2:
                    b2 = Agent()
                    self.b1 = b2.searchJobs(b5, b4)
                elif b3 = = 3:
                    print("Clustering")
                    self.fonk5(b4)
                elif b3 = = 4:
                    print("Quitting program")
                    break
                else:
                    print("Invalid b3 selected. Try again")
            except ValueError:
                print("Invalid input. Please enter a number.")
    def fonk4(self):
        b5 = input("\n---------------\nEnter search keywords: ")
        b4 = input("Enter the value of b4: ")
        if b4.isdigit():
            b2 = Agent()
            self.b1 = b2.searchJobs(b5, int(b4))
            return b5, int(b4)
        else:
            print("Invalid value of b4, try again")
            return self.fonk4()
    def fonk5(self, b4):
        b6 = [self.b1.pop(randint(0, len(self.b1) - 1)) for _ in range(int(b4))]
        for row in self.b1:
            b7 = self.fonk6(row)
            row.append(self.fonk7(b6, b7))
        self.fonk9(self.b1, b6, b4)
    def fonk6(self, job):
        return (f"{job[0]} {job[1]} {job[2]} {job[3]}").lower().split(" ")
    def fonk7(self, b6, b7):
        b8 = [
            self.fonk8(b7, self.fonk6(item))
            for item in b6
        ]
        return min(enumerate(b8), b9 = itemgetter(1))[0]
    def fonk8(self, keywords, job_details):
        b10 = len(set(keywords) & set(job_details))
        b11 = len(set(keywords) | set(job_details))
        return 1 - b10 / float(b11)
    def fonk9(self, b1, b6, b4):
        b12 = with open("cluster.html", "w") as f:
            f.write(b12.format(b4 = b4))
            for i, centroid in enumerate(b6):
                b13 = [centroid] + [job for job in b1 if job[7] == i]
                b14 = self.fonk10(b13)
                f.write(f"""
                <table b15 = "GeneratedTable">
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
                    {b14}
                </tbody>
                </table><br>
                """)
            f.write("</body></html>")
        webbrowser.open("cluster.html")
        print("Cluster result opened as webpage in browser")
    def fonk10(self, b13):
        return "".join(
            f"<tr>{''.join(f'<td><a b16 = "{cell}" target="_blank">{cell}</a></td>' if j == 4 else f'<td>{cell}</td>' for j, cell in enumerate(job[:5]))}</tr>"
            for job in b13
        )
