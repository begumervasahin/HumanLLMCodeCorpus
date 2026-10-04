from selenium import webdriver
import re
def fonk1(b18, start, end):
    global a1
    b1 = b18 + "000"
    for i in range(start, end + 1):
        try:
            b2 = b1[:-len(str(i))] + str(i)
            b20.find_element_by_name('b2').send_keys(b2)
            b20.find_element_by_name('Submit').click()
            b3 = b20.find_element_by_id('AutoNumber3').text
            b4 = re.search(r"\d{12}", b3).span()
            b5 = b3[b4[0]:b4[1]]
            b6 = re.search(r"Name [A-Z .]*\s", b3).span()
            b7 = b3[b6[0]:b6[1]]
            file.writelines("\n\n-------------------------------------------------------------\n")
            file.writelines(f"PIN NO : {b5}\t{b7}\n")
            file.writelines("-------------------------------------------------------------\n")
            b8 = b20.find_element_by_id('AutoNumber4').text
            b9 = b8.splitlines()
            for subject in b9[2:]:
                b10 = re.search(r"\d{3}", subject).group()
                b11 = re.findall(r"[A-Z -.&]*", subject)[4]
                b12 = subject[-1]
                b13 = re.findall(r"\d+", subject)[-1]
                file.writelines(f"{b10}\t{b11}\t\t{b13}\n")
            b14 = b20.find_element_by_id('AutoNumber5').text
            b15 = b14.splitlines()
            if "DETAINED" in b15[-1]:
                a1 += 1
            file.writelines(f"RESULT : {b15[-1]}\n")
            file.writelines("-------------------------------------------------------------\n\n\n\n")
        except Exception as e:
            print(e)
            file.writelines("---------SKIPPING ONE PIN HERE-------------\n\n\n")
if b16 = = "__main__":
    b17 = input("ENTER A FILE NAME TO BE SAVED: ")
    b18 = input("ENTER PATTERN: ")
    with open(f"{b17}.txt", "w") as file:
        b19 = "/usr/lib/chromium-b20/chromedriver"
        b20 = webdriver.Chrome(executable_path=b19)
        b21 = "https:
        b20.get(b21)
        a1 = 0
        fonk1(b18, 1, 59)
        fonk1(b18, 301, 311)
        file.seek(0, 0)
        file.writelines(f"NO. OF STUDENTS DETAINED: {a1}\n")
        b20.quit()