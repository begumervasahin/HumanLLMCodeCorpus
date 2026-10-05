from job_search_agent import Agent
from random import randint
from operator import itemgetter
import webbrowser
class class1:
    b1 = []
    def fonk1(self):
        pass
    def fonk2(self, b4, b5):
        b2 = Agent()
        self.b1 = b2.search_jobs(b4, b5)
        self.fonk3(b4, b5)
    def fonk3(self, b4, b5):
        print("\n--------------------\nType the corresponding number and press enter")
        print("1. Start a new search")
        print("2. Run previous search again - Keywords:", b4, ", Value of b5:", b5)
        print("3. Cluster previous search - Keywords:", b4, ", Value of b5:", b5)
        print("4. Quit")
        b3 = input("Enter the number: ")
        try:
            b3 = int(b3)
            if b3 = = 1:
                self.fonk4()
            elif b3 = = 2:
                self.fonk5(b4, b5)
            elif b3 = = 3:
                self.fonk6(b5)
            elif b3 = = 4:
                self.fonk12()
            else:
                print("Invalid b3 selected.\nTry again")
                self.fonk3(b4, b5)
        except ValueError:
            print("Invalid b3 selected.\nTry again")
            self.fonk3(b4, b5)
    def fonk4(self):
        b4 = input("\n---------------\nEnter search b11: ")
        b5 = input("Enter the value of b5: ")
        if b5.isdigit():
            b2 = Agent()
            self.b1 = b2.search_jobs(b4, b5)
            self.fonk3(b4, b5)
        else:
            print("Invalid value of b5, try again")
            self.fonk3(b4, b5)
    def fonk5(self, b4, b5):
        b2 = Agent()
        self.b1 = b2.search_jobs(b4, b5)
        self.fonk3(b4, b5)
    def fonk6(self, b5):
        b6 = self.fonk7(b5)
        self.fonk8(b6)
        self.fonk11(self.b1, b6, b5)
    def fonk7(self, b5):
        b6 = []
        for i in range(0, int(b5)):
            b7 = randint(0, len(self.b1) - 1)
            b6.append(self.b1[b7])
            self.b1.pop(b7)
        return b6
    def fonk8(self, b6):
        for row in self.b1:
            b8 = (row[0] + " " + row[1] + " " + row[2] + " " + row[3]).lower().split(" ")
            row.append(self.fonk9(b6, b8))
    def fonk9(self, b6, jobs_words):
        b9 = [self.fonk10(jobs_words, (item[0] + " " + item[1] + " " + item[2] + " " + item[3]).lower().split(" ")) for item in b6]
        return min(enumerate(b9), b10 = itemgetter(1))[0]
    def fonk10(self, b11, b12):
        b11 = [kw.lower() for kw in b11]
        b12 = [jd.lower() for jd in b12]
        b13 = len(set(b11).b13(b12))
        b14 = len(set(b11).b14(b12))
        return 1 - b13 / float(b14)
    def fonk11(self, b1, b6, b5):
        b15 = + str(b5) + "</h4>"
        b16 = open("cluster.html", "w")
        b16.write(b15)
        for i in range(0, len(b6)):
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
            b16.write(b17)
            b18 = [b6[i]] + [item for item in b1 if item[7] == i]
            for item in b18:
                b16.write("<tr>")
                for b19 in range(0, 5):
                    b16.write("<td>")
                    if b19 = = 4:
                        b16.write('<a b20 = "_blank" href="')
                        b16.write(item[b19])
                        b16.write('">')
                        b16.write(item[b19])
                        b16.write("</a>")
                    else:
                        b16.write(item[b19])
                    b16.write("</td>")
                b16.write("</tr>")
            b16.write("</tbody></table><br>")
        b16.write("</body></html>")
        b16.close()
        webbrowser.open("cluster.html")
        print("Cluster result opened as webpage in browser")
    def fonk12(self):
        print("Quitting program")
        exit(0)