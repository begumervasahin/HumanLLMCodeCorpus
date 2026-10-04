import pandas as pd
import matplotlib.pylab as plt
from sklearn import preprocessing
from scipy.stats import skew
import numpy as np
import seaborn
import re
print ' '
print ' '
print '                 Welcome to SkewU.py'
print '                 --by Niam Moltta--'
print '                      ~~/\
print ' '
print ' '
print ' '
print 'Application: SKEWNESS CALCULATION.\n\nINSTRUCTIONS:\n\n- Select file, select b8.\n- Returns skewness value.\n- Returns skewness representation graph.\n\n'
b1 = raw_input('Enter .csv file name: ')
if b1 = = '':
    print ' '
    print 'Arrivederci!'
    print ' '
    exit()
print ' '
b2 = str(b1)
b3 = pd.read_csv(b2)
b4 = pd.DataFrame(b3)
b5 = b4.b6
b6 = np.asarray(b5)
while True:
    print ' '
    print 'Columns in', re.findall('(.+?).csv', b2), 'are:\n'
    print b6
    print ' '
    b7 = raw_input('Enter b8 header: ')
    b8 = str(b7)
    if (b8 = = '') | (b8 == 'ya'):
        break
    else:
        b3[b8].fillna(0,b9 = True)
        print 'Missing values replaced with zeros.'
        print ' '
        b10 = preprocessing.scale(b3[b8])
        b11 = skew(b10)
        b12 = str(b11)
        b13 = plt.b13()
        print 'b14 = ', b11
        b13.add_subplot(121)
        plt.hist(b10,b15 = 'lightblue',alpha=0.75)
        plt.b12(" b14 greater than zero shows large skewed distribution --> ")
        plt.title(b8)
        plt.text(2,100000,"b14: {0:.2f}".format(b11))
        b13.add_subplot(122)
        plt.boxplot(b10)
        plt.title("Skewed Distribution")
        plt.b12(b12)
        plt.show()
print '\nHasta la vista, human.\n'