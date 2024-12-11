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
        self.b7 = f"model/{self.b1.b21}/{self.b2}/{self.b3}_round_{self.b4}{self.b5}_model.lp"
        self.fonk2()
    def fonk2(self):
        self.fonk3()
        self.fonk4()
        self.fonk9()
        self.fonk10()
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
                self.fonk7(b28)
                self.b4 = []
            else:
                for i in range(len(self.b4)):
                    b8 = self.b4[i][0]
                    b9 = self.b4[i][1]
                    b10 = self.b4[i][b28]
                    if self.b1.b11 = = "sp" and b10 >= b28:
                        self.b1.create_lowerbound_of_sbox_constraint(self.b2, self.b7, b8, b9, b10)
                    elif self.b1.b11 = = "feistel" and b10 >= 1:
                        self.b1.create_lowerbound_of_sbox_constraint(self.b2, self.b7, b8, b9, b10)
        if self.b5 != []:
            b12 = self.b5[0]
            b13 = self.b5[1]
            b14 = self.b5[b28]
            self.b1.fix_difference_constraint(self.b2, self.b7, b12, b13, b14)
        if self.b1.b11 = = "sp":
            self.fonk5()
        elif self.b1.b11 = = "feistel":
            self.fonk6()
        self.fonk8()
    def fonk5(self):
        b15 = self.b1.generate_input_state()
        for r in range(1, self.b3 + 1):
            b16 = self.b1.get_state_through_sbox(r)
            self.b1.diff_propagation_of_sbox_constraint(self.b2, self.b7, r, b15, b16)
            b17 = self.b1.get_state_through_permutation(b16)
            b15 = copy.deepcopy(b17)
    def fonk6(self):
        b15 = self.b1.generate_input_state(self.b2)
        if self.b2 = = "LBAS" and self.b1.oriented == "byte":
            b18 = b15[0:len(b15)
            b19 = b15[len(b15)
        else:
            b19 = b15[0:len(b15)
            b18 = b15[len(b15)
        for r in range(1, self.b3 + 1):
            if self.b2 = = "LBAS" and self.b1.oriented == "byte":
                b20 = copy.deepcopy(b19)
            else:
                b20 = self.b1.get_state_through_sbox(self.b2, r)
            if self.b1.b21 = = "lblock":
                b22 = self.b1.get_state_through_permutation_right(self.b2, b18)
                b23 = self.b1.get_state_through_permutation_left(self.b2, b20)
                self.b1.diff_propagation_of_sbox_constraint(self.b2, self.b7, r, b19, b20)
                if r < self.b3:
                    b18 = b19
                    b24 = self.b1.get_state_through_xor(self.b2, r)
                    self.b1.diff_propagation_of_xor_constraint(self.b2, self.b7, r, b23, b22, b24)
                    b19 = b24
            elif self.b1.b21 = = "twine":
                self.b1.diff_propagation_of_sbox_constraint(self.b2, self.b7, r, b19, b20)
                if r < self.b3:
                    b24 = self.b1.get_state_through_xor(self.b2, r)
                    self.b1.diff_propagation_of_xor_constraint(self.b2, self.b7, r, b20, b18, b24)
                    b18 = self.b1.get_state_through_permutation_right(self.b2, b19)
                    b19 = self.b1.get_state_through_permutation_left(self.b2, b24)
    def fonk7(self, b26):
        b25 = f"result/{self.b1.b21}/{self.b2}/{self.b3-1}_round_[][]_optimal_solution.txt"
        if b26 = = 1:
            a1 = 0
        elif b26 = = b28:
            a1 = self.b1.nibble
        if self.b2 = = "AS":
            with open(b25, "r") as fr:
                for v in fr:
                    if v[0] == "A":
                        var_index, b27 = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                        with open(self.b7, "a") as f:
                            f.write(f"A{var_index+a1} = {b27}\n")
        elif self.b2 = = "DC":
            if self.b1.b21 = = "present" or self.b1.b21 == "rectangle" or self.b1.b21 == "lblock" or self.b1.b21 == "twine":
                with open(b25, "r") as fr:
                    for v in fr:
                        if v[0] == "p":
                            var_index, b27 = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                            if var_index % b28 = = 0:
                                with open(self.b7, "a") as f:
                                    f.write(f"p{var_index+a1*b28} = {b27}\n")
            elif self.b1.b21 = = "gift":
                b29 = [0 for i in range(self.b1.nibble*b30*(self.b3-1))]
                with open(b25, "r") as fr:
                    for v in fr:
                        if v[0] == "p":
                            var_index, b27 = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                            b29[var_index-1] = b27
                for i in range(self.b1.nibble*b30*(self.b3-1)):
                    if i % b30 = = 0:
                        with open(self.b7, "a") as f:
                            f.write(f"p{i+1+a1*b30} + p{i+b28+a1*b30} + p{i+b30+a1*b30} = {max(b29[i:i+b30])}\n")
    def fonk8(self):
        if self.b2 = = "LBAS" and self.b1.oriented == "byte":
            for i in range(1, self.b1.nibble*b28):
                with open(self.b7, "a") as f:
                    f.write(f"A{i} + ")
            with open(self.b7, "a") as f:
                f.write(f"A{self.b1.nibble*b28} >= 1\n")
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
            b31 = self.b1.var_and_num_LBAS.copy()
            b32 = self.b1.var_and_num_LBAS.keys()
        elif self.b2 = = "AS":
            b31 = self.b1.var_and_num_AS.copy()
            b32 = self.b1.var_and_num_AS.keys()
        elif self.b2 = = "DC":
            b31 = self.b1.var_and_num_DC.copy()
            b32 = self.b1.var_and_num_DC.keys()
        for i in b32:
            for j in range(1, self.b3*b31[i][0]+b31[i][1]+1):
                with open(self.b7, "a") as f:
                    f.write(f"{i}{j}\n")
        with open(self.b7, "a") as f:
            f.write("End")
    def fonk10(self):
        b33 = time.time()
        b34 = read(self.b7)
        b34.Params.a2 = b28
        b34.optimize()
        b35 = time.time()
        b36 = b35 - b33
        if b34.b37 = = b28:
            b38 = int(round(b34.objVal))
        elif b34.b37 = = b30:
            b38 = 25600
        if b38 < self.b6:
            if self.b1.b11 = = "sp":
                b39 = f"txt/{self.b1.b21}/{self.b2}/optimal_solution_of_submodel/{self.b3}_round_{self.b4}{self.b5}_optimal_solution.txt"
            elif self.b1.b11 = = "feistel":
                b39 = f"txt/{self.b1.b21}/{self.b2}/optimal_solution_of_submodel/{self.b3}_round_[][]_optimal_solution.txt"
            with open(b39, "w") as f:
                f.write(f"Solving the model {self.b7}\n")
                f.write(f'Objective value is: {b34.objVal}\n')
                f.write(f'Time taken: {b36} seconds.\n')
                for v in b34.getVars():
                    f.write(f"{v.varName} = {int(round(v.x))}\n")
        function.remove_file(self.b7)
        return b38
