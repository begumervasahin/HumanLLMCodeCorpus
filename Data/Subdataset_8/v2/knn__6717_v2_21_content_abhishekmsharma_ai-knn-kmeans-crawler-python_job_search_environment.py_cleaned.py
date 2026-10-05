from job_search_agent import Agent
from random import randint
from operator import itemgetter
import webbrowser
class Environment:
    all_jobs = []
    def __init__(self):
        pass
    def run(self):
        keyword_input, k = self.prompt_user_for_search()
        self.fetch_and_print_menu(keyword_input, k)
    def prompt_user_for_search(self):
        print("\n--------------------\nType the corresponding number and press enter")
        print("1. Start a new search")
        print("2. Run previous search again")
        print("3. Cluster previous search")
        print("4. Quit")
        option = input("Enter the number: ")
        try:
            option = int(option)
            if option == 1:
                return self.get_new_search_params()
            elif option == 2 or option == 3:
                if not self.all_jobs:
                    print("No previous search to run.")
                    return self.get_new_search_params()
                elif option == 3:
                    self.cluster_jobs()
                return keyword_input, k
            elif option == 4:
                print("Quitting program")
                exit(0)
            else:
                print("Invalid option selected. Please try again.")
                return self.prompt_user_for_search()
        except ValueError:
            print("Invalid option selected. Please try again.")
            return self.prompt_user_for_search()
    def get_new_search_params(self):
        keyword_input = input("\n---------------\nEnter search keywords: ")
        k = input("Enter the value of k: ")
        if k.isdigit():
            a = Agent()
            self.all_jobs = a.searchJobs(keyword_input, k)
            return keyword_input, k
        else:
            print("Invalid value of k. Please try again.")
            return self.get_new_search_params()
    def fetch_and_print_menu(self, keyword_input, k):
        print("Keywords:", keyword_input, ", Value of k:", k)
        self.printMenu(keyword_input, k)
    def printMenu(self, keyword_input, k):
        pass
    def cluster_jobs(self):
        pass
    def getClosestCentroid(self, centroid_jobs, jobs_words):
        pass
    def jaccardDistance(self, keywords, job_details):
        pass
    def printHTMLTable(self, all_jobs, centroid_jobs, k):
        pass
if __name__ == '__main__':
    env = Environment()
    env.run()