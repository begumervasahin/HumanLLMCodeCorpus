    import cv2
    import os
    import numpy as np
    b1 = input("Enter the classifier b1\n")
    b2 = "images/"+b1
    os.mkdir(b2)
    print("Folder craeted for : ",b1,"\n")
    b3 = cv2.VideoCapture(0)
    b4 = cv2.VideoWriter_fourcc(*'XVID')
    b5 = cv2.VideoWriter('output.avi',b4, 20.0, (640,480))
    while(b3.isOpened()):
        b7, b6 = b3.read()
        if b7 = =True:
            b6 = cv2.flip(b6,1)
            b5.write(b6)
            cv2.imshow('b6',b6)
            if cv2.waitKey(1) & b8 = = ord('q'):
                break
        else:
            break
    b3.release()
    b5.release()
    cv2.destroyAllWindows()
    b9 = cv2.VideoCapture('output.avi')
    b11,b10 = b9.read()
    a1 = 0
    b11 = True
    while b11:
      b11,b10 = b9.read()
      if(b11 = =True):
      cv2.imwrite('images/'+b1+'/b6%d.jpg' % a1, b10)
      print('Read a new b6: ', b11)
      a1 += 1
    else:
      pass