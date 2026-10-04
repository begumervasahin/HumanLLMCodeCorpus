
def factorial(x):
    i=x;
    fac=1;
    while i>1:
        fac*=i
        i-=1;
    return fac;
def separate_into_chars(num):
    s=str(num);
    chars=[];
    i=0;
    while i<len(s):
        chars.append(s[i]);
        i+=1;
    return list(chars);
def is_spec_num(num):
    chars=separate_into_chars(num);
    tot=0;
    i=0;
    while i<len(chars):
        tot+=factorial(int(chars[i]));
        i+=1;
    if tot==num:
        return True;
    return False;
def find_all_spec_nums(max):
    i=3;
    spec=[];
    while i<max:
        if i%100000==0:
            print("trying i as",i,"so there's another hundred thousand tested");
        if is_spec_num(i):
            spec.append(i);
        i+=1;
    print("special numbers are",spec,"so there are",len(spec),"that are less than",max);
    return spec;
find_all_spec_nums(100000000)