from uncompyle6.main import decompile
import marshal,time,sys,os,marcode
def fonk1():
	b1 = input("[*] decompile marshal python 3.7.X\n[?] File output: ")
	b2 = marshal.loads(marcode.py3)
	b3 = decompile(3.7,b2,sys.stdout)
	b4 = "
	with open(b1+".py","w") as f:
		f.write(b4)
	print("\n\n[result] Saved as \033[95m%s.py"%(b1))
def fonk2():
	b1 = raw_input("[*]decompile marshal python 2.7.X\n[?] File output: ")
	b2 = marshal.loads(marcode.py2)
	b3 = decompile(2.7,b2,sys.stdout)
	b4 = "
	with open(b1+".py","w") as f:
		f.write(b4)
	print("\n\n[result] Saved as \033[95m%s.py"%(b1))
try:
	os.system('clear')
	print()
	if sys.version[0] in '3':
		fonk1()
	elif sys.version[0] in '2':
		fonk2()
except Exception as F:
	print("Err: %s"%(F))