'''
Developer: Abhishek Manoj Sharma
Date: September 27, 2017
Class: Environment
'''
from job_search_agent import Agent
from random import randint
from operator import itemgetter
import webbrowser
class Environment:
    all_jobs = []
    def envFirstRun(self, keyword_input, k):
        a = Agent()
        self.all_jobs = a.searchJobs(keyword_input, k)
        self.printMenu(keyword_input, k)
    def printMenu(self, keyword_input, k):
        print("\n--------------------\nType the corresponding number and press enter")
        print("1. Start a new search")
        print("2. Run previous search again - Keywords:", keyword_input, ", Value of k:", k)
        print("3. Cluster previous search - Keywords:", keyword_input, ", Value of k:", k)
        print("4. Quit")
        option = input("Enter the number: ")
        try:
            option = int(option)
            if option == 1:
                keyword_input_new = input("\n---------------\nEnter search keywords: ")
                k_new = input("Enter the value of k: ")
                if k_new.isdigit():
                    a = Agent()
                    self.all_jobs = a.searchJobs(keyword_input_new, k_new)
                    self.printMenu(keyword_input_new, k_new)
                else:
                    print("Invalid value of k, try again")
                    self.printMenu(keyword_input, k)
            elif option == 2:
                a = Agent()
                self.all_jobs = a.searchJobs(keyword_input, k)
                self.printMenu(keyword_input, k)
            elif option == 3:
                print("Clustering")
                self.clusterJobs(k)
                self.printMenu(keyword_input, k)
            elif option == 4:
                print("Quitting program")
                exit(0)
            else:
                print("Invalid option selected.\nTry again")
                self.printMenu(keyword_input, k)
        except ValueError:
            print("Invalid option selected.\nTry again")
            self.printMenu(keyword_input, k)
    def clusterJobs(self, k):
        centroid_jobs = []
        for i in range(0, int(k)):
            r = randint(0, len(self.all_jobs) - 1)
            centroid_jobs.append(self.all_jobs[r])
            self.all_jobs.pop(r)
        for row in self.all_jobs:
            job_words = (row[0] + " " + row[1] + " " + row[2] + " " + row[3]).lower()
            job_words = job_words.split(" ")
            row.append(self.getClosestCentroid(centroid_jobs, job_words))
        self.printHTMLTable(self.all_jobs, centroid_jobs, k)
    def getClosestCentroid(self, centroid_jobs, jobs_words):
        jaccard_distances = []
        for item in centroid_jobs:
            centroid_words = (item[0] + " " + item[1] + " " + item[2] + " " + item[3]).lower()
            centroid_words = centroid_words.split(" ")
            jaccard_distances.append(self.jaccardDistance(jobs_words, centroid_words))
        return min(enumerate(jaccard_distances), key=itemgetter(1))[0]
    def jaccardDistance(self, keywords, job_details):
        keywords = [word.lower() for word in keywords]
        job_details = [word.lower() for word in job_details]
        intersection = len(set(keywords).intersection(set(job_details)))
        union = len(set(keywords).union(set(job_details)))
        return 1 - intersection / float(union)
    def printHTMLTable(self, all_jobs, centroid_jobs, k):
        table_1 =  + str(k) +
        with open("cluster.html", "w") as f:
            f.write(table_1)
            for i in range(len(centroid_jobs)):
                table_text = """<table class="GeneratedTable">
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
                f.write(table_text)
                cluster_jobs = [centroid_jobs[i]]
                for item in all_jobs:
                    if item[-1] == i:
                        cluster_jobs.append(item)
                for item in cluster_jobs:
                    f.write("<tr>")
                    for j in range(5):
                        f.write("<td>")
                        if j == 4:
                            f.write(f'<a target="_blank" href="{item[j]}">{item[j]}</a>')
                        else:
                            f.write(item[j])
                        f.write("</td>")
                    f.write("</tr>")
                f.write("</tbody></table><br>")
            f.write("</body></html>")
        webbrowser.open("cluster.html")
        print("Cluster result opened as webpage in browser")
env = Environment()
keyword_input = input("Enter search keywords: ")
k = input("Enter the value of k: ")
env.envFirstRun(keyword_input, k)