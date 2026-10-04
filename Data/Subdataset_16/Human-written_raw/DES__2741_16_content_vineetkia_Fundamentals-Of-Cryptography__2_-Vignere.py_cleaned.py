def fonk1(PlainText,KEY):
    b1 = ''
    for i in range(len(PlainText)):
        b2 = i%len(KEY)
        if(PlainText[i].isupper()):
            b1+=chr(((ord(PlainText[i])+ord(KEY[b2]))%26+66))
        else:
            b1+=chr(((ord(PlainText[i])+ord(KEY[b2]))%26+98))
    return b1
print(fonk1("VINeeT","WOW"))