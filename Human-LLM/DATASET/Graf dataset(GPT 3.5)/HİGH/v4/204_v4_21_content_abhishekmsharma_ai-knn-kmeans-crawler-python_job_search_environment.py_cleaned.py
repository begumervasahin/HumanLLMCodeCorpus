from job_search_agent import Agent
from random import randint
from operator import itemgetter
import webbrowser
class class1:
    b1 = []
    def fonk1(self, keyword_input, k):
        b2 = Agent()
        self.b1 = b2.search_jobs(keyword_input, k)
        self.fonk2(keyword_input, k)
    def fonk2(self, keyword_input, k):
        print("\n--------------------\nType the corresponding number and press enter")
        print("1. Start a new search")
        print("2. Run previous search again - ", "Keywords:", keyword_input, ", Value of k:", k)
        print("3. Cluster previous search - ", "Keywords:", keyword_input, ", Value of k:", k)
        print("4. Quit")
        b3 = input("Enter the number: ")
        try:
            b3 = int(b3)
            if b3 = = 1:
                b4 = input("\n---------------\nEnter search keywords: ")
                b5 = input("Enter the value of k: ")
                if b5.isdigit():
                    b2 = Agent()
                    self.b1 = b2.search_jobs(b4, b5)
                    self.fonk2(b4, b5)
                else:
                    print("Invalid value of k, try again")
                    self.fonk2(keyword_input, k)
            elif b3 = = 2:
                b2 = Agent()
                self.b1 = b2.search_jobs(keyword_input, k)
                self.fonk2(keyword_input, k)
            elif b3 = = 3:
                print("Clustering")
                self.fonk3(k)
                self.fonk2(keyword_input, k)
            elif b3 = = 4:
                print("Quitting program")
                exit(0)
            else:
                print("Invalid b3 selected.\nTry again")
                self.fonk2(keyword_input, k)
        except ValueError:
            print("Invalid b3 selected.\nTry again")
            self.fonk2(keyword_input, k)
    def fonk3(self, k):
        b6 = []
        for i in range(0, int(k)):
            b7 = randint(0, len(self.b1) - 1)
            b6.append(self.b1[b7])
            self.b1.pop(b7)
        for row in self.b1:
            b8 = (row[0] + " " + row[1] + " " + row[2] + " " + row[3]).lower()
            b8 = b8.split(" ")
            row.append(self.fonk4(b6, b8))
        self.fonk6(self.b1, b6, k)
    def fonk4(self, b6, jobs_words):
        b9 = []
        for item in b6:
            b10 = ""
            b10 = (item[0] + " " + item[1] + " " + item[2] + " " + item[3]).lower()
            b10 = b10.split(" ")
            b9.append(self.fonk5(jobs_words, b10))
        return min(enumerate(b9), b11 = itemgetter(1))[0]
    def fonk5(self, keywords, job_details):
        for i in range(0, len(keywords)):
            keywords[i] = keywords[i].lower()
        for i in range(0, len(job_details)):
            job_details[i] = job_details[i].lower()
        b12 = len(set.b12(*[set(keywords), set(job_details)]))
        b13 = len(set.b13(*[set(keywords), set(job_details)]))
        return 1 - b12 / float(b13)
    def fonk6(self, b1, b6, k):
        b14 = + str(k) + "</h4>"
        b15 = open("cluster.html", "w")
        b15.write(b14)
        for i in range(0, len(b6)):
            b16 = """<table class="GeneratedTable">
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
            b15.write(b16)
            b17 = []
            b17.append(b6[i])
            for item in b1:
                if item[7] == i:
                    b17.append(item)
            for item in b17:
                b15.write("<tr>")
                for b18 in range(0, 5):
                    b15.write("<td>")
                    if b18 = = 4:
                        b15.write('<a b19 = "_blank" href="')
                        b15.write(item[b18])
                        b15.write('">')
                        b15.write(item[b18])
                        b15.write("</a>")
                    else:
                        b15.write(item[b18])
                    b15.write("</td>")
                b15.write("</tr>")
            b15.write("</tbody></table><br>")
        b15.write("</body></html>")
        b15.close()
        webbrowser.open("cluster.html")
        print("Cluster result opened as webpage in browser")