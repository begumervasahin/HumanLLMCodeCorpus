import numpy as np
import matplotlib.pyplot as plt
class class1(object):
		def fonk1(self,datafile):
			self.x, self.y, self.b1 = np.loadtxt(datafile, unpack=True)
		def fonk2(self,nsteps, min, max):
			b2 = np.linspace(min,max,num=nsteps)
			b3 = np.linspace(min,max,num=nsteps)
			b4 = abs(max-min)/float(nsteps)
			b5 = abs(max-min)/float(nsteps)
			self.a1 = 0
			self.a2 = 0
			self.b6 = np.zeros(shape=(nsteps,nsteps))
			for i in range(len(b2)):
				for j in range(len(b3)):
					a3 = 1
					for k in range(len(self.x)):
						a3 *= (1/(np.sqrt(2*3.14)*self.b1[k]))*np.exp(-((self.y[k]-(b2[i]*self.x[k]+b3[j]))**2)/(2*self.b1[k]**2))
					self.b6[i][j]=a3
			a4 = 0
			for i in range(len(b2)):
				for j in range(len(b3)):
					a4+=b5*self.b6[i][j]*b4
			self.a4 = a4
			for i in range(len(b2)):
				for j in range(len(b3)):
					self.a1 += b2[i]*self.b6[i][j]*b5*b4/self.a4
					self.a2 += b3[i]*self.b6[j][i]*b5*b4/self.a4
			a5 = 0
			a6 = 0
			for i in range(len(b2)):
				for j in range(len(b3)):
					a5 += (b2[i]-self.a1)**2*self.b6[i][j]*b5*b4/self.a4
					a6 += (b3[i]-self.a2)**2*self.b6[j][i]*b5*b4/self.a4
			self.a5 = np.sqrt(a5)
			self.a6 = np.sqrt(a6)
			a7 = 0
			for i in range(len(b2)):
				for j in range(len(b3)):
					a7 += (b2[i]-self.a1)*(b3[j]-self.a2)*self.b6[i][j]*b5*b4/self.a4
			self.a7 = a7
			self.b7 = self.a7/(self.a5*self.a6)
		def fonk3(self):
			plt.plot(self.x,self.y,'o')
			b8 = np.linspace(0,10,100)
			b9 = (self.a1)*b8+(self.a2)
			return plt.plot(b8, b9)