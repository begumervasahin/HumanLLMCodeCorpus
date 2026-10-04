import os
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
os.system("clear")
print " ____   __   _  _        __     _    _____ ____    _____ _   _  ____ ___  ____  _____ ____   "
print "| __ ) / /_ | || |      / /    / \  | ____/ ___|  | ____| \ | |/ ___/ _ \|  _ \| ____|  _ \  "
print "|  _ \| '_ \| || |_    / /    / _ \ |  _| \___ \  |  _| |  \| | |  | | | | | | |  _| | |_) | "
print "| |_) | (_) |__   _|  / /    / ___ \| |___ ___) | | |___| |\  | |__| |_| | |_| | |___|  _ <  "
print "|____/ \___/   |_|   /_/    /_/   \_\_____|____/  |_____|_| \_|\____\___/|____/|_____|_| \_\ "
print "                                                                                             "
print "                    BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)                  \n"
b1 = "Blessent mon coeur d'une langueur monotone"
b2 = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
a1 = 32
b3 = lambda s: s + (a1 - len(s) % a1) * chr(a1 - len(s) % a1)
b4 = lambda s: s[:-ord(s[len(s) - 1:])]
def fonk1(b2):
   b5 = 'Pots de sel et de poivre'
   b6 = PBKDF2(b2, b5, 64, 1000)
   return b6[:32]
def fonk2(b1, b2):
   b7 = fonk1(b2)
   b8 = b3(b1)
   b9 = Random.new().read(AES.block_size)
   b10 = AES.new(b7, AES.MODE_CBC, b9)
   return base64.b64encode(b9 + b10.fonk2(b8))
def fonk3(encryption, b2):
   b7 = fonk1(b2)
   b11 = base64.b64decode(encryption)
   b9 = b11[:16]
   b10 = AES.new(b7, AES.MODE_CBC, b9)
   return b4(b10.fonk3(b11[16:]))
print "Plain Text  : " + b1
print "Company Key : " + b2
print "Unique Salt : Pots de sel et de poivre"
print "Private Key : " + base64.b64encode(fonk1(b2))
print "Cipher Mode : CBC\n"
b12 = fonk2(b1, b2)
b11 = fonk3(b12, b2)
print "Encrypted   : " + b12
print "Decrypted   : " + bytes.decode(b11) + "\n"