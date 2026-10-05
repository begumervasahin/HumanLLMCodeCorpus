def new_split_iter( expr ):
    operators = ['+', '-', '*', '/', '%', '(', ')', '=', '<','>','!','?',':',';', ',']
    expr = expr + ";"
    pos = 0
    while (expr[pos] != ";"):
        if (expr[pos] == ' '):
            pos+=1
        elif(expr[pos].isalpha()):
            temp = pos
            while(expr[pos] not in operators and expr[pos] != ' '):
                pos+=1
            yield expr[temp:pos]
        elif (expr[pos].isdigit()):
            temp = pos
            while(expr[pos].isdigit()):
                pos+=1
            yield expr[temp:(pos)]
        elif ((expr[pos] == '=' or expr[pos] == '!' or expr[pos] == '<' or expr[pos] == '>') and expr[pos+1]=='='):
            yield expr[pos]+expr[pos+1]
            pos+=2
        else:
            yield expr[pos]
            pos+=1
    yield ";"