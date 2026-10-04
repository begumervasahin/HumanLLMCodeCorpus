from selenium import webdriver
from selenium.webdriver.common.by import By
import re
b1 = input("Enter a file name to be saved: ")
b2 = input("Enter b2: ")
with open(f"{b1}.txt", "w") as file:
    b3 = "/usr/lib/chromium-b4/chromedriver"
    b4 = webdriver.Chrome(executable_path=b3)
    b5 = "https:
    b4.get(b5)
    a1 = 0
    def fonk1(b2, start, end):
        global a1
        for i in range(start, end + 1):
            try:
                b6 = b2 + str(i).zfill(3)
                b7 = b4.find_element(By.NAME, 'b6')
                b7.clear()
                b7.send_keys(b6)
                b4.find_element(By.NAME, 'Submit').click()
                b8 = b4.find_element(By.ID, 'AutoNumber3').text
                b9 = re.search(r"\d{12}", b8).span()
                b10 = b8[b9[0]:b9[1]]
                b11 = re.search(r"Name [A-Z .]*\s", b8).span()
                file.write("\n\n-------------------------------------------------------------\n")
                file.write(f"PIN NO: {b10}\t{b8[b11[0]:b11[-1]]}\n")
                file.write("-------------------------------------------------------------\n")
                b12 = b4.find_element(By.ID, 'AutoNumber4').text
                b13 = b12.splitlines()
                for subject in b13[2:]:
                    b14 = re.search(r"\d{3}", subject).span()
                    b15 = subject[b14[0]:b14[1]]
                    b16 = re.findall(r"[A-Z -.&]*", subject)[4]
                    b17 = subject[-1]
                    b18 = re.findall(r"\d+", subject)[-1]
                    file.write(f"{b15}\t{b16}\t\t{b18}\n")
                b19 = b4.find_element(By.ID, 'AutoNumber5').text
                b20 = b19.splitlines()
                if "DETAINED" in b20[-1]:
                    a1 += 1
                file.write(f"RESULT: {b20[-1]}\n")
                file.write("-------------------------------------------------------------\n\n\n\n")
            except Exception as e:
                print(e)
                file.write("---------SKIPPING ONE PIN HERE-------------\n\n\n")
    fonk1(b2, 1, 59)
    fonk1(b2, 301, 311)
    file.seek(0, 0)
    file.write(f"NO. OF STUDENTS DETAINED: {a1}\n")
b4.quit()