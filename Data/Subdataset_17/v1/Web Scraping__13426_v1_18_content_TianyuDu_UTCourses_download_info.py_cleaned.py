import numpy as np
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("https:
    def close(self):
        self.driver.close()
    def batch_retrieve(self, department: str) -> pd.DataFrame:
        department = department.upper()
        search_box = self.driver.find_element(By.ID, "courseCode")
        search_button = self.driver.find_element(By.ID, "searchButton")
        search_box.clear()
        search_box.click()
        search_box.send_keys(department)
        search_button.click()
        course_lst = []
        while not course_lst:
            time.sleep(1.0)
            course_lst = self.driver.find_elements(By.CLASS_NAME, "perCourse")
        course_info_lst = []
        print(f"Total courses found: {len(course_lst)}")
        for course in course_lst:
            code, title = course.find_element(By.CLASS_NAME, "courseTitle").text.split("   ")
            print(f"{code}\t{title}")
            meeting_lst = course.find_elements(By.CLASS_NAME, "perMeeting")
            for meeting in meeting_lst:
                meeting_code = meeting.find_element(By.CLASS_NAME, "colCode").text
                print(f"\t{meeting_code}")
                try:
                    meeting_info = meeting.find_element(By.CLASS_NAME, "secLec" if meeting_code.startswith("LEC") else "secTut").text
                except selenium.common.exceptions.NoSuchElementException:
                    meeting_info = meeting.find_element(By.CLASS_NAME, "secPra").text
                info = [code, title, meeting_code, meeting_info]
                course_info_lst.append(info)
        course_info_df = pd.DataFrame(
            np.array(course_info_lst),
            columns=["Code", "Title", "Session", "Details"]
        )
        return course_info_df
    def batch_download(self, code_lst: list, save_dir: str) -> None:
        department_lst = [
            x.text
            for x in self.driver.find_elements(By.CLASS_NAME, "option")
        ]
        print(department_lst)
        code_lst = [
            x[1:-1]
            for dep in department_lst
            for x in dep.split(" ")
            if x.startswith("(") and x.endswith(")")
        ]
        all_courses = []
        for x in code_lst:
            y = self.batch_retrieve(x)
            all_courses.append(y)
        df = pd.concat(all_courses, axis=0)
        print(df.head())
        print(df.shape)
        df.to_csv(save_dir, index=False)
if __name__ == "__main__":
    b = Bot()
    code_lst = ["MAT"]
    b.batch_download(code_lst, save_dir="./results.csv")
    b.close()