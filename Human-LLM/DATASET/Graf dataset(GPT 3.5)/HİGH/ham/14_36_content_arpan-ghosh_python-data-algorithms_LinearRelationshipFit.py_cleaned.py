import pandas
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn import datasets
from sklearn import linear_model
b1 = ['x','b10']
b2 = pandas.read_csv('/home/idies/workspace/AS.171.205/data/b2.csv', names=b1, header=None)
b3 = pandas.read_csv('/home/idies/workspace/AS.171.205/data/b3.csv', names=b1, header=None)
b4 = pandas.read_csv('/home/idies/workspace/AS.171.205/data/b4.csv', names=b1, header=None)
b5 = pandas.read_csv('/home/idies/workspace/AS.171.205/data/b5.csv', names=b1, header=None)
plt.figure(b6 = (12,8))
fig, b7 = plt.subplots(1, 4, sharey=True)
b2.plot(b8 = 'scatter', x='x', b10='b10', ax=b7[0], b6=(16, 8))
b3.plot(b8 = 'scatter', x='x', b10='b10', ax=b7[1], b6=(16, 8))
b4.plot(b8 = 'scatter', x='x', b10='b10', ax=b7[2], b6=(16, 8))
b5.plot(b8 = 'scatter', x='x', b10='b10', ax=b7[3], b6=(16, 8))
b7[0].set_title("b2.csv Scatter")
b7[1].set_title("b3.csv Scatter")
b7[2].set_title("b4.csv Scatter")
b7[3].set_title("b5.csv Scatter")
plt.xlabel("x")
plt.ylabel("b10")
plt.legend()
plt.show()
from numpy import *
from scipy.interpolate import *
from matplotlib.pyplot import *
from sklearn import datasets
from sklearn import linear_model
print ('Bfit.csv')
plot(b2.x,b2.b10,'o')
plot(b2.x,polyval(b9,b2.x), 'r-')
plot(b2.x,polyval(b11,b2.x), 'b--')
plot(b2.x,polyval(b12,b2.x), 'm:')
b9 = polyfit(b2.x, b2.b10, 1)
print('The following will give me the b10 = mx+b format, and print the slope and intercept')
print(b9)
print ()
b11 = polyfit(b2.x, b2.b10, 2)
print('The following will give me the quadratic and print its coefficients')
print (b11)
print ()
b12 = polyfit(b2.x, b2.b10, 3)
print('The following will give me the polynomial and print its coefficients')
print (b12)
b13 = b9[0] * b2.x + b9[1]
b14 = b2.b10 - b13
b15 = sum(pow(b14,2))
b16 = len(b2.b10) * var(b2.b10)
b17 = 1 - b15/b16
print ()
print('I am computing the r squared value using the b13 derived')
print(b17)
print ()
from scipy.stats import *
slope, intercept, r_value, p_value, b18 = linregress(b2.x, b2.b10)
print('I am computing the r squared value using the scipy method')
print(pow(r_value,2))
print ()
print('This is the pvalue')
print(p_value)
print ('                                             Bfit.csv')
from numpy import *
from scipy.interpolate import *
from matplotlib.pyplot import *
from sklearn import datasets
from sklearn import linear_model
print ('Cfit.csv')
plot(b3.x,b3.b10,'o')
plot(b3.x,polyval(b19,b3.x), 'r-')
plot(b3.x,polyval(b20,b3.x), 'b--')
plot(b3.x,polyval(b21,b3.x), 'm:')
b19 = polyfit(b3.x, b3.b10, 1)
print('The following will give me the b10 = mx+b format, and print the slope and intercept')
print(b19)
print ()
b20 = polyfit(b3.x, b3.b10, 2)
print('The following will give me the quadratic and print its coefficients')
print (b20)
print ()
b21 = polyfit(b3.x, b3.b10, 3)
print('The following will give me the polynomial and print its coefficients')
print (b21)
b13 = b19[0] * b3.x + b19[1]
b14 = b3.b10 - b13
b15 = sum(pow(b14,2))
b16 = len(b3.b10) * var(b3.b10)
b17 = 1 - b15/b16
print ()
print('I am computing the r squared value using the b13 derived')
print(b17)
print ()
from scipy.stats import *
slope, intercept, r_value, p_value, b18 = linregress(b3.x, b3.b10)
print('I am computing the r squared value using the scipy method')
print(pow(r_value,2))
print ()
print('This is the pvalue')
print(p_value)
print ('                                             Cfit.csv')
from numpy import *
from scipy.interpolate import *
from matplotlib.pyplot import *
from sklearn import datasets
from sklearn import linear_model
print ('b4.csv')
plot(b4.x,b4.b10,'o')
plot(b4.x,polyval(b22,b4.x), 'r-')
plot(b4.x,polyval(b23,b4.x), 'b--')
plot(b4.x,polyval(b24,b4.x), 'm:')
b22 = polyfit(b4.x, b4.b10, 1)
print('The following will give me the b10 = mx+b format, and print the slope and intercept')
print(b22)
print ()
b23 = polyfit(b4.x, b4.b10, 2)
print('The following will give me the quadratic and print its coefficients')
print (b23)
print ()
b24 = polyfit(b4.x, b4.b10, 3)
print('The following will give me the polynomial and print its coefficients')
print (b24)
b13 = b22[0] * b4.x + b22[1]
b14 = b4.b10 - b13
b15 = sum(pow(b14,2))
b16 = len(b4.b10) * var(b4.b10)
b17 = 1 - b15/b16
print ()
print('I am computing the r squared value using the b13 derived')
print(b17)
print ()
from scipy.stats import *
slope, intercept, r_value, p_value, b18 = linregress(b4.x, b4.b10)
print('I am computing the r squared value using the scipy method')
print(pow(r_value,2))
print ()
print('This is the pvalue')
print(p_value)
print ('                                             Dfit.csv')
from numpy import *
from scipy.interpolate import *
from matplotlib.pyplot import *
from sklearn import datasets
from sklearn import linear_model
print ('b5.csv')
plot(b5.x,b5.b10,'o')
plot(b5.x,polyval(b19,b5.x), 'r-')
plot(b5.x,polyval(b20,b5.x), 'b--')
plot(b5.x,polyval(b21,b5.x), 'm:')
b25 = polyfit(b5.x, b5.b10, 1)
print('The following will give me the b10 = mx+b format, and print the slope and intercept')
print(b25)
print ()
b26 = polyfit(b5.x, b5.b10, 2)
print('The following will give me the quadratic and print its coefficients')
print (b26)
print ()
b27 = polyfit(b5.x, b5.b10, 3)
print('The following will give me the polynomial and print its coefficients')
print (b27)
b13 = b25[0] * b5.x + b25[1]
b14 = b5.b10 - b13
b15 = sum(pow(b14,2))
b16 = len(b5.b10) * var(b5.b10)
b17 = 1 - b15/b16
print ()
print('I am computing the r squared value using the b13 derived')
print(b17)
print ()
from scipy.stats import *
slope, intercept, r_value, p_value, b18 = linregress(b5.x, b5.b10)
print('I am computing the r squared value using the scipy method')
print(pow(r_value,2))
print ()
print('This is the pvalue')
print(p_value)
print ('                                             b5.csv')