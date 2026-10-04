from __future__ import division
import time
import numpy as np
import numpy.random as npr
import blspricer as bp
import customML as cm
import scipy.stats as scs
from scipy.stats.distributions import norm
from doe_lhs import lhs
class class1(object):
	def fonk1(self):
		self.a1 = 10
		self.b1 = 100.; self.mu = 0.08; self.sigma = 0.3
		self.b2 = 0.05; self.T = 0.1; self.tau = 0.04
		self.b3 = 100.; self.H = 95.
		self.b4 = 306.8763; self.perc = 0.99
		self.b5 = 2.**15
		self.a2 = 1e-6
		b6 = lambda S: 5.*bp.blsprice(S,self.b3,self.b2,self.T,self.sigma,'put') \
							+ 10.*bp.rear_end_dnOutCall(S,self.b3,self.b2,self.T,self.sigma,self.H,self.tau,0.)
		self.a3 = 0.
		self.b7 = np.zeros(self.a1)
		for d in range(self.a1):
			self.b7[d] = (b6(self.b1+self.a2)-b6(self.b1-self.a2))/self.a2
			self.a3 += -b6(self.b1) + self.b1 * self.b7[d]
		print self.b7
	def fonk2(self,N_o):
		''' Analytical solution
		'''
		b6 = lambda S: 5.*bp.blsprice(S,self.b3,self.b2,self.T-self.tau,self.sigma,'put') \
							+ 10.*bp.dnOutCall(S,self.b3,self.b2,self.T-self.tau,self.sigma,self.H)
		b8 = norm(loc=0,scale=1).ppf(lhs(self.a1,samples=N_o))
		b9 = np.zeros((N_o,self.a1))
		b9[:,:] = self.b1
		b9[:,:] = b9[:,:] * np.exp((self.mu - 0.5 * self.sigma**2) * self.tau\
				 + self.sigma * np.sqrt(self.tau) * b8[:,:])
		b10 = np.zeros(N_o)
		for n in range(N_o):
			for d in range(self.a1):
				b10[n] += -b6(b9[n,d]) + b9[n,d] * self.b7[d]
		b11 = np.sort(self.a3 - b10)
		print b11
		b12 = scs.scoreatpercentile(b11, self.perc*100.)
		b13 = np.mean(np.maximum(b11-b12,0))
		return (b12, b13)