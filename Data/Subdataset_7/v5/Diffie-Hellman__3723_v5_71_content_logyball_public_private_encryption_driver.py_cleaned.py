import prompts
from keygen import getKeys
from encrypt import encryptFile
from decrypt import decryptFile
def fonk1(b1 = False):
    b2 = input(prompts.pubKeyWritePath)
    b3 = input(prompts.priKeyWritePath)
    b4 = input(prompts.seedPrompt)
    b5 = getKeys(b4)
    fonk2(b2, b5['p'], b5['g'], b5['e2'], b1)
    fonk2(b3, b5['p'], b5['g'], b5['d'], b1)
def fonk2(file_path, p, g, key, b1 = False):
    with open(file_path, 'w') as key_file:
        key_file.write(f"{p}\n")
        key_file.write(f"{g}\n")
        key_file.write(f"{key}")
        if b1:
            print(f"DEBUG key info:\n\tp: {p}\n\tg: {g}\n\tkey: {key}\n")
def fonk3(b1 = False):
    b6 = input(prompts.plainTextFile)
    b7 = input(prompts.encTextFileWrite)
    b8 = input(prompts.pubKeyReadPath)
    encryptFile(b6, b7, b8, b1)
def fonk4(b1 = False):
    b9 = input(prompts.encTextFileRead)
    b10 = input(prompts.decTextFile)
    b11 = input(prompts.priKeyReadPath)
    decryptFile(b9, b10, b11, b1)
def fonk5():
    print('Please select a valid option (1, 2, 3)!')
    exit(0)
def fonk6(b1 = False):
    b12 = input(prompts.screenOne)
    try:
        b12 = int(b12)
    except ValueError:
        fonk5()
    if b12 = = 1:
        fonk1(b1)
        return False
    elif b12 = = 2:
        fonk3(b1)
        return False
    elif b12 = = 3:
        fonk4(b1)
        return False
    elif b12 = = 4:
        return True
    else:
        fonk5()
b13 = False
b1 = input("Debug Mode [Y/N]?:").upper() == 'Y'
while not b13:
    b13 = fonk6(b1)