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
            print("\n--------------------\nType the corresponding number and press enter")
            print("1. Start a new search")
            print(f"2. Run previous search again - Keywords: {keyword_input}, Value of k: {k}")
            print(f"3. Cluster previous search - Keywords: {keyword_input}, Value of k: {k}")
            print("4. Quit")
            try:
                option = int(input("Enter the number: "))
                if option == 1:
                    keyword_input, k = self.start_new_search()
                elif option == 2:
                    agent = Agent()
                    self.all_jobs = agent.searchJobs(keyword_input, k)
                elif option == 3:
                    print("Clustering")
                    self.cluster_jobs(k)
                elif option == 4:
                    print("Quitting program")
                    break
                else:
                    print("Invalid option selected. Try again")
            except ValueError:
                print("Invalid input. Please enter a number.")
    def start_new_search(self):
        keyword_input = input("\n---------------\nEnter search keywords: ")
        k = input("Enter the value of k: ")
        if k.isdigit():
            agent = Agent()
            self.all_jobs = agent.searchJobs(keyword_input, int(k))
            return keyword_input, int(k)
        else:
            print("Invalid value of k, try again")
            return self.start_new_search()
    def cluster_jobs(self, k):
        centroid_jobs = [self.all_jobs.pop(randint(0, len(self.all_jobs) - 1)) for _ in range(int(k))]
        for row in self.all_jobs:
            job_words = self.extract_words_from_job(row)
            row.append(self.get_closest_centroid(centroid_jobs, job_words))
        self.print_html_table(self.all_jobs, centroid_jobs, k)
    def extract_words_from_job(self, job):
        return (f"{job[0]} {job[1]} {job[2]} {job[3]}").lower().split(" ")
    def get_closest_centroid(self, centroid_jobs, job_words):
        jaccard_distances = [
            self.jaccard_distance(job_words, self.extract_words_from_job(item))
            for item in centroid_jobs
        ]
        return min(enumerate(jaccard_distances), key=itemgetter(1))[0]
    def jaccard_distance(self, keywords, job_details):
        intersection = len(set(keywords) & set(job_details))
        union = len(set(keywords) | set(job_details))
        return 1 - intersection / float(union)
    def print_html_table(self, all_jobs, centroid_jobs, k):
        table_header =
        with open("cluster.html", "w") as f:
            f.write(table_header.format(k=k))
            for i, centroid in enumerate(centroid_jobs):
                cluster_jobs = [centroid] + [job for job in all_jobs if job[7] == i]
                table_rows = self.generate_table_rows(cluster_jobs)
                f.write(f"""
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
                <tbody>
                    {table_rows}
                </tbody>
                </table><br>
                """)
            f.write("</body></html>")
        webbrowser.open("cluster.html")
        print("Cluster result opened as webpage in browser")
    def generate_table_rows(self, cluster_jobs):
        return "".join(
            f"<tr>{''.join(f'<td><a href="{cell}" target="_blank">{cell}</a></td>' if j == 4 else f'<td>{cell}</td>' for j, cell in enumerate(job[:5]))}</tr>"
            for job in cluster_jobs
        )
