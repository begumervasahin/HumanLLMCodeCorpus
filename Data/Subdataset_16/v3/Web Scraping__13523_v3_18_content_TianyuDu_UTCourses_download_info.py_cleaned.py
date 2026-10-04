import numpy as np
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class class1:
    def fonk1(self, driver_path: str, url: str):
        self.b1 = webdriver.Chrome(driver_path)
        self.b1.get(url)
    def fonk2(self):
        self.b1.fonk2()
    def fonk3(self, b2: str) -> pd.DataFrame:
        b2 = b2.upper()
        b3 = self.b1.find_element(By.ID, "courseCode")
        b4 = self.b1.find_element(By.ID, "searchButton")
        b3.clear()
        b3.send_keys(b2)
        b4.click()
        b5 = []
        while not b5:
            time.sleep(1.0)
            b5 = self.b1.find_elements(By.CLASS_NAME, "perCourse")
        b6 = []
        print(f"Total courses found: {len(b5)}")
        for course_element in b5:
            code, b7 = course_element.find_element(By.CLASS_NAME, "courseTitle").text.split("   ")
            print(f"{code}\t{b7}")
            b8 = course_element.find_elements(By.CLASS_NAME, "perMeeting")
            for meeting_element in b8:
                b9 = meeting_element.find_element(By.CLASS_NAME, "colCode").text
                print(f"\t{b9}")
                b10 = self.fonk4(meeting_element, b9)
                b6.append([code, b7, b9, b10])
        b11 = pd.DataFrame(
            b6,
            b12 = ["Code", "Title", "Session", "Details"]
        )
        return b11
    def fonk4(self, meeting_element, b9):
        try:
            if b9.startswith("LEC"):
                return meeting_element.find_element(By.CLASS_NAME, "secLec").text
            else:
                return meeting_element.find_element(By.CLASS_NAME, "secTut").text
        except selenium.common.exceptions.NoSuchElementException:
            return meeting_element.find_element(By.CLASS_NAME, "secPra").text
    def fonk5(self, b21: str) -> None:
        b13 = self.b1.find_elements(By.CLASS_NAME, "option")
        b14 = [
            option.text.split(" ")[0][1:-1]
            for option in b13
            if option.text.startswith("(") and option.text.endswith(")")
        ]
        b15 = []
        for code in b14:
            b16 = self.fonk3(code)
            b15.append(b16)
        b17 = pd.concat(b15, axis=0)
        print(b17.head())
        print(b17.shape)
        b17.to_csv(b21, b18 = False)
if b19 = = "__main__":
    b20 = class1(driver_path="./chromedriver", url="https:
    b20.fonk5(b21 = "./results.csv")
    b20.fonk2()