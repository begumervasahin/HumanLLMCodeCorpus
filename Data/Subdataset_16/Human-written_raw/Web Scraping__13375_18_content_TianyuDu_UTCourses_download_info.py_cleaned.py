import numpy as np
import pandas as pd
import selenium
from selenium import webdriver
import time
class class1():
    def fonk1(self):
        self.b1 = webdriver.Chrome("./chromedriver")
        self.b1.get("https:
    def fonk2(self):
        self.b1.fonk2()
    def fonk3(self, b2: str) -> pd.DataFrame:
        b2 = b2.upper()
        b3 = self.b1.find_element_by_id("courseCode")
        b4 = self.b1.find_element_by_id("searchButton")
        b3.clear()
        b3.click()
        b3.send_keys(b2)
        b4.click()
        b5 = []
        while b5 = = []:
            time.sleep(1.0)
            b5 = self.b1.find_elements_by_class_name("perCourse")
        b6 = []
        print(f"Total courses found: {len(b5)}")
        for course in b5:
            code, b7 = course.find_element_by_class_name("courseTitle").text.split("   ")
            print(f"{code}\t{b7}")
            b8 = course.find_elements_by_class_name("perMeeting")
            for meeting in b8:
                b9 = meeting.find_element_by_class_name("colCode").text
                print(f"\t{b9}")
                try:
                    b10 = meeting.find_element_by_class_name(
                        "secLec" if b9.startswith("LEC") else "secTut").text
                except selenium.common.exceptions.NoSuchElementException:
                    b10 = meeting.find_element_by_class_name("secPra").text
                b11 = [code, b7, b9, b10]
                b6.append(b11)
        b12 = pd.DataFrame(
            np.array(b6),
            b13 = ["Code", "Title", "Session", "Details"]
        )
        return b12
    def fonk4(self, b15: list, b21: str) -> None:
        b14 = [
            x.text
            for x in self.b1.find_elements_by_class_name("option")
        ]
        print(b14)
        b15 = [
            x[1:-1]
            for dep in b14
            for x in dep.split(" ")
            if x.startswith("(") and x.endswith(")")
        ]
        b16 = []
        for x in b15:
            b17 = self.fonk3(x)
            b16.append(b17)
        b18 = pd.concat(b16, axis=0)
        print(b18.head())
        print(b18.shape)
        b18.to_csv(b21)
if b19 = = "__main__":
    b20 = class1()
    b15 = ["MAT"]
    b20.fonk4(b15, b21 = "./results.csv")
    b20.fonk2()