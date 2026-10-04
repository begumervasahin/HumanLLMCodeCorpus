import sys
inp = sys.argv[:]
hel=
if len(inp)<=4 :
    print hel
    exit()
min = int(inp[1])
max = int(inp[2])
p = str(inp[4])
listn = str(inp[3])
ff =open('letters.txt','r')
letters = ff.read().split('\n')[0]
ff.close()
f = open(listn,'w')
def creat(l,pas) :
    if len(pas) ==(l):
        for lett in letters:
            npas = pas + str(lett)+'\n'
            if p=='y' or p=='Y':
                print npas
            f.write(npas)
    elif len(pas)<l:
        for lett in letters:
            npas = pas + str(lett)
            creat(l,npas)
hello =
print hello
for i in range(min-1,max) :
    creat(i,'')
f.close()
print 'Password List Created Succesfully ..'