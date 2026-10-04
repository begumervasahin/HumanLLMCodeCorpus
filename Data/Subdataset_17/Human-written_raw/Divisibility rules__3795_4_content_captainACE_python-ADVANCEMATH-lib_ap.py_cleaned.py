def ap():
    print ("this is an ARITHMETIC PROGRESSION module")
    print("one can find the last  number  in a sequence or list of numbers")
    print("for determing last number one has to enter the first terms of the A.P and the common difference")
    a=int(input("first term of the number sequence: "))
    d=int(input("the common difference in the number sequence: "))
    n = int (input("number of terms: "))
    print (a+(n-1)*d)
ap()