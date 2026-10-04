from selenium import webdriver
import re
def format_htno(base_htno, number):
    return base_htno[:-len(str(number))] + str(number)
def write_result_header(file, pin_no, name):
    file.write("\n\n-------------------------------------------------------------\n")
    file.write(f"PIN NO : {pin_no}\t{name}\n")
    file.write("-------------------------------------------------------------\n")
def write_marks_details(file, marks_list):
    for subject in marks_list[2:]:
        subject_code = re.search(r"\d{3}", subject).group()
        subject_name = re.findall(r"[A-Z -.&]*", subject)[4]
        gpa_scored = re.findall(r"\d+", subject)[-1]
        file.write(f"{subject_code}\t{subject_name}\t\t{gpa_scored}\n")
def find_results(browser, file, pattern, start, end):
    global detained
    base_htno = pattern + "000"
    for i in range(start, end + 1):
        try:
            htno = format_htno(base_htno, i)
            browser.find_element_by_name('htno').send_keys(htno)
            browser.find_element_by_name('Submit').click()
            details_table = browser.find_element_by_id('AutoNumber3').text
            pin_no = re.search(r"\d{12}", details_table).group()
            name = re.search(r"Name [A-Z .]*\s", details_table).group()
            write_result_header(file, pin_no, name)
            marks_table = browser.find_element_by_id('AutoNumber4').text
            marks_list = marks_table.splitlines()
            write_marks_details(file, marks_list)
            result_table = browser.find_element_by_id('AutoNumber5').text
            result_lines = result_table.splitlines()
            if "DETAINED" in result_lines[-1]:
                detained += 1
            file.write(f"RESULT : {result_lines[-1]}\n")
            file.write("-------------------------------------------------------------\n\n\n\n")
        except Exception as e:
            print(e)
            file.write("---------SKIPPING ONE PIN HERE-------------\n\n\n")
if __name__ == "__main__":
    file_name = input("ENTER A FILE NAME TO BE SAVED: ")
    pattern = input("ENTER PATTERN: ")
    with open(f"{file_name}.txt", "w") as file:
        PATH = "/usr/lib/chromium-browser/chromedriver"
        browser = webdriver.Chrome(executable_path=PATH)
        url = "https:
        browser.get(url)
        detained = 0
        find_results(browser, file, pattern, 1, 59)
        find_results(browser, file, pattern, 301, 311)
        file.seek(0, 0)
        file.write(f"NO. OF STUDENTS DETAINED: {detained}\n")
        browser.quit()