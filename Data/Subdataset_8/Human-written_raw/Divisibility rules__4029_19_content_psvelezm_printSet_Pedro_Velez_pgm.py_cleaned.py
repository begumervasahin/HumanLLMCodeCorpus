def printStringProperties(S):
    charList=list(S)
    evenCharList=[char for char in charList if (charList.index(char)%2==1)]
    evenString="".join(evenCharList)
    print "The input string is: "+S
    print "The characters that have even indexes are: "+(evenString)
    print "The string in reverse order is: "+S[::-1]
    if(S==S[::-1]):
        print "The string is a palindrome: True"
    else:
        print "The string is a palindrome: False"
printStringProperties("11411")
def printSet(L,H):
    numList=[]
    for i in range (H-L-1):
        n=L+i
        if ((n%7==0) and (n%5!=0)):
            numList.append(n)
    M=set(numList)
    print M
printSet(11,21)