import os, glob, pickle
import tfidf
y = []
x = []
def read_files(path, label):
	print("read_files=", path)
	files = glob.glob(path + "/*.txt")
	for f in files:
		if os.path.basename(f) == 'LICENSE.txt':
			continue
		tfidf.add_file(f)
		y.append(label)
read_files('data/text/sports-watch', 0)
read_files('data/text/it-life-hack', 1)
read_files('data/text/movie-enter', 2)
read_files('data/text/international', 3)
x = tfidf.calc_files()
dir_for_pkls = 'data/pkl/'
os.makedirs(dir_for_pkls, exist_ok=True)
pkl_for_data = "data.pkl"
pickle.dump([y, x], open(dir_for_pkls + pkl_for_data, 'wb'))
if os.path.exists(dir_for_pkls + pkl_for_data):
	print('ãã¼ã¿pickleãã¡ã¤ã«ã®ä¿å­å®äº')
else:
	print('ãã¼ã¿pickleãã¡ã¤ã«ã®ä¿å­ã«å¤±æãã¾ãã')
pkl_for_dic = 'dic.pkl'
tfidf.save_dic(dir_for_pkls + pkl_for_dic)
if os.path.exists(dir_for_pkls + pkl_for_dic):
	print('è¾æ¸pickleãã¡ã¤ã«ã®ä¿å­å®äº')
else:
	print('è¾æ¸pickleãã¡ã¤ã«ã®ä¿å­ã«å¤±æãã¾ãã')