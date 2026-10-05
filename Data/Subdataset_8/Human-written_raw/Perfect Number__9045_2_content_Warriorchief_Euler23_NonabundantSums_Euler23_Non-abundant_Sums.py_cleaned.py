
import math;
def find_sum_prop_factors(x):
    factors=[];
    i=1;
    while i<math.ceil((x/2)+1):
        if x%i==0:
            factors.append(i);
        i+=1;
    tot=0;
    for f in factors:
        tot+=f
    return tot;
abundants=[];
k=11;
while k<28123:
    if k%1000==0:
        print("trying",k,"...");
    if find_sum_prop_factors(k)>k:
        abundants.append(k);
    k+=1;
sum2abundants=[];
p=0;
while p<len(abundants):
    if p%100==0:
        print("passing through p being",p,"out of 6965");
    q=0;
    while q<len(abundants):
        if abundants[p]+abundants[q]<28123:
            sum2abundants.append(abundants[p]+abundants[q]);
        q+=1;
    p+=1;
sum2nodupes=set(sum2abundants);
print("sum2nodupes has length",len(sum2nodupes));
output=0;
z=0;
while z<28123:
    if z%100==0:
        print("passing through z being",z,"out of 28123");
    if z not in sum2nodupes:
        output+=z;
    z+=1;
print("the answer to this question should be",output);