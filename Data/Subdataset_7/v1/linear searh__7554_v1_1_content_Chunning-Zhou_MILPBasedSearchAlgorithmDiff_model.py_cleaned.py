from gurobipy import *
import time
import copy
import function
import math
import re
class class1:
    def fonk1(self, b1, model_param):
        self.b1 = b1
        self.b2 = model_param["b2"]
        self.b3 = model_param["b3"]
        self.b4 = model_param["b4"]
        self.b5 = model_param["b5"]
        self.b6 = model_param["b6"]
        self.b7 = f"model/{self.b1.b26}/{self.b2}/{self.b3}_round_{self.b4}{self.b5}_model.lp"
        self.b8 = self.fonk2()
        self.b9 = self.fonk10()
    def fonk2(self):
        self.b10 = self.fonk3()
        self.b11 = self.fonk4()
        self.b12 = self.fonk9()
    def fonk3(self):
        with open(self.b7, "w") as f:
            f.write("Minimize\n")
        self.b1.fonk3(self.b2, self.b7, 1, self.b3)
        with open(self.b7, "a") as f:
            f.write("\n")
    def fonk4(self):
        with open(self.b7, "a") as f:
            f.write("Subject To\n")
        if self.b4 != []:
            if self.b4 = = "get_upperbound_1":
                self.fonk7(1)
                self.b4 = []
            elif self.b4 = = "get_upperbound_2":
                self.fonk7(b33)
                self.b4 = []
            else:
                for i in range(len(self.b4)):
                    b13 = self.b4[i][0]
                    b14 = self.b4[i][1]
                    b15 = self.b4[i][b33]
                    if self.b1.b16 = = "sp" and b15 >= b33:
                        self.b1.lowbound_of_sbox(self.b2, self.b7, b13, b14, b15)
                    elif self.b1.b16 = = "feistel" and b15 >= 1:
                        self.b1.lowbound_of_sbox(self.b2, self.b7, b13, b14, b15)
        if self.b5 != []:
            b17 = self.b5[0]
            b18 = self.b5[1]
            b19 = self.b5[b33]
            self.b1.fix_diff(self.b2, self.b7, b17, b18, b19)
        if self.b1.b16 = = "sp":
            self.fonk5()
        elif self.b1.b16 = = "feistel":
            self.fonk6()
        self.fonk8()
    def fonk5(self):
        b20 = self.b1.gen_input_state()
        for r in range(1, self.b3 + 1):
            b21 = self.b1.get_state_through_sbox(r)
            self.b1.diff_propagation_of_sbox(self.b2, self.b7, r, b20, b21)
            b22 = self.b1.get_state_through_per(b21)
            b20 = copy.deepcopy(b22)
    def fonk6(self):
        b20 = self.b1.gen_input_state(self.b2)
        if self.b2 = = "LBAS" and self.b1.oriented == "byte":
            b23 = b20[0:len(b20)
            b24 = b20[len(b20)
        else:
            b24 = b20[0:len(b20)
            b23 = b20[len(b20)
        for r in range(1, self.b3 + 1):
            if self.b2 = = "LBAS" and self.b1.oriented == "byte":
                b25 = copy.deepcopy(b24)
            else:
                b25 = self.b1.get_state_through_sbox(self.b2, r)
            if self.b1.b26 = = "lblock":
                b27 = self.b1.get_state_through_per_right(self.b2, b23)
                b28 = self.b1.get_state_through_per_left(self.b2, b25)
                self.b1.diff_propagation_of_sbox(self.b2, self.b7, r, b24, b25)
                if r < self.b3:
                    b23 = b24
                    b29 = self.b1.get_state_through_xor(self.b2, r)
                    self.b1.diff_propagation_of_xor(self.b2, self.b7, r, b28, b27, b29)
                    b24 = b29
            elif self.b1.b26 = = "twine":
                self.b1.diff_propagation_of_sbox(self.b2, self.b7, r, b24, b25)
                if r < self.b3:
                    b29 = self.b1.get_state_through_xor(self.b2, r)
                    self.b1.diff_propagation_of_xor(self.b2, self.b7, r, b25, b23, b29)
                    b23 = self.b1.get_state_through_per_right(self.b2, b24)
                    b24 = self.b1.get_state_through_per_left(self.b2, b29)
    def fonk7(self, b31):
        b30 = f"result/{self.b1.b26}/{self.b2}/{self.b3-1}_round_[][]_optimal_solution.txt"
        if b31 = = 1:
            a1 = 0
        elif b31 = = b33:
            a1 = self.b1.nibble
        if self.b2 = = "AS":
            with open(b30, "r") as fr:
                for v in fr:
                    if v[0] == "A":
                        var_index, b32 = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                        with open(self.b7, "a") as f:
                            f.write(f"A{var_index+a1} = {b32}\n")
        elif self.b2 = = "DC":
            if self.b1.b26 = = "present" or self.b1.b26 == "rectangle" or self.b1.b26 == "lblock" or self.b1.b26 == "twine":
                with open(b30, "r") as fr:
                    for v in fr:
                        if v[0] == "p":
                            var_index, b32 = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                            if var_index % b33 = = 0:
                                with open(self.b7, "a") as f:
                                    f.write(f"p{var_index+a1*b33} = {b32}\n")
            elif self.b1.b26 = = "gift":
                b34 = [0 for i in range(self.b1.nibble*b35*(self.b3-1))]
                with open(b30, "r") as fr:
                    for v in fr:
                        if v[0] == "p":
                            var_index, b32 = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                            b34[var_index-1] = b32
                for i in range(self.b1.nibble*b35*(self.b3-1)):
                    if i % b35 = = 0:
                        with open(self.b7, "a") as f:
                            f.write(f"p{i+1+a1*b35} + p{i+b33+a1*b35} + p{i+b35+a1*b35} = {max(b34[i:i+b35])}\n")
    def fonk8(self):
        if self.b2 = = "LBAS" and self.b1.oriented == "byte":
            for i in range(1, self.b1.nibble*b33):
                with open(self.b7, "a") as f:
                    f.write(f"A{i} + ")
            with open(self.b7, "a") as f:
                f.write(f"A{self.b1.nibble*b33} >= 1\n")
        else:
            for i in range(1, self.b1.block_size):
                with open(self.b7, "a") as f:
                    f.write(f"x{i} + ")
            with open(self.b7, "a") as f:
                f.write(f"x{self.b1.block_size} >= 1\n")
    def fonk9(self):
        with open(self.b7, "a") as f:
            f.write("Binary\n")
        if self.b2 = = "LBAS":
            b36 = self.b1.var_and_num_LBAS.copy()
            b37 = self.b1.var_and_num_LBAS.keys()
        elif self.b2 = = "AS":
            b36 = self.b1.var_and_num_AS.copy()
            b37 = self.b1.var_and_num_AS.keys()
        elif self.b2 = = "DC":
            b36 = self.b1.var_and_num_DC.copy()
            b37 = self.b1.var_and_num_DC.keys()
        for i in b37:
            for j in range(1, self.b3*b36[i][0]+b36[i][1]+1):
                with open(self.b7, "a") as f:
                    f.write(f"{i}{j}\n")
        with open(self.b7, "a") as f:
            f.write("End")
    def fonk10(self):
        b38 = time.time()
        b39 = read(self.b7)
        b39.Params.a2 = b33
        b39.optimize()
        b40 = time.time()
        b41 = b40 - b38
        if b39.b42 = = b33:
            b43 = int(round(b39.objVal))
        elif b39.b42 = = b35:
            b43 = 25600
        if b43 < self.b6:
            if self.b1.b16 = = "sp":
                b44 = f"txt/{self.b1.b26}/{self.b2}/optimal_solution_of_submodel/{self.b3}_round_{self.b4}{self.b5}_optimal_solution.txt"
            elif self.b1.b16 = = "feistel":
                b44 = f"txt/{self.b1.b26}/{self.b2}/optimal_solution_of_submodel/{self.b3}_round_[][]_optimal_solution.txt"
            with open(b44, "w") as f:
                f.write(f"solving the model {self.b7}\n")
                f.write(f'obj is: {b39.objVal}\n')
                f.write(f'time is {b41} s.\n')
                for v in b39.getVars():
                    f.write(f"{v.varName} = {int(round(v.x))}\n")
        function.remove_file(self.b7)
        return b43
