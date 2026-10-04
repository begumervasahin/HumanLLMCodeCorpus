def fonk1( b2 ):
    b1 = ['+', '-', '*', '/', '%', '(', ')', '=', '<','>','!','?',':',';', ',']
    b2 = b2 + ";"
    a1 = 0
    while (b2[a1] != ";"):
        if (b2[a1] == ' '):
            a1+=1
        elif(b2[a1].isalpha()):
            b3 = a1
            while(b2[a1] not in b1 and b2[a1] != ' '):
                a1+=1
            yield b2[b3:a1]
        elif (b2[a1].isdigit()):
            b3 = a1
            while(b2[a1].isdigit()):
                a1+=1
            yield b2[b3:(a1)]
        elif ((b2[a1] == '=' or b2[a1] == '!' or b2[a1] == '<' or b2[a1] == '>') and b2[a1+1]=='='):
            yield b2[a1]+b2[a1+1]
            a1+=2
        else:
            yield b2[a1]
            a1+=1
    yield ";"