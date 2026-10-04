import math
import re
import numpy as np
import pandas as pd
print ' '
print ' '
print ' '
print '          Welcome to ConverS.py'
print '           --by Niam Moltta--'
print '                ~~/\
print ' '
print ' '
print ' '
print 'Application: STRINGS TO NUMBERS TRANSFORMATION.\n\nINSTRUCTIONS:\n\n-You need to modify the code itself in order to convert your own b3.\n\n'
b1 = raw_input('File name: ')
b2 = str(b1)
if b1 = = '':
    print ' '
    print 'Arrivederci!'
    print ' '
    exit()
b3 = pd.read_csv(b1)
print ' '
b4 = pd.DataFrame(b3)
b5 = b4.b6
b6 = np.asarray(b5)
print ' '
print 'Columns in', re.findall('(.+?).csv', b2), 'are:\n'
print b6
print ' '
b7 = raw_input('Enter b8 header:\n\n')
b8 = str(b7)
if (b8 = = 'ya') | (b8 == ''):
    print '\nHasta la vista, human.\n\n'
    exit()
b3[b8].fillna(0,b9 = True)
b10 = b3[b8]
a1 = 0
a2 = 0
a3 = 0
b11 = list()
for b12 in b10:
    b12 = str(b12)
    if len(b12) <= 3:
        b13 = str(b12)
        b11.append(b13)
        a1 = a1 + 1
        a3 = a3 + 1
        print 'Keeping b18'
    else :
        b13 = int(0)
        b11.append(b13)
        a2 = a2 + 1
        a3 = a3 + 1
        print 'Replacing b18'
print ' '
print 'New list created'
print ' '
print 'Number of replaced b14 = ', a2
print 'Number of kept b14 = ', a1
print 'b15 = ', a3
print ' '
b16 = open('ChangedValues.txt', 'w')
b17 = list()
for numero in b11:
    b18 = str(numero)
    b16.write(b18)
    b16.write('\n')
b16.close()
print 'File created as "ChangedValues.txt"'
print ' '