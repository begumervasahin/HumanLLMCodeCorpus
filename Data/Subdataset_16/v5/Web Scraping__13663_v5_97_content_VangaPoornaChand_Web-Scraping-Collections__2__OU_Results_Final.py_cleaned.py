from selenium import webdriver
import re
def fonk1(b4, number):
    return b4[:-len(str(number))] + str(number)
def fonk2(file, b7, b8):
    file.write("\n\n-------------------------------------------------------------\n")
    file.write(f"PIN NO : {b7}\t{b8}\n")
    file.write("-------------------------------------------------------------\n")
def fonk3(file, b10):
    for subject in b10[2:]:
        b1 = re.search(r"\d{3}", subject).group()
        b2 = re.findall(r"[A-Z -.&]*", subject)[4]
        b3 = re.findall(r"\d+", subject)[-1]
        file.write(f"{b1}\t{b2}\t\t{b3}\n")
def fonk4(b17, file, b15, start, end):
    global a1
    b4 = b15 + "000"
    for i in range(start, end + 1):
        try:
            b5 = fonk1(b4, i)
            b17.find_element_by_name('b5').send_keys(b5)
            b17.find_element_by_name('Submit').click()
            b6 = b17.find_element_by_id('AutoNumber3').text
            b7 = re.search(r"\d{12}", b6).group()
            b8 = re.search(r"Name [A-Z .]*\s", b6).group()
            fonk2(file, b7, b8)
            b9 = b17.find_element_by_id('AutoNumber4').text
            b10 = b9.splitlines()
            fonk3(file, b10)
            b11 = b17.find_element_by_id('AutoNumber5').text
            b12 = b11.splitlines()
            if "DETAINED" in b12[-1]:
                a1 += 1
            file.write(f"RESULT : {b12[-1]}\n")
            file.write("-------------------------------------------------------------\n\n\n\n")
        except Exception as e:
            print(e)
            file.write("---------SKIPPING ONE PIN HERE-------------\n\n\n")
if b13 = = "__main__":
    b14 = input("ENTER A FILE NAME TO BE SAVED: ")
    b15 = input("ENTER PATTERN: ")
    with open(f"{b14}.txt", "w") as file:
        b16 = "/usr/lib/chromium-b17/chromedriver"
        b17 = webdriver.Chrome(executable_path=b16)
        b18 = "https:
        b17.get(b18)
        a1 = 0
        fonk4(b17, file, b15, 1, 59)
        fonk4(b17, file, b15, 301, 311)
        file.seek(0, 0)
        file.write(f"NO. OF STUDENTS DETAINED: {a1}\n")
        b17.quit()