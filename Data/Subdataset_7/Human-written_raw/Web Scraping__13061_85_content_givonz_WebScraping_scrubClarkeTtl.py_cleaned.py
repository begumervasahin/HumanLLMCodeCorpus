from bs4 import BeautifulSoup
from urllib.request import urlopen
def fonk1(b23,b20,b21,b22):
    b1 = urlopen(b23).read()
    b2 = BeautifulSoup(b1,"html.parser")
    b3 = b2.find_all("a")
    a1 = 0
    for link in b3:
         a1+=1
    a1-=1
    a2 = 0
    for link in b3:
        if len(link.get("href"))==5:
            a2+=1
            continue
        if  link.get("href")[-9:]=="index.htm":
            b4 = str(b3[a2])
            for b12 in range(len(b4)):
                 if b4[b12:b12+6]==">H.I.<":
                      return
            a2+=1
            continue
        a2+=1
        if a2 = =a1:
            return
        b5 = "http:
        b6 = urlopen(b5).read()
        b7 = BeautifulSoup(b6,"html.parser")
        b8 = b7.find_all("p")
        for line in range(len(b8)):
            b9 = str(b8[2])
            a3 = 0
            a4 = 0
            a5 = 0
            for pos in range(len(b9)-1):
                 if b9[pos:pos+1]==">":
                     a4 = pos+1
                 if b9[pos:pos+1]=="<":
                     a3+=1
                     if a3 = =2:
                         a5 = pos-1
            print(b9[a4:a5])
            b20.write(b9[a4:a5]+"\n")
            b10 = str(b8[3])
            a3 = 0
            a4 = 0
            a5 = 0
            for pos in range(len(b10)-1):
                 if b10[pos:pos+1]==">":
                     a4 = pos+1
                 if b10[pos:pos+1]=="<":
                     a3+=1
                     if a3 = =2:
                         a5 = pos-1
            b11 = len(b10)
            for b12 in range(b11):
                 if b12 = =b11:
                      break
                 if b10[b12:b12+8]=="        ":
                      b10 = b10[:b12-1]+b10[b12+10:]
            a4 = 0
            a5 = 0
            for pos in range(len(b10)):
                  if b10[pos:pos+1]=="<":
                      a4 = pos
                  if b10[pos:pos+1]==">":
                      a5 = pos
                      break
            b10 = b10[1:1]+b10[pos+1:]
            for pos in range(len(b10)):
                  if b10[pos:pos+1]=="(":
                      b10 = b10[:pos]+b10[pos+1:]
                      continue
                  if b10[pos:pos+1]==")":
                      b10 = b10[:pos]+b10[pos+1:]
                      break
            b13 = fonk3(b10)
            b21.write(b13+"\n")
            b14 = fonk2(b7)
            b22.write(b14+"\n")
            break
def fonk2(soup3):
  b15 = str(soup3)
  a6 = 0
  a7 = 0
  a8 = 0
  for pos in range(len(b15)):
      if b15[pos:pos+8]=="Clinical":
          a6 = 1
      if a6 = =1 and b15[pos:pos+4]=="</b>":
          a7 = pos+4
      if a7>0 and b15[pos:pos+13]=="</blockquote>":
          a8 = pos
          break
  b16 = b15[a7:a8]
  b11 = len(b16)
  for b12 in range(b11):
      if b12 = =b11:
          break
      if b16[b12:b12+3]=="<i>":
          b16 = b16[:b12]+" 2"+b16[b12+3:]
      if b16[b12:b12+22]=='<font b17 = "
          b16 = b16[:b12]+b16[b12+22:]
      if b16[b12:b12+7]=="</font>":
          b16 = b16[:b12]+b16[b12+7:]
  for b12 in range(b11):
      if b12 = =b11:
          break
      if b16[b12:b12+4]=="</i>":
          b16 = b16[:b12]+b16[b12+4:]
  for b12 in range(b11):
      if b12 = =b11:
          break
      if b16[b12:b12+1]=="\n":
          b16 = b16[:b12]+b16[b12+1:]
  for b12 in range(b11):
      if b12 = =b11:
          break
      if b16[b12:b12+8]=="        ":
          b16 = b16[:b12]+b16[b12+6:]
          b16 = b16[:b12]+b16[b12+1:]
  b18 = fonk3(b16)
  return(b18)
def fonk3(b18):
  b19 = '"'
  b12 = 0
  a2 = 0
  while(b12 < len(b18)):
      if b18[b12:b12+1] == '.':
           if b18[b12-1:b12]=='N' or b18[b12-1:b12]=='O':
                b12+=1
                continue
           b19 = b19+b18[a2:b12]+'","'
           b3 = 1
           while(b18[b12+b3:b12+b3+1]==' '):
               b3+=1
               continue
           a2 = b12+b3
      b12+=1
  b19 = b19[:len(b19)-2]
  b12 = 0
  while(b12 < len(b19)):
      if b19[b12:b12+1] == '"' and (b19[b12+1:b12+2]>="A" and b19[b12+1:b12+2]<="Z"):
           b19 = b19[:b12+1]+'1'+b19[b12+1:]
      b12+=1
  b12 = 0
  while(b12 < len(b19)):
      if b19[b12:b12+1] == '"':
            if b19[b12+1:b12+2]=="1":
                 b19 = b19[:b12+2]+'","'+b19[b12+2:]
                 b12 = b12+3
            if b19[b12+1:b12+2]=="2":
                 b19 = b19[:b12+2]+'","'+b19[b12+2:]
                 b12 = b12+3
      b12+=1
  return(b19)
def fonk4():
    b20 = open("h-remedies","w")
    b21 = open("commonRemedyNames","w")
    b22 = open("remedy-symptoms","w")
    for b12 in range(26):
        b23 = "http:
        fonk1(b23,b20,b21,b22)
    b20.close()
    b21.close()
    b22.close()
fonk4()