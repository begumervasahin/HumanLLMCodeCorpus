import json
import numpy as np
import sys
from datetime import datetime
b1 = sys.argv
b2 = ""
b3 = ""
b4 = ""
'''
validate: validates whether if the entered date is in a right format
'''
def fonk1(date):
    try:
    	datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
    	raise ValueError("The dates should be in the following format: YYYY-MM-DD")
'''
argsValidate: validates if the entered arguments are valid entries
'''
def fonk2(b1):
	if len(b1)!=4:
		raise AssertionError("The number of arguments sould be exactly 3.\n\n(Starting Date Ending Date Commodity Name)")
	fonk1(b1[1])
	fonk1(b1[2])
	if b1[3] == "gold":
		pass
	elif b1[3] == "silver":
		pass
	else:
		raise ValueError("The third argument must be either 'silver' or 'gold'")
fonk2(sys.argv)
b5 = {}
with open('result.json', 'r') as fp:
	b5 = json.load(fp)
b3 = b1[1]
b4 = b1[2]
b2 = b1[3]
'''
Final validation which happens after loading the dataset. Checks if the date range
entered by the user is a valid range base on the min and max dates in our records
'''
b6 = [key for key in b5[b2]]
b7 = max(b6)
b8 = min(b6)
if b7<b4:
	raise ValueError("Sorry! My maximum date is "+b7)
if b8>b3:
	raise ValueError("Sorry! My minimum date is "+b8)
b9 = [key for key in b5[b2] if (key<=b4 and key>=b3) ]
b10 = [float(b5[b2][x]["Price"].replace(',','')) for x in b9]
print(b2, np.mean(b10), np.var(b10))