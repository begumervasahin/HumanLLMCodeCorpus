
from job_search_agent import Agent
from random import randint
from operator import itemgetter
import webbrowser
class Environment:
    def __init__(self):
        self.all_jobs = []
    def env_first_run(self, keyword_input, k):
        agent = Agent()
        self.all_jobs = agent.searchJobs(keyword_input, k)
        self.print_menu(keyword_input, k)
    def print_menu(self, keyword_input, k):
        while True:
            print("\n--------------------")
            print("Type the corresponding number and press enter")
            print("1. Start a new search")
            print(f"2. Run previous search again - Keywords: {keyword_input}, Value of k: {k}")
            print(f"3. Cluster previous search - Keywords: {keyword_input}, Value of k: {k}")
            print("4. Quit")
            option = input("Enter the number: ")
            if option.isdigit():
                option = int(option)
            else:
                print("Invalid option selected. Try again.")
                continue
            if option == 1:
                self.new_search()
            elif option == 2:
                self.run_previous_search(keyword_input, k)
            elif option == 3:
                self.cluster_jobs(k)
            elif option == 4:
                print("Quitting program")
                exit(0)
            else:
                print("Invalid option selected. Try again.")
    def new_search(self):
        keyword_input = input("\n---------------\nEnter search keywords: ")
        k = input("Enter the value of k: ")
        if k.isdigit():
            agent = Agent()
            self.all_jobs = agent.searchJobs(keyword_input, k)
            self.print_menu(keyword_input, k)
        else:
            print("Invalid value of k, try again")
            self.print_menu(keyword_input, k)
    def run_previous_search(self, keyword_input, k):
        agent = Agent()
        self.all_jobs = agent.searchJobs(keyword_input, k)
        self.print_menu(keyword_input, k)
    def cluster_jobs(self, k):
        print("Clustering")
        centroid_jobs = self.select_centroids(k)
        for job in self.all_jobs:
            job_description = ' '.join(job[:4]).lower().split()
            closest_centroid = self.get_closest_centroid(centroid_jobs, job_description)
            job.append(closest_centroid)
        self.print_html_table(self.all_jobs, centroid_jobs, k)
    def select_centroids(self, k):
        centroids = []
        for _ in range(int(k)):
            random_index = randint(0, len(self.all_jobs) - 1)
            centroids.append(self.all_jobs.pop(random_index))
        return centroids
    def get_closest_centroid(self, centroids, job_words):
        distances = [self.jaccard_distance(job_words, ' '.join(centroid[:4]).lower().split()) for centroid in centroids]
        return min(enumerate(distances), key=itemgetter(1))[0]
    def jaccard_distance(self, set1, set2):
        set1, set2 = set(set1), set(set2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return 1 - intersection / union
    def print_html_table(self, all_jobs, centroid_jobs, k):
        html_content = f
        with open("cluster.html", "w") as file:
            file.write(html_content)
            for i, centroid in enumerate(centroid_jobs):
                file.write(self.create_table(centroid, all_jobs, i))
            file.write("</body></html>")
        webbrowser.open("cluster.html")
        print("Cluster result opened as webpage in browser")
    def create_table(self, centroid, all_jobs, cluster_index):
        table = """
        <table class="GeneratedTable">
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
        cluster_jobs = [job for job in all_jobs if job[-1] == cluster_index]
        cluster_jobs.insert(0, centroid)
        for job in cluster_jobs:
            table += "<tr>" + ''.join(f'<td><a target="_blank" href="{job[4]}">{job[4]}</a></td>' if i == 4 else f'<td>{job[i]}</td>' for i in range(5)) + "</tr>"
        table += "</tbody></table><br>"
        return table
if __name__ == "__main__":
    env = Environment()
    keyword_input = input("Enter search keywords: ")
    k = input("Enter the value of k: ")
    env.env_first_run(keyword_input, k)