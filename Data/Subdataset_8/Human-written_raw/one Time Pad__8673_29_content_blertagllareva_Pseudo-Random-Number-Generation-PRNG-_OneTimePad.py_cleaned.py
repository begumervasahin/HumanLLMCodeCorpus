def charToNum(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num = 1
    for letter in alphabet:
        if letter == char:
            break
        else:
            num+=1
    return num
def numToChar(num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[num+1]
def encodeChar(pText, key):
    cNum = ( charToNum(pText) + charToNum(key) ) % 26
    cText = numToChar(cNum)
    return cText
def decodeChar(cText, key):
    pNum = charToNum(cText) - charToNum(key)
    pText= numToChar(pNum)
    return pText
def encode(pText, key):
    cText= ""
    for i in range(0, len(pText)):
        cText += encodeChar(pText[i], key[i])
    return cText
def decode(cText, key):
    pText=""
    for i in range(0, len(cText)):
        pText += decodeChar(cText[i], key[i])
    return pText
def main():
    cont=True
    choice=""
    print("OneTimePad Program.  ÃelÃ«si duhet tÃ« jetÃ« mÃ« i vogÃ«l ose i barabartÃ« me plain-tekstin.  Plain-teksti nuk duhet tÃ« ketÃ« numra.")
    print("\nMundÃ«sitÃ«:\n1: Enkodimi\n2: Dekodimi\n3: NdÃ«rprerje")
    while cont == True:
        choice = input(">>> ")
        if choice == "1":
            print("Cipher-teksti: " + encode(input("Plain-teksti: "), input("ÃelÃ«si: ")))
        elif choice == "2":
            print("Plain-teksti: " + decode(input("Cipher-teksti: "), input("ÃelÃ«si: ")))
        elif choice == "3":
            cont = False
        else:
            print("Ju lutem zgjedhni 1, 2, or 3")
main()