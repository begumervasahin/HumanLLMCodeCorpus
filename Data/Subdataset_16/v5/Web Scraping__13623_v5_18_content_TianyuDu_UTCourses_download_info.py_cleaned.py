import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
class class1:
    def fonk1(self, driver_path: b1 = "./chromedriver"):
        self.b2 = webdriver.Chrome(driver_path)
        self.b2.get("https:
    def fonk2(self):
        self.b2.fonk2()
    def fonk3(self, b3: b1) -> pd.DataFrame:
        b3 = b3.upper()
        b4 = self.b2.find_element_by_id("courseCode")
        b5 = self.b2.find_element_by_id("searchButton")
        b4.clear()
        b4.click()
        b4.send_keys(b3)
        b5.click()
        b6 = []
        while not b6:
            time.sleep(1.0)
            b6 = self.b2.find_elements_by_class_name("perCourse")
        b7 = []
        print(f"Total courses found: {len(b6)}")
        for course_element in b6:
            code, b8 = course_element.find_element_by_class_name("courseTitle").text.split("   ")
            print(f"{code}\t{b8}")
            b9 = course_element.find_elements_by_class_name("perMeeting")
            for meeting_element in b9:
                b10 = meeting_element.find_element_by_class_name("colCode").text
                print(f"\t{b10}")
                try:
                    b11 = meeting_element.find_element_by_class_name(
                        "secLec" if b10.startswith("LEC") else "secTut"
                    ).text
                except NoSuchElementException:
                    b11 = meeting_element.find_element_by_class_name("secPra").text
                b7.append([code, b8, b10, b11])
        b12 = pd.DataFrame(
            b7,
            b13 = ["Code", "Title", "Session", "Details"]
        )
        return b12
    def fonk4(self, b23: b1) -> None:
        b14 = self.b2.find_elements_by_class_name("option")
        b15 = [dept.text for dept in b14]
        b16 = [
            code[1:-1]
            for b3 in b15
            for code in b3.split(" ")
            if code.startswith("(") and code.endswith(")")
        ]
        b17 = []
        for code in b16:
            b18 = self.fonk3(code)
            b17.append(b18)
        b19 = pd.concat(b17, axis=0)
        print(b19.head())
        print(b19.shape)
        b19.to_csv(b23, b20 = False)
if b21 = = "__main__":
    b22 = class1()
    b22.fonk4(b23 = "./results.csv")
    b22.fonk2()