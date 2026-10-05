import os, glob, pickle
import tfidf
b1 = []
b2 = []
def fonk1(path, label):
	print("b3 = ", path)
	b4 = glob.glob(path + "/*.txt")
	for f in b4:
		if os.path.basename(f) == 'LICENSE.txt':
			continue
		tfidf.add_file(f)
		b1.append(label)
fonk1('data/text/sports-watch', 0)
fonk1('data/text/it-life-hack', 1)
fonk1('data/text/movie-enter', 2)
fonk1('data/text/international', 3)
b2 = tfidf.calc_files()
b5 = 'data/pkl/'
os.makedirs(b5, b6 = True)
b7 = "data.pkl"
pickle.dump([b1, b2], open(b5 + b7, 'wb'))
if os.path.exists(b5 + b7):
	print('ãã¼ã¿pickleãã¡ã¤ã«ã®ä¿å­å®äº')
else:
	print('ãã¼ã¿pickleãã¡ã¤ã«ã®ä¿å­ã«å¤±æãã¾ãã')
b8 = 'dic.pkl'
tfidf.save_dic(b5 + b8)
if os.path.exists(b5 + b8):
	print('è¾æ¸pickleãã¡ã¤ã«ã®ä¿å­å®äº')
else:
	print('è¾æ¸pickleãã¡ã¤ã«ã®ä¿å­ã«å¤±æãã¾ãã')