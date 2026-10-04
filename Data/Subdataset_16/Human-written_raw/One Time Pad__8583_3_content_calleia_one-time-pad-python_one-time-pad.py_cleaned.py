import random
import sys
def fonk1(b1):
  b1 = ord(b1)
  b2 = []
  b2.append(random.randint(0, 255))
  b2.append(b1 ^ b2[0])
  return b2
def fonk2(byte0,b8):
  b2 = []
  b2.append(ord(byte0))
  b2.append(ord(b8))
  b3 = b2[0] ^ b2[1]
  return b3
def fonk3(input1, b7, output2):
  b4 = open(b7, 'wb')
  b5 = open(output2, 'wb')
  with open(input1, "rb") as f:
    b1 = f.read(1)
    while b1:
      b3 = fonk1(b1)
      b4.write(b3[0].to_bytes(1,b6 = "big",signed=False))
      b5.write(b3[1].to_bytes(1,b6 = "big",signed=False))
      b1 = f.read(1)
def fonk4(input1, input2, b7):
  b7 = open(b7, 'wb')
  with open(input1, "rb") as f1:
    with open(input2, "rb") as f2:
      b8 = f1.read(1)
      b9 = f2.read(1)
      while b8:
        b7.write(fonk2(b8, b9).to_bytes(1,b6 = "big",signed=False))
        b8 = f1.read(1)
        b9 = f2.read(1)
print("Starting script...")
if len(sys.argv) == 2:
  fonk3(sys.argv[1], sys.argv[1] + ".0", sys.argv[1] + ".1")
elif len(sys.argv) == 3:
  fonk4(sys.argv[1], sys.argv[2], sys.argv[1][:-2])
else:
  print("Argument parsing error.")
print("Script finished.")