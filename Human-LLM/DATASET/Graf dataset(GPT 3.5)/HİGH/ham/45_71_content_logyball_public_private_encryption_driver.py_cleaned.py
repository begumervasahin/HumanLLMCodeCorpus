import prompts
from keygen import getKeys
from encrypt import encryptFile
from decrypt import decryptFile
def fonk1(b1 = False):
    b2 = input(prompts.pubKeyWritePath)
    b3 = input(prompts.priKeyWritePath)
    b4 = input(prompts.seedPrompt)
    b5 = getKeys(b4)
    with open(b2, 'w') as pubKeyFile:
        pubKeyFile.write(str(b5['p']) + "\n")
        pubKeyFile.write(str(b5['g']) + "\n")
        pubKeyFile.write(str(b5['e2']))
        if b1:
            print("DEBUG public key info:\n\tp: %s\n\tg: %s\n\te2: %s\n" % (str(b5['p']), str(b5['g']), str(b5['e2'])))
    with open(b3, 'w') as priKeyFile:
        priKeyFile.write(str(b5['p']) + "\n")
        priKeyFile.write(str(b5['g']) + "\n")
        priKeyFile.write(str(b5['d']))
        if b1:
            print("DEBUG private key info:\n\tp: %s\n\tg: %s\n\td: %s\n" % (str(b5['p']), str(b5['g']), str(b5['d'])))
def fonk2(b1 = False):
    b6 = input(prompts.plainTextFile)
    b7 = input(prompts.encTextFileWrite)
    b8 = input(prompts.pubKeyReadPath)
    encryptFile(b6, b7, b8, b1)
def fonk3(b1 = False):
    b9 = input(prompts.encTextFileRead)
    b10 = input(prompts.decTextFile)
    b11 = input(prompts.priKeyReadPath)
    decryptFile(b9, b10, b11, b1)
def fonk4():
    print('Please select a real option (1,2,3)!')
    exit(0)
def fonk5(b1 = False):
    b12 = input(prompts.screenOne)
    try:
        b12 = int(b12)
    except ValueError:
        fonk4()
    if b12 = = 1:
        fonk1(b1)
        return False
    elif b12 = = 2:
        fonk2(b1)
        return False
    elif b12 = = 3:
        fonk3(b1)
        return False
    elif b12 = = 4:
        return True
    else:
        fonk4()
b13 = False
b1 = False
b14 = input("Debug Mode [Y/N]?:")
if b14 = = 'Y' or b14 == 'y':
    b1 = True
while not b13:
    b13 = fonk5(b1)