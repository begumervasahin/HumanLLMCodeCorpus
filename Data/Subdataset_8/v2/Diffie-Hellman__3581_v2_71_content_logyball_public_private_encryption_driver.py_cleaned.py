import prompts
from keygen import getKeys
from encrypt import encryptFile
from decrypt import decryptFile
def keyGeneration(debug=False):
    pubPath = input(prompts.pubKeyWritePath)
    priPath = input(prompts.priKeyWritePath)
    seed = input(prompts.seedPrompt)
    keyDict = getKeys(seed)
    writeKeysToFile(pubPath, priPath, keyDict, debug)
def writeKeysToFile(pubPath, priPath, keyDict, debug=False):
    with open(pubPath, 'w') as pubKeyFile:
        pubKeyFile.write(f"{keyDict['p']}\n")
        pubKeyFile.write(f"{keyDict['g']}\n")
        pubKeyFile.write(f"{keyDict['e2']}")
        if debug:
            print(f"DEBUG public key info:\n\tp: {keyDict['p']}\n\tg: {keyDict['g']}\n\te2: {keyDict['e2']}\n")
    with open(priPath, 'w') as priKeyFile:
        priKeyFile.write(f"{keyDict['p']}\n")
        priKeyFile.write(f"{keyDict['g']}\n")
        priKeyFile.write(f"{keyDict['d']}")
        if debug:
            print(f"DEBUG private key info:\n\tp: {keyDict['p']}\n\tg: {keyDict['g']}\n\td: {keyDict['d']}\n")
def fileEncrypt(debug=False):
    plainPath = input(prompts.plainTextFile)
    encWritePath = input(prompts.encTextFileWrite)
    pubKeyPath = input(prompts.pubKeyReadPath)
    encryptFile(plainPath, encWritePath, pubKeyPath, debug)
def fileDecrypt(debug=False):
    encryptedPath = input(prompts.encTextFileRead)
    decWritePath = input(prompts.decTextFile)
    priKeyPath = input(prompts.priKeyReadPath)
    decryptFile(encryptedPath, decWritePath, priKeyPath, debug)
def quitWithError():
    print('Please select a real option (1,2,3)!')
    exit(0)
def collectInput(debug=False):
    choice = input(prompts.screenOne)
    try:
        choice = int(choice)
    except ValueError:
        quitWithError()
    if choice == 1:
        keyGeneration(debug)
        return False
    elif choice == 2:
        fileEncrypt(debug)
        return False
    elif choice == 3:
        fileDecrypt(debug)
        return False
    elif choice == 4:
        return True
    else:
        quitWithError()
done = False
debug = False
userD = input("Debug Mode [Y/N]?:")
if userD.upper() == 'Y':
    debug = True
while not done:
    done = collectInput(debug)