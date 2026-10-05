import prompts
from keygen import getKeys
from encrypt import encryptFile
from decrypt import decryptFile
def fonk1(b1 = False):
    b2 = input(prompts.pubKeyWritePath)
    b3 = input(prompts.priKeyWritePath)
    b4 = input(prompts.seedPrompt)
    b5 = getKeys(b4)
    with open(b2, 'w') as pub_key_file:
        pub_key_file.write(f"{b5['p']}\n")
        pub_key_file.write(f"{b5['g']}\n")
        pub_key_file.write(f"{b5['e2']}")
        if b1:
            print(f"DEBUG public key info:\n\tp: {b5['p']}\n\tg: {b5['g']}\n\te2: {b5['e2']}\n")
    with open(b3, 'w') as pri_key_file:
        pri_key_file.write(f"{b5['p']}\n")
        pri_key_file.write(f"{b5['g']}\n")
        pri_key_file.write(f"{b5['d']}")
        if b1:
            print(f"DEBUG private key info:\n\tp: {b5['p']}\n\tg: {b5['g']}\n\td: {b5['d']}\n")
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
    print('Please select a real option (1, 2, 3)!')
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
if b14.upper() == 'Y':
    b1 = True
while not b13:
    b13 = fonk5(b1)