from selenium import webdriver
import re
b1 = input("ENTER A FILE NAME TO BE SAVED : ")
b2 = input("ENTER PATTERN : ")
b3 = open(f"{b1}.txt","w")
b4 = "/usr/lib/chromium-b5/chromedriver"
b5 = webdriver.Chrome(executable_path=b4)
b6 = "https:
b5.get(b6)
a1 = 0
def fonk1(b2,start,end):
	global a1
	b7 = b2+"000"
	for i in range(start,end+1):
		try:
			if len(str(abs(i)))==1: b7 = b7[:-1]+str(i)
			if len(str(abs(i)))==2: b7 = b7[:-2]+str(i)
			if len(str(abs(i)))==3: b7 = b7[:-3]+str(i)
			b5.find_element_by_name('b7').send_keys(b7)
			b5.find_element_by_name('Submit').click()
			b8 = b5.find_element_by_id('AutoNumber3').text
			b9 = re.search("\d{12}",b8).span()
			b10 = b8[b9[0]:b9[1]]
			b11 = re.search("Name [A-Z .]*\s",b8).span()
			b3.writelines("\n\n-------------------------------------------------------------\n")
			b3.writelines("PIN NO : "+b10+"\t"+str(b8[b11[0]:b11[-1]])+"\n")
			b3.writelines("-------------------------------------------------------------\n")
			b12 = b5.find_element_by_id('AutoNumber4').text
			b13 = b12.splitlines()
			for subject in b13[2:]:
				b14 = re.search("\d{3}",subject).span()
				b15 = subject[b14[0]:b14[1]]
				b16 = re.findall("[A-Z -.&]*",subject)[4]
				b17 = subject[-1]
				b18 = re.findall("\d+",subject)[-1]
				b19 = "\t\t"
				b3.writelines(str(b15)+"\t"+str(b16)+b19+str(b18)+"\n")
			b20 = b5.find_element_by_id('AutoNumber5').text
			b21 = b20.splitlines()
			if "DETAINED" in str(b21[-1]):
				a1 += 1
			b3.writelines(str(["RESULT : ",str(b21[-1])])+"\n")
			b3.writelines("-------------------------------------------------------------\n\n\n\n")
		except Exception as e:
			print(e)
			b3.writelines("---------SKIPING ONE PIN HERE-------------\n\n\n")
fonk1(b2,1,59)
fonk1(b2,301,311)
b3.seek(0, 0)
b3.writelines("NO. OF STUDENTS DETAINED: "+str(a1)+"\n")
b3.close()