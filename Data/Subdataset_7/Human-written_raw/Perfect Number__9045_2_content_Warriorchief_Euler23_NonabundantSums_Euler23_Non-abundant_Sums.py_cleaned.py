
import math;
def fonk1(x):
    b1 = [];
    b2 = 1;
    while b2<math.ceil((x/2)+1):
        if x%b2 = =0:
            b1.append(b2);
        b2+=1;
    b3 = 0;
    for f in b1:
        b3+=f
    return b3;
b4 = [];
b5 = 11;
while b5<28123:
    if b5%b6 = =0:
        print("trying",b5,"...");
    if fonk1(b5)>b5:
        b4.append(b5);
    b5+=1;
b7 = [];
b8 = 0;
while b8<len(b4):
    if b8%b9 = =0:
        print("passing through b8 being",b8,"out of 6965");
    b10 = 0;
    while b10<len(b4):
        if b4[b8]+b4[b10]<28123:
            b7.append(b4[b8]+b4[b10]);
        b10+=1;
    b8+=1;
b11 = set(b7);
print("b11 has length",len(b11));
b12 = 0;
b13 = 0;
while b13<28123:
    if b13%b9 = =0:
        print("passing through b13 being",b13,"out of 28123");
    if b13 not in b11:
        b12+=b13;
    b13+=1;
print("the answer to this question should be",b12);