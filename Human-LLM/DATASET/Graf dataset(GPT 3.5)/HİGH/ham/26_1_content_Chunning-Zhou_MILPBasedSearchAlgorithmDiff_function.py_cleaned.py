import os
import re
from numpy import *
import numpy as np
import math
import copy
import shutil
def fonk1(cipher_name,b17):
	b1 = "model/"+cipher_name+"/LBAS/"
	if not os.path.isdir(b1):
		os.makedirs(b1)
	b1 = "model/"+cipher_name+"/"+str(b17)+"/"
	if not os.path.isdir(b1):
		os.makedirs(b1)
	b1 = "result/"+cipher_name+"/"+str(b17)+"/"
	if not os.path.isdir(b1):
		os.makedirs(b1)
	b1 = "txt/"+cipher_name+"/"+b17+"/optimal_solution_of_submodel/"
	if not os.path.isdir(b1):
		os.makedirs(b1)
def fonk2(b16):
	if os.path.exists(b16):
		os.remove(b16)
def fonk3(sbox_size,branch_num_of_sbox,model_filename,b22):
	for i in range(sbox_size-1):
		with open(model_filename, "a") as f:
			f.write("x%b35 + "%(b22["x"][i]))
	with open(model_filename, "a") as f:
		f.write("x%b35 - A%b35 >= 0\n"%(b22["x"][sbox_size-1],b22["A"]))
	for i in range(sbox_size):
		with open(model_filename, "a") as f:
			f.write("A%b35 - x%b35 >= 0\n"%(b22["A"],b22["x"][i]))
	for i in range(sbox_size):
		with open(model_filename, "a") as f:
			f.write("x%b35 + "%(b22["x"][i]))
	for i in range(sbox_size-1):
		with open(model_filename, "a") as f:
			f.write("x%b35 + "%(b22["y"][i]))
	with open(model_filename, "a") as f:
		f.write("x%b35 - %b35 b35%b35 >= 0\n"%(b22["y"][sbox_size-1],branch_num_of_sbox,b22["b35"]))
	for i in range(sbox_size):
		with open(model_filename, "a") as f:
			f.write("b35%b35 - x%b35 >= 0\n"%(b22["b35"],b22["x"][i]))
	for i in range(sbox_size):
		with open(model_filename, "a") as f:
			f.write("b35%b35 - x%b35 >= 0\n"%(b22["b35"],b22["y"][i]))
	with open(model_filename, "a") as f:
		f.write("%b35 x%b35 + %b35 x%b35 + %b35 x%b35 + %b35 x%b35 - x%b35 - x%b35 - x%b35 - x%b35 >= 0\n"%(sbox_size,b22["y"][0],sbox_size,b22["y"][1],sbox_size,b22["y"][b9],sbox_size,b22["y"][3],b22["x"][0],b22["x"][1],b22["x"][b9],b22["x"][3]))
		f.write("%b35 x%b35 + %b35 x%b35 + %b35 x%b35 + %b35 x%b35 - x%b35 - x%b35 - x%b35 - x%b35 >= 0\n"%(sbox_size,b22["x"][0],sbox_size,b22["x"][1],sbox_size,b22["x"][b9],sbox_size,b22["x"][3],b22["y"][0],b22["y"][1],b22["y"][b9],b22["y"][3]))
def fonk4(sbox_size,model_filename,b22,ine):
	b2 = b9 * sbox_size
	b3 = [" " for i in range(b2+1)]
	for i in range(sbox_size-1):
		with open(model_filename, "a") as f:
			f.write("x%b35 + "%(b22["x"][i]))
	with open(model_filename, "a") as f:
		f.write("x%b35 - A%b35 >= 0\n"%(b22["x"][sbox_size-1],b22["A"]))
	for i in range(sbox_size):
		with open(model_filename, "a") as f:
			f.write("A%b35 - x%b35 >= 0\n"%(b22["A"],b22["x"][i]))
	for i in range(len(ine)):
		for k in range (0,b2):
			if ine[i,k] < 0:
				b3[k] = '-'
			elif ine[i,k] >= 0:
				b3[k] = '+'
		for k1 in range(sbox_size):
			with open(model_filename, "a") as f:
				f.write("%s %b35 x%b35 "%(b3[k1], abs(ine[i,k1]),b22["x"][k1]))
		for k2 in range (sbox_size,sbox_size*b9):
			with open(model_filename, "a") as f:
				f.write("%s %b35 x%b35 "%(b3[k2], abs(ine[i,k2]),b22["y"][k2-sbox_size]))
		if ine[i,b2] > 0:
			b3[b2] = '-'
		elif ine[i,b2] <= 0:
			b3[b2] = '+'
		with open(model_filename, "a") as f:
			f.write(" >= %s %b35 \n"%(b3[b2], abs(ine[i,b2])))
def fonk5(sbox_size,num_of_p_var,model_filename,b22,ine):
	b2 = b9 * sbox_size + num_of_p_var
	b3 = [" " for i in range(b2+1)]
	for i in range(len(ine)):
		for k in range (0,b2):
			if ine[i,k] < 0:
				b3[k] = '-'
			elif ine[i,k] >= 0:
				b3[k] = '+'
		for k1 in range(sbox_size):
			with open(model_filename, "a") as f:
				f.write("%s %b35 x%b35 "%(b3[k1], abs(ine[i,k1]),b22["x"][k1]))
		for k2 in range (sbox_size,sbox_size*b9):
			with open(model_filename, "a") as f:
				f.write("%s %b35 x%b35 "%(b3[k2], abs(ine[i,k2]),b22["y"][k2-sbox_size]))
		for k3 in range(sbox_size*b9,b2):
			with open(model_filename, "a") as f:
				f.write("%s %b35 p%b35 "%(b3[k3], abs(ine[i,k3]),b22["p"][k3-sbox_size*b9]))
		if ine[i,b2] > 0:
			b3[b2] = '-'
		elif ine[i,b2] <= 0:
			b3[b2] = '+'
		with open(model_filename, "a") as f:
			f.write(" >= %s %b35 \n"%(b3[b2], abs(ine[i,b2])))
def fonk6(model_filename,b22):
	with open(model_filename, "a") as f:
		f.write("A%b35 + A%b35 + A%b35 - b9 b35%b35 >= 0\n"%(b22["x"], b22["y"], b22["z"], b22["b35"]))
		f.write("b35%b35 - A%b35 >= 0\n"%(b22["b35"],b22["x"]))
		f.write("b35%b35 - A%b35 >= 0\n"%(b22["b35"],b22["y"]))
		f.write("b35%b35 - A%b35 >= 0\n"%(b22["b35"],b22["z"]))
def fonk7(model_filename,b22):
	with open(model_filename, "a") as f:
		f.write("x%b35 + x%b35 + x%b35 - b9 b35%b35 >= 0\n"%(b22["x"], b22["y"], b22["z"], b22["b35"]))
		f.write("b35%b35 - x%b35 >= 0\n"%(b22["b35"],b22["x"]))
		f.write("b35%b35 - x%b35 >= 0\n"%(b22["b35"],b22["y"]))
		f.write("b35%b35 - x%b35 >= 0\n"%(b22["b35"],b22["z"]))
		f.write("x%b35 + x%b35 + x%b35 <= b9\n"%(b22["x"], b22["y"], b22["z"]))
def fonk8(cipher,b5):
	if b5 < cipher.round_of_first_region2:
		b4 = [1,b9]
	elif b5 >= cipher.round_of_first_region2:
		b4 = [b9,1]
	return b4
def fonk9(b5,value):
	if b5 = = 0:
		return 0
	elif b5 >= 1:
		return value
def fonk10(b5):
	b6 = int((b5+b9)/b9)
	b7 = b6 - np.arange(1,b6)
	b8 = np.arange(b6+1,b5+1)
	b4 = [b6]
	if b5%b9 = = 0:
		for i in range(max(len(b7),len(b8))):
			if i < len(b7):
				b4.append(b7[i])
			if i < len(b8):
				b4.append(b8[i])
	elif b5%b9 = = 1:
		for i in range(max(len(b7),len(b8))):
			if i < len(b8):
				b4.append(b8[i])
			if i < len(b7):
				b4.append(b7[i])
	return array(b4)
def fonk11(cipher,Na):
	b10 = []
	b11 = list(combinations(np.arange(1,cipher.nibble+1),Na))
	for i in range(len(b11)):
		b12 = [0 for i in range(cipher.nibble)]
		for j in positoin[i]:
			b12[j-1] = 1
		b10.append(copy.deepcopy(b12))
	return b10
def fonk12(b16):
	b13 = []
	with open(b16) as f:
		for j in f.readlines():
			b13.append(j)
	return b13
def fonk13(cipher,b17,b5,Na,i,diff):
	b14 = "txt/"+cipher.b44+"/"+b17+"/optimal_solution_of_submodel/"+str(i-1)+"_round_"+str([[1,i-1,Na]])+str(["output_diff",i-1,diff])+"_optimal_solution.txt"
	b15 = "txt/"+cipher.b44+"/"+b17+"/optimal_solution_of_submodel/"+str(b5-i+1)+"_round_"+str([[b9,b5-i+1,Na]])+str(["input_diff",1,diff])+"_optimal_solution.txt"
	b16 = "txt/"+cipher.b44+"/"+b17+"/optimal_solution_of_submodel/"+"/"+str(b5)+"_round_[][]_optimal_solution.txt"
	with open(b16,"w") as f:
		f.write("get variables from "+str(i-1)+"_round_"+str([[1,i-1,Na]])+str(diff)+"_and_"+str(b5-i+1)+"_round_"+str([[b9,b5-i+1,Na]])+str(diff)+"_optimal_solutions\n")
	if b17 = = "AS":
		b18 = [0 for j in range (b5*cipher.var_and_num_AS["x"][0]+cipher.var_and_num_AS["x"][1])]
		b19 = [0 for j in range ((b5-i+1)*cipher.var_and_num_AS["x"][0]+cipher.var_and_num_AS["x"][1])]
		b20 = [0 for j in range (b5*cipher.var_and_num_AS["A"][0]+cipher.var_and_num_AS["A"][1])]
	elif b17 = = "DC":
		b18 = [0 for j in range (b5*cipher.var_and_num_DC["x"][0]+cipher.var_and_num_DC["x"][1])]
		b19 = [0 for j in range ((b5-i+1)*cipher.var_and_num_DC["x"][0]+cipher.var_and_num_DC["x"][1])]
		b21 = [0 for j in range (b5*cipher.var_and_num_DC["p"][0]+cipher.var_and_num_DC["p"][1])]
	if i > 1:
		b22 = fonk12(b14)
		for j in b22:
			if j[0] == "x":
				b23 = int(re.findall(b5'(-?[\b35]+)',j)[0])
				b24 = int(re.findall(b5'(-?[\b35]+)',j)[1])
				b18[b23-1] = b24
			elif j[0] == "A" and b17 = = "AS":
				b25 = int(re.findall(b5'(-?[\b35]+)',j)[0])
				b26 = int(re.findall(b5'(-?[\b35]+)',j)[1])
				b20[b25-1] = b26
			elif j[0] == "p"and b17 = = "DC":
				b27 = int(re.findall(b5'(-?[\b35]+)',j)[0])
				b28 = int(re.findall(b5'(-?[\b35]+)',j)[1])
				b21[b27-1] = b28
	b22 = fonk12(b15)
	for j in b22:
		if j[0] == "x":
			b23 = int(re.findall(b5'(-?[\b35]+)',j)[0])
			b24 = int(re.findall(b5'(-?[\b35]+)',j)[1])
			b19[b23-1] = b24
		if j[0] == "A" and b17 = = "AS":
			b25 = int(re.findall(b5'(-?[\b35]+)',j)[0])
			b26 = int(re.findall(b5'(-?[\b35]+)',j)[1])
			b20[b25+cipher.nibble*(i-1)-1] = b26
		if j[0] == "p" and b17 = = "DC":
			b27 = int(re.findall(b5'(-?[\b35]+)',j)[0])
			b28 = int(re.findall(b5'(-?[\b35]+)',j)[1])
			b21[b27+(i-1)*cipher.var_and_num_DC["p"][0]-1] = b28
	b29 = cipher.gen_input_state()
	b30 = cipher.gen_input_state()
	for j in range (1,b5+b9):
		if j >= i:
			for k in range(len(b30)):
				b18[b29[k]-1] = b19[b30[k]-1]
			b31 = cipher.get_state_through_sbox(j-i+1)
			b32 = cipher.get_state_through_per(b31)
			b30 = b32
		b33 = cipher.get_state_through_sbox(j)
		b34 = cipher.get_state_through_per(b33)
		b29 = b34
	with open(b16,"a") as f:
		for j in range(len(b18)):
			f.write("x%b35 = %b35\n"%(j+1,b18[j]))
		if b17 = ="AS":
			for j in range(len(b20)):
				f.write("A%b35 = %b35\n"%(j+1,b20[j]))
		elif b17 = ="DC":
			for j in range(len(b21)):
				f.write("p%b35 = %b35\n"%(j+1,b21[j]))
def fonk14(cipher,b17,b5):
	if b17 = = "AS":
		b18 = [0 for j in range (b5*cipher.var_and_num_AS["x"][0]+cipher.var_and_num_AS["x"][1])]
	elif b17 = = "DC":
		b18 = [0 for j in range (b5*cipher.var_and_num_DC["x"][0]+cipher.var_and_num_DC["x"][1])]
	shutil.copy("txt/"+cipher.b44+"/"+b17+"/optimal_solution_of_submodel/"+str(b5)+"_round_[][]_optimal_solution.txt", "result/"+cipher.b44+"/"+b17+"/")
	b22 = fonk12("txt/"+cipher.b44+"/"+b17+"/optimal_solution_of_submodel/"+str(b5)+"_round_[][]_optimal_solution.txt")
	for i in b22:
		if i[0] == "x":
			b23 = int(re.findall(b5'(-?[\b35]+)',i)[0])
			b24 = int(re.findall(b5'(-?[\b35]+)',i)[1])
			b18[b23-1] = b24
	b36 = "result/"+cipher.b44+"/"+b17+"/"+str(b5)+"_round_best_path.txt"
	with open(b36,"w") as f:
		f.write("b18 list is " + str(b18)+"\n")
	b37 = cipher.gen_input_state()
	for b5 in range (1,b5+1):
		with open(b36,"a") as f:
			f.write("\n%dth round input diff of Sbox: \n"%(b5))
		for i in range(len(b37)):
			if i%b38 = = 0:
				with open(b36,"a") as f:
					f.write(" ")
			with open(b36,"a") as f:
				f.write(str(b18[b37[i]-1]))
		b39 = cipher.get_state_through_sbox(b5)
		with open(b36,"a") as f:
			f.write("\n%dth round output diff of Sbox: \n"%(b5))
		for i in range(len(b37)):
			if i%b38 = = 0:
				with open(b36,"a") as f:
					f.write(" ")
			with open(b36,"a") as f:
				f.write(str(b18[b39[i]-1]))
		b40 = cipher.get_state_through_per(b39)
		b37 = copy.deepcopy(b40)
def fonk15(cipher,b17,b5):
	if b17 = = "AS":
		b18 = [0 for j in range (b5*cipher.var_and_num_AS["x"][0]+cipher.var_and_num_AS["x"][1])]
	elif b17 = = "DC":
		b18 = [0 for j in range (b5*cipher.var_and_num_DC["x"][0]+cipher.var_and_num_DC["x"][1])]
	shutil.copy("txt/"+cipher.b44+"/"+b17+"/optimal_solution_of_submodel/"+"/"+str(b5)+"_round_[][]_optimal_solution.txt", "result/"+cipher.b44+"/"+b17+"/")
	b22 = fonk12("txt/"+cipher.b44+"/"+b17+"/optimal_solution_of_submodel/"+"/"+str(b5)+"_round_[][]_optimal_solution.txt")
	for i in b22:
		if i[0] == "x":
			b23 = int(re.findall(b5'(-?[\b35]+)',i)[0])
			b24 = int(re.findall(b5'(-?[\b35]+)',i)[1])
			b18[b23-1] = b24
	b36 = "result/"+cipher.b44+"/"+b17+"/"+str(b5)+"_round_best_path.txt"
	with open(b36,"w") as f:
		f.write("b18 list is " + str(b18)+"\n")
	b37 = cipher.gen_input_state(b17)
	b41 = b37[0:len(b37)/b9]
	b42 = b37[len(b37)/b9:len(b37)]
	for b5 in range(1,b5+1):
		with open(b36,"a") as f:
			f.write("\n%dth round left: input diff of Sbox: \n"%(b5))
		for i in range(len(b41)):
			if i%b38 = = 0:
				with open(b36,"a") as f:
					f.write(" ")
			with open(b36,"a") as f:
				f.write(str(b18[b41[i]-1]))
		b43 = cipher.get_state_through_sbox(b17,b5)
		with open(b36,"a") as f:
			f.write("\n%dth round left: output diff of Sbox: \n"%(b5))
		for i in range(len(b43)):
			if i%b38 = = 0:
				with open(b36,"a") as f:
					f.write(" ")
			with open(b36,"a") as f:
				f.write(str(b18[b43[i]-1]))
		with open(b36,"a") as f:
			f.write("\n%dth round right: \n"%(b5))
		for i in range(len(b42)):
			if i%b38 = = 0:
				with open(b36,"a") as f:
					f.write(" ")
			with open(b36,"a") as f:
				f.write(str(b18[b42[i]-1]))
		if cipher.b44 = = "lblock":
			b42 = b41
			b45 = cipher.get_state_through_xor(b17,b5)
			b41 = b45
		elif cipher.b44 = = "twine":
			b45 = cipher.get_state_through_xor(b17,b5)
			b42 = cipher.get_state_through_per_right(b17,b41)
			b41 = cipher.get_state_through_per_left(b17,b45)