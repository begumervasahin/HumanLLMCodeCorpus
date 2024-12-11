from job_search_agent import Agent
import webbrowser
class class1:
    b1 = []
    def fonk1(self):
        pass
    def fonk2(self):
        b4, b2 = self.fonk3()
        self.fonk5(b4, b2)
    def fonk3(self):
        print("\n--------------------\nType the corresponding number and press enter")
        print("1. Start b5 new search")
        print("2. Run previous search again")
        print("3. Cluster previous search")
        print("4. Quit")
        b3 = input("Enter the number: ")
        try:
            b3 = int(b3)
            if b3 = = 1:
                return self.fonk4()
            elif b3 = = 2 or b3 == 3:
                if not self.b1:
                    print("No previous search to run.")
                    return self.fonk4()
                elif b3 = = 3:
                    self.fonk7()
                return b4, b2
            elif b3 = = 4:
                print("Quitting program")
                exit(0)
            else:
                print("Invalid b3 selected. Please try again.")
                return self.fonk3()
        except ValueError:
            print("Invalid b3 selected. Please try again.")
            return self.fonk3()
    def fonk4(self):
        b4 = input("\n---------------\nEnter search keywords: ")
        b2 = input("Enter the value of b2: ")
        if b2.isdigit():
            b5 = Agent()
            self.b1 = b5.searchJobs(b4, b2)
            return b4, b2
        else:
            print("Invalid value of b2. Please try again.")
            return self.fonk4()
    def fonk5(self, b4, b2):
        print("Keywords:", b4, ", Value of b2:", b2)
        self.fonk6(b4, b2)
    def fonk6(self, b4, b2):
        pass
    def fonk7(self):
        pass
    def fonk8(self, centroid_jobs, jobs_words):
        pass
    def fonk9(self, keywords, job_details):
        pass
    def fonk10(self, b1, centroid_jobs, b2):
        pass
if b6 = = '__main__':
    b7 = class1()
    b7.fonk2()