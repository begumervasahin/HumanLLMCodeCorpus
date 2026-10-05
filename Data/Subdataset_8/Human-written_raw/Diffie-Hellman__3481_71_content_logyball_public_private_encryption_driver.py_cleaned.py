import prompts
from keygen import getKeys
from encrypt import encryptFile
from decrypt import decryptFile
def keyGeneration(debug=False):
    pubPath = input(prompts.pubKeyWritePath)
    priPath = input(prompts.priKeyWritePath)
    seed = input(prompts.seedPrompt)
    keyDict = getKeys(seed)
    with open(pubPath, 'w') as pubKeyFile:
        pubKeyFile.write(str(keyDict['p']) + "\n")
        pubKeyFile.write(str(keyDict['g']) + "\n")
        pubKeyFile.write(str(keyDict['e2']))
        if debug:
            print("DEBUG public key info:\n\tp: %s\n\tg: %s\n\te2: %s\n" % (str(keyDict['p']), str(keyDict['g']), str(keyDict['e2'])))
    with open(priPath, 'w') as priKeyFile:
        priKeyFile.write(str(keyDict['p']) + "\n")
        priKeyFile.write(str(keyDict['g']) + "\n")
        priKeyFile.write(str(keyDict['d']))
        if debug:
            print("DEBUG private key info:\n\tp: %s\n\tg: %s\n\td: %s\n" % (str(keyDict['p']), str(keyDict['g']), str(keyDict['d'])))
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
if userD == 'Y' or userD == 'y':
    debug = True
while not done:
    done = collectInput(debug)