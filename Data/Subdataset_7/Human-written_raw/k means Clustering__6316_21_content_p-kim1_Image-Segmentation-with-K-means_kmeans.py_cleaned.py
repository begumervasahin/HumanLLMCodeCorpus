import numpy as np
class class1:
        def fonk1(self,b3,data):
                self.b1 = np.shape(data)[0]
                self.b2 = np.shape(data)[1]
                self.b3 = b3
        def fonk2(self,data,b4 = 10):
                b5 = data.min(b12=0)
                b6 = data.max(b12=0)
                self.b7 = np.random.rand(self.b3,self.b2)*(b6-b5)+b5
                b8 = np.random.rand(self.b3,self.b2)*(b6-b5)+b5
                a1 = 0
                while np.sum(np.sum(b8-self.b7))!= 0 and a1<b4:
                        b8 = self.b7.copy()
                        a1 += 1
                        b9 = np.ones((1,self.b1))*np.sum((data-self.b7[0,:])**2,b12=1)
                        for j in range(self.b3-1):
                                b9 = np.append(b9,np.ones((1,self.b1))*np.sum((data-self.b7[j+1,:])**2,b12=1),b12=0)
                        b10 = b9.argmin(b12=0)
                        b10 = np.transpose(b10*np.ones((1,self.b1)))
                        for j in range(self.b3):
                                b11 = np.where(b10==j,1,0)
                                if sum(b11)>0:
                                        self.b7[j,:] = np.sum(data*b11,b12 = 0)/np.sum(b11)
                return self.b7
        def fonk3(self,data):
                b1 = np.shape(data)[0]
                b9 = np.ones((1,b1))*np.sum((data-self.b7[0,:])**2,b12=1)
                for j in range(self.b3-1):
                        b9 = np.append(b9,np.ones((1,b1))*np.sum((data-self.b7[j+1,:])**2,b12=1),b12=0)
                b10 = b9.argmin(b12=0)
                b10 = np.transpose(b10*np.ones((1,b1)))
                return b10