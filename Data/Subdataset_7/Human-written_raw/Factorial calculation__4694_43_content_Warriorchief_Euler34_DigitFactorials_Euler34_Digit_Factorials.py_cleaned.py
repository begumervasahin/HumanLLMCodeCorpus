
def fonk1(x):
    b1 = x;
    b2 = 1;
    while b1>1:
        b2*=b1
        b1-=1;
    return b2;
def fonk2(num):
    b3 = str(num);
    b4 = [];
    b1 = 0;
    while b1<len(b3):
        b4.append(b3[b1]);
        b1+=1;
    return list(b4);
def fonk3(num):
    b4 = fonk2(num);
    b5 = 0;
    b1 = 0;
    while b1<len(b4):
        b5+=fonk1(int(b4[b1]));
        b1+=1;
    if b5 = =num:
        return True;
    return False;
def fonk4(max):
    b1 = 3;
    b6 = [];
    while b1<max:
        if b1%b7 = =0:
            print("trying b1 as",b1,"so there'b3 another hundred thousand tested");
        if fonk3(b1):
            b6.append(b1);
        b1+=1;
    print("special numbers are",b6,"so there are",len(b6),"that are less than",max);
    return b6;
fonk4(100000000)