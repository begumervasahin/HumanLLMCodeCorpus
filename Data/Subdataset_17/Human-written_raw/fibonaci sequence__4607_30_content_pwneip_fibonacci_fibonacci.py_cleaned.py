from math import sqrt
import argparse
__author__ = "PwnEIP"
__copyright__ = "Copyright 2007, The Cogent Project"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "PwnEIP"
__email__ = "pwneip@gmail.com"
__status__ = "Production"
def main():
	output = ""
	parser = argparse.ArgumentParser(description='Generate Fibonacci sequence',
			usage="fibonacci.py [-b] number",
			version="fibonacci.py 1.0",
			add_help=True)
	parser.add_argument("-b", "--binary",
			action="store_true",
			dest="binary",
			default=False,
			help="Print output in binary",)
	parser.add_argument("number",
			type=int,
			help="Generate n length sequence",)
	try:
    		arguments = parser.parse_args()
	except IOError, msg:
    		parser.error(str(msg))
	for x in range(1, int(arguments.number) +1):
		if (arguments.binary):
			output +=  bin(fibonacci(x))[2:] + " "
		else:
			output +=  repr(fibonacci(x)) + " "
	print output
def fibonacci(n):
	return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
if __name__ == '__main__':
    main()