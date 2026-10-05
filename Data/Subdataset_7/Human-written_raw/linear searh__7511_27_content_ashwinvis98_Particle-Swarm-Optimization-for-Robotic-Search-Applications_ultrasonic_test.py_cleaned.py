import os
import time
import threading
import nxt
from nxt.sensor import *
b1 = nxt.locator.find_one_brick('00:16:53:0C:1D:29')
def fonk1():
	while True:
		b2 = Ultrasonic(b1, PORT_2,check_compatible=False).get_sample()
		print("obstacle at",b2)
	'''if b2 < 50 :
		print('You are close Iam going to take your picture')
		b3 = b3 + 1
		b4 = str(b3) + '.jpg'
		os.system('fswebcam -r 352x288 ' + b4)
		time.sleep(1)'''
def fonk2(a1):
	a1 = 0
	while(True):
		a1 = a1+1
		print("a1 = ",a1)
b5 = threading.Thread(target=ultra)
b6 = threading.Thread(target=cal,args=1)
b5.start()
b6.start()
b5.join()
b6.join()