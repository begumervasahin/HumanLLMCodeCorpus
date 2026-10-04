from selenium import webdriver
from selenium.webdriver.common.by import By
import re
file_name = input("Enter a file name to be saved: ")
pattern = input("Enter pattern: ")
with open(f"{file_name}.txt", "w") as file:
    PATH = "/usr/lib/chromium-browser/chromedriver"
    browser = webdriver.Chrome(executable_path=PATH)
    url = "https:
    browser.get(url)
    detained = 0
    def find_results(pattern, start, end):
        global detained
        for i in range(start, end + 1):
            try:
                htno = pattern + str(i).zfill(3)
                htno_input = browser.find_element(By.NAME, 'htno')
                htno_input.clear()
                htno_input.send_keys(htno)
                browser.find_element(By.NAME, 'Submit').click()
                details_table = browser.find_element(By.ID, 'AutoNumber3').text
                pin_area = re.search(r"\d{12}", details_table).span()
                pin_no = details_table[pin_area[0]:pin_area[1]]
                name_span = re.search(r"Name [A-Z .]*\s", details_table).span()
                file.write("\n\n-------------------------------------------------------------\n")
                file.write(f"PIN NO: {pin_no}\t{details_table[name_span[0]:name_span[-1]]}\n")
                file.write("-------------------------------------------------------------\n")
                marks_table = browser.find_element(By.ID, 'AutoNumber4').text
                marks_list = marks_table.splitlines()
                for subject in marks_list[2:]:
                    subject_code_span = re.search(r"\d{3}", subject).span()
                    subject_code = subject[subject_code_span[0]:subject_code_span[1]]
                    subject_name = re.findall(r"[A-Z -.&]*", subject)[4]
                    subject_grade_secured = subject[-1]
                    gpa_scored = re.findall(r"\d+", subject)[-1]
                    file.write(f"{subject_code}\t{subject_name}\t\t{gpa_scored}\n")
                result_table = browser.find_element(By.ID, 'AutoNumber5').text
                result_lines = result_table.splitlines()
                if "DETAINED" in result_lines[-1]:
                    detained += 1
                file.write(f"RESULT: {result_lines[-1]}\n")
                file.write("-------------------------------------------------------------\n\n\n\n")
            except Exception as e:
                print(e)
                file.write("---------SKIPPING ONE PIN HERE-------------\n\n\n")
    find_results(pattern, 1, 59)
    find_results(pattern, 301, 311)
    file.seek(0, 0)
    file.write(f"NO. OF STUDENTS DETAINED: {detained}\n")
browser.quit()