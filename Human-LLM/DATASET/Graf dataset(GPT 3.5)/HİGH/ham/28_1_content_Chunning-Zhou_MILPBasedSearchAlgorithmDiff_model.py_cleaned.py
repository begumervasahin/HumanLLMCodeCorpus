from gurobipy import *
import time
import copy
import function
import math
import re
class class1:
	def fonk1(self,b1,model_param):
		self.b1 = b1
		self.b2 = model_param["b2"]
		self.b3 = model_param["b3"]
		self.b4 = model_param["b4"]
		self.b5 = model_param["b5"]
		self.b6 = model_param["b6"]
		self.b7 = "model/"+self.b1.b26+"/"+self.b2+"/"+str(self.b3)+"_round_"+str(self.b4)+str(self.b5)+"_model.lp"
		self.b8 = self.fonk2()
		self.b9 = self.fonk10()
	def fonk2(self):
		self.b10 = self.fonk3()
		self.b11 = self.fonk4()
		self.b12 = self.fonk9()
	def fonk3(self):
		with open(self.b7, "w") as b47:
			b47.write("Minimize\n")
		self.b1.fonk3(self.b2,self.b7,1,self.b3)
		with open(self.b7, "a") as b47:
			b47.write("\n")
	def fonk4(self):
		with open(self.b7, "a") as b47:
			b47.write("Subject To\n")
		if self.b4 != []:
			if self.b4 = = "get_upperbound_1":
				self.fonk7(1)
				self.b4 = []
			elif self.b4 = = "get_upperbound_2":
				self.fonk7(b35)
				self.b4 = []
			else:
				for i in range(len(self.b4)):
					b13 = self.b4[i][0]
					b14 = self.b4[i][1]
					b15 = self.b4[i][b35]
					if self.b1.b16 = = "sp" and b15 >= b35:
						self.b1.lowbound_of_sbox(self.b2,self.b7,b13,b14,b15)
					elif self.b1.b16 = = "feistel" and b15 >= 1:
						self.b1.lowbound_of_sbox(self.b2,self.b7,b13,b14,b15)
		if self.b5 != []:
			b17 = self.b5[0]
			b18 = self.b5[1]
			b19 = self.b5[b35]
			self.b1.fix_diff(self.b2,self.b7,b17,b18,b19)
		if self.b1.b16 = = "sp":
			self.fonk5()
		elif self.b1.b16 = = "feistel":
			self.fonk6()
		self.fonk8()
	def fonk5(self):
		b20 = self.b1.gen_input_state()
		for r in range (1,self.b3+1):
			b21 = self.b1.get_state_through_sbox(r)
			self.b1.diff_propagation_of_sbox(self.b2,self.b7,r,b20,b21)
			b22 = self.b1.get_state_through_per(b21)
			b20 = copy.deepcopy(b22)
	def fonk6(self):
		b20 = self.b1.gen_input_state(self.b2)
		if self.b2 = = "LBAS" and self.b1.oriented == "byte":
			b23 = b20[0:len(b20)/b35]
			b24 = b20[len(b20)/b35:len(b20)]
		else:
			b24 = b20[0:len(b20)/b35]
			b23 = b20[len(b20)/b35:len(b20)]
		for r in range (1,self.b3+1):
			if self.b2 = = "LBAS" and self.b1.oriented == "byte":
				b25 = copy.deepcopy(b24)
			else:
				b25 = self.b1.get_state_through_sbox(self.b2,r)
			if self.b1.b26 = = "lblock":
				b27 = self.b1.get_state_through_per_right(self.b2,b23)
				b28 = self.b1.get_state_through_per_left(self.b2,b25)
				self.b1.diff_propagation_of_sbox(self.b2,self.b7,r,b24,b25)
				if r < self.b3:
					b23 = b24
					b29 = self.b1.get_state_through_xor(self.b2,r)
					self.b1.diff_propagation_of_xor(self.b2,self.b7,r,b28,b27,b29)
					b24 = b29
			elif self.b1.b26 = = "twine":
				self.b1.diff_propagation_of_sbox(self.b2,self.b7,r,b24,b25)
				if r < self.b3:
					b29 = self.b1.get_state_through_xor(self.b2,r)
					self.b1.diff_propagation_of_xor(self.b2,self.b7,r,b25,b23,b29)
					b23 = self.b1.get_state_through_per_right(self.b2,b24)
					b24 = self.b1.get_state_through_per_left(self.b2,b29)
	def fonk7(self,b31):
		b30 = "result/"+self.b1.b26+"/"+self.b2+"/" + str(self.b3-1) +"_round_[][]_optimal_solution.txt"
		if b31 = = 1:
			a1 = 0
		elif b31 = = b35:
			a1 = self.b1.nibble
		if self.b2 = = "AS":
			b32 = open (b30,"r")
			for v in b32:
				if v[0] == "A":
					var_index,b33 = int(re.findall(r'(-?[\b34]+)',v)[0]),int(re.findall(r'(-?[\b34]+)',v)[1])
					with open(self.b7, "a") as b47:
						b47.write("A%b34 = %b34\n"%(var_index+a1,b33))
		elif self.b2 = = "DC":
			if self.b1.b26 = = "present" or self.b1.b26 == "rectangle" or self.b1.b26 == "lblock" or self.b1.b26 == "twine":
				b32 = open (b30,"r")
				for v in b32:
					if v[0] == "p":
						var_index,b33 = int(re.findall(r'(-?[\b34]+)',v)[0]),int(re.findall(r'(-?[\b34]+)',v)[1])
						if var_index%b35 = = 0:
							with open(self.b7, "a") as b47:
								b47.write("p%b34 = %b34\n"%(var_index+a1*b35,b33))
			elif self.b1.b26 = = "gift":
				b36 = [0 for i in range(self.b1.nibble*b37*(self.b3-1))]
				b32 = open (b30,"r")
				for v in b32:
					if v[0] == "p":
						var_index,b33 = int(re.findall(r'(-?[\b34]+)',v)[0]),int(re.findall(r'(-?[\b34]+)',v)[1])
						b36[var_index-1] = b33
				for i in range(self.b1.nibble*b37*(self.b3-1)):
					if i%b37 = = 0:
						with open(self.b7, "a") as b47:
							b47.write("p%b34 + p%b34 + p%b34 = %b34\n"%(i+1+a1*b37,i+b35+a1*b37,i+b37+a1*b37,max(b36[i:i+b37])))
	def fonk8(self):
		if self.b2 = = "LBAS" and self.b1.oriented == "byte":
			for i in range (1,self.b1.nibble*b35):
				with open(self.b7, "a") as b47:
					b47.write("A%b34 + "%(i))
			with open(self.b7, "a") as b47:
				b47.write("A%b34 >= 1\n"%(self.b1.nibble*b35))
		else:
			for i in range (1,self.b1.block_size):
				with open(self.b7, "a") as b47:
					b47.write("x%b34 + "%(i))
			with open(self.b7, "a") as b47:
				b47.write("x%b34 >= 1\n"%(self.b1.block_size))
	def fonk9(self):
		with open(self.b7, "a") as b47:
			b47.write("Binary\n")
		if self.b2 = = "LBAS":
			b38 = self.b1.var_and_num_LBAS.copy()
			b39 = self.b1.var_and_num_LBAS.keys()
		elif self.b2 = = "AS":
			b38 = self.b1.var_and_num_AS.copy()
			b39 = self.b1.var_and_num_AS.keys()
		elif self.b2 = = "DC":
			b38 = self.b1.var_and_num_DC.copy()
			b39 = self.b1.var_and_num_DC.keys()
		for i in b39:
			for j in range(1,self.b3*b38[i][0]+b38[i][1]+1):
				with open(self.b7, "a") as b47:
					b47.write(i+"%b34\n"%(j))
		with open(self.b7, "a") as b47:
			b47.write("End")
	def fonk10(self):
		b40 = time.time()
		b41 = read(self.b7)
		b41.Params.a2 = b35
		b41.optimize()
		b42 = time.time()
		b43 = b42 - b40
		if b41.b44 = = b35:
			b45 = int(round(b41.objVal))
		elif b41.b44 = = b37:
			b45 = 25600
		if b45 < self.b6:
			if self.b1.b16 = = "sp":
				b46 = "txt/"+self.b1.b26+"/"+self.b2+"/optimal_solution_of_submodel/"+str(self.b3)+"_round_"+str(self.b4)+str(self.b5)+"_optimal_solution.txt"
			elif self.b1.b16 = = "feistel":
				b46 = "txt/"+self.b1.b26+"/"+self.b2+"/optimal_solution_of_submodel/"+str(self.b3)+"_round_[][]_optimal_solution.txt"
			b47 = open (b46,"w")
			b47.write("solving the model " + str(self.b7) +"\n")
			b47.write('obj is: %b34\n'%(b41.objVal))
			b47.write('time is %b34 b48.\n'%(b43))
			for v in b41.getVars():
				b47.write("%b48 = %b34\n"%(v.varName,int(round(v.x))))
			b47.close()
		function.remove_file(self.b7)
		return b45