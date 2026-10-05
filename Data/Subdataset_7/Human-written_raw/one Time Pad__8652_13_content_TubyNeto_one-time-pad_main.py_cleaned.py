import string
import random
def fonk1(b6, letterKey):
  b1 = 'abcdefghijklmnopqrstuvwxyz'
  b2 = b1.index(b6) + 1
  b3 = b1.index(letterKey) + 1
  b4 = (b2 + b3) % 26
  b5 = b1[b4]
  return b5
def fonk2(b5, letterKey):
  b1 = 'abcdefghijklmnopqrstuvwxyz'
  b4 = b1.index(b5) + 1
  b3 = b1.index(letterKey) + 1
  b2 = b4 - b3
  b6 = b1[b2]
  return b6
def fonk3(b8, b11):
  b7 = ''
  for i in range(len(b8)):
    b7 += fonk2(b8[i], b11[i])
  return b7
def fonk4(b7, b11):
  b8 = ''
  for i in range(len(b7)):
    b8 += fonk1(b7[i], b11[i])
  return b8
def fonk5(keyLength):
    b9 = string.ascii_lowercase
    return ''.join(random.choice(b9) for i in range(keyLength))
while (True):
  print("Menu:")
  print("1 - Encrypt")
  print("2 - Decrypt")
  print("3 - Quit")
  b10 = input()
  if (b10 = = '1'):
    print("Type the Plain Text:")
    b7 = input()
    b11 = fonk5(len(b7))
    print('Cypher Text:', fonk4(b7, b11))
  elif (b10 = = '2'):
    print("Type the Cypher Text:")
    b8 = input()
    b11 = fonk5(len(b8))
    print('Plain Text:', fonk3(b8, b11))
  elif (b10 = = '3'):
    break
  else:
    print("Only 1/2/3 options avaible")