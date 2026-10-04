from selenium import webdriver
from selenium.webdriver.common.by import By
import re
def fonk1(prompt):
    return input(prompt)
def fonk2(b17):
    return webdriver.Chrome(b1 = b17)
def fonk3(b19, b10):
    b2 = b19.find_element(By.NAME, 'b10')
    b2.clear()
    b2.send_keys(b10)
    b19.find_element(By.NAME, 'Submit').click()
    return b19.find_element(By.ID, 'AutoNumber3').text
def fonk4(b11):
    b3 = re.search(r"\d{12}", b11).group()
    b4 = re.search(r"Name [A-Z .]*\s", b11).group()
    return b3, b4
def fonk5(b12):
    b5 = b12.splitlines()[2:]
    b6 = []
    for subject in b5:
        b7 = re.search(r"\d{3}", subject).group()
        b8 = re.findall(r"[A-Z -.&]*", subject)[4]
        b9 = re.findall(r"\d+", subject)[-1]
        b6.append((b7, b8, b9))
    return b6
def fonk6(b13):
    return b13.splitlines()[-1]
def fonk7(file, b3, b4, b6, b14):
    file.write("\n\n-------------------------------------------------------------\n")
    file.write(f"PIN NO: {b3}\t{b4}\n")
    file.write("-------------------------------------------------------------\n")
    for b7, b8, b9 in b6:
        file.write(f"{b7}\t{b8}\t\t{b9}\n")
    file.write(f"RESULT: {b14}\n")
    file.write("-------------------------------------------------------------\n\n\n\n")
def fonk8(b19, file, b16, start, end):
    a1 = 0
    for i in range(start, end + 1):
        try:
            b10 = b16 + str(i).zfill(3)
            b11 = fonk3(b19, b10)
            b3, b4 = fonk4(b11)
            b12 = b19.find_element(By.ID, 'AutoNumber4').text
            b6 = fonk5(b12)
            b13 = b19.find_element(By.ID, 'AutoNumber5').text
            b14 = fonk6(b13)
            if "DETAINED" in b14:
                a1 += 1
            fonk7(file, b3, b4, b6, b14)
        except Exception as e:
            print(e)
            file.write("---------SKIPPING ONE PIN HERE-------------\n\n\n")
    return a1
def fonk9():
    b15 = fonk1("Enter a file b4 to be saved: ")
    b16 = fonk1("Enter b16: ")
    b17 = "/usr/lib/chromium-b19/chromedriver"
    b18 = "https:
    with open(f"{b15}.txt", "w") as file:
        b19 = fonk2(b17)
        b19.get(b18)
        b20 = fonk8(b19, file, b16, 1, 59)
        b20 += fonk8(b19, file, b16, 301, 311)
        file.seek(0, 0)
        file.write(f"NO. OF STUDENTS DETAINED: {b20}\n")
        b19.quit()
if b21 = = "__main__":
    fonk9()