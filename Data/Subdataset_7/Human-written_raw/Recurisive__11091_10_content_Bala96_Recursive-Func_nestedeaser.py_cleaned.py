
import sys
def fonk1(the_list,b1 = False,level=0,fh=sys.stdout):
	for each_item in the_list :
		if isinstance (each_item,list):
			fonk1(each_item,b1,level+1,fh)
		else :
			if b1:
				for tab_stop in range(level):
					print("\t",b2 = '',b3=fh)
			print(each_item,b3 = fh)
