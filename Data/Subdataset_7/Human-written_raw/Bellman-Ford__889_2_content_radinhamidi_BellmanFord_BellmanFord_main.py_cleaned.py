
import numpy as np
b1 = int(input("PLease enter number of routers : "))
b2 = np.full((b1,b1),100,int)
b3 = np.full((1,b1,b1,b1),100,int)
def fonk1(b6):
    b4 = np.full((1,b1,b1,b1),100)
    for i in range(b1):
        for j in range(b1):
            if i!=j :
                if b6[b6.shape[0]-1,i,i,j]==100 :
                    b4[0,i,j,:]=100
                else:
                    b4[0,i,j,:]=b6[b6.shape[0]-1,j,j,:]
            else:
                for b5 in range(b1):
                    if b5 = =i :
                        b4[0,i,i,b5]=0
                    else :
                        b4[0,i,i,b5]=100
                        for u in range(b1):
                            if  (b6[b6.shape[0]-1,i,i,u]+b6[b6.shape[0]-1,u,u,b5])<b4[0,i,i,b5]:
                                b4[0,i,i,b5]=(b6[b6.shape[0]-1,i,i,u]+b6[b6.shape[0]-1,u,u,b5])
    if np.array_equal(b6[b6.shape[0]-1,:,:,:],b4[0,:,:,:]) is False:
         b6 = np.concatenate((b6,b4))
    return b6
for i in range(b1):
    b7 = input("Fill row number %d of the matrix "%(i+1))
    b2[i]=np.fromstring(b7,b8 = int, sep=' ')
for j in range(b1):
    b3[0,j,j,:]=b2[j,:]
while 1:
    b9 = b3.shape[0]
    b3 = fonk1(b3)
    b10 = b3.shape[0]
    if b10 = =b9 :
        break
b11 = b3.shape
b11 = b11[0]
while 1:
    print("\nthere are %d iterations and %d routers\n"%(b11,b1))
    print("-------------------------------------------------------------")
    b12 = input("Routing finished successfully...\nPlease enter iteration level you want to take a look at.\n")
    b13 = input("Enter router number or enter 'a' for overall view.\n")
    if b13 = ='a' :
        print(b3[int(b12)-1,:,:,:])
    else:
        print(b3[int(b12)-1,int(b13)-1,:,:])
    if input("Do you need more report ? (Y/N)").__le__('n') :
        break