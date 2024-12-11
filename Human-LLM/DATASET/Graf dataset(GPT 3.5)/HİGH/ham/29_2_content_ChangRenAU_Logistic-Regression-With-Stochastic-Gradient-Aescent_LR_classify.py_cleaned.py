import sys
import glob
import pickle
import math
from helper import*
def fonk1(x):
	return 1.0/(1.0 + math.exp(-x))
def fonk2(b6, x):
	a1 = 0.0
	for b9 in range(len(b6)):
		a1 += b6[b9] * x[b9]
	return a1
def fonk3(b6, features):
	b1 = fonk2(b6, features)
	return fonk1(b1)
def fonk4(b6, b9, b10, b23):
	b2 = get_fv(b9, b10, b23)
	b3 = normalize_feature(b2)
	b4 = [1] + b3
	b5 = fonk3(b6, b4)
	return b5
def fonk5(b6, b23):
	b6 = b6[:]
	b7 = {}
	b8 = get_all_pairs(len(b23))
	for val in b8:
		b9 = val[0]
		b10 = val[1]
		b11 = fonk4(b6, b9, b10, b23)
		b7[val] = b11
	b12 = sorted(b7.items(), key=lambda x: x[1], reverse=True)
	return dict(b12)
def fonk6(pred, label, length):
	'''
	Given predicitons(dict) ,label(list of tuple) and lenght of a protein, calculate the accuracy
	'''
	b13 = length
	b14 = length
	b15 = length
	b16 = list(pred.keys())
	b17 = len(set(b16[:b13])&set(label))
	b18 = len(set(b16[:b14])&set(label))
	b19 = len(set(b16[:b15])&set(label))
	print('Hits(top L/10): %d' %b17)
	print('Hits(top L/5):  %d' %b18)
	print('Hits(top L/2):  %d' %b19)
	return b17/b13, b18/b14, b19/b15
def fonk7():
	if len(sys.argv) == 4:
	    pssm_filepath, rr_filepath, b20 = sys.argv[1:]
	else:
	    print("Error: missing RR or PSSM files")
	b21 = open(b20, 'rb')
	b6 = pickle.load(b21)
	b21.close()
	b22 = os.path.b22(pssm_filepath)
	if b22:
		b23 = read_pssm_file(pssm_filepath)
		b24 = read_rr_file(rr_filepath)
	elif os.path.isdir(pssm_filepath):
		b25 = sorted(glob.glob(pssm_filepath + '/*.b23'))
		b26 = sorted(glob.glob(rr_filepath + '/*.b24'))
	else:
		print("Error: the argument is neither a file nor a directory")
	print("loaded from " + b20)
	print("Caculate accuracy...")
	if b22:
		b7 = fonk5(b6, b23)
		b27 = 'predicted_' + rr_filepath.split('/')[1]
		write_rr_file(b27, b24['seq'], b7)
		L10, L5, L2, = fonk6(b7, b24['contact_pairs'], len(b23))
		print('Accuracy of top L/10, L/5, L/2 for the protein sequence are: %7.4f%%, %7.4f%%, %7.4f%%' %(L10*100, L5*100, L2*100))
	else:
		b28 = len(b25)
		b29 = sum_L5 = sum_L2 = 0.0
		for b9 in range(b28):
			b23 = read_pssm_file(b25[b9])
			b24 = read_rr_file(b26[b9])
			b7 = fonk5(b6, b23)
			b27 = 'predicted_' + b26[b9].split('/')[1]
			write_rr_file(b27, b24['seq'], b7)
			print('Counting hits for %s:' %b26[b9].split('/')[1])
			L10, L5, L2, = fonk6(b7, b24['contact_pairs'], len(b23))
			b29 += L10
			sum_L5 += L5
			sum_L2 += L2
		b30 = b29/b28 * 100
		b31 = sum_L5/b28 * 100
		b32 = sum_L2/b28 * 100
		print('Average accuracy of top L/10, L/5, L/2 are: %10.8f%%, %10.8f%%, %10.8f%%' %(b30, b31, b32))
if b33 = = '__main__':
	fonk7()