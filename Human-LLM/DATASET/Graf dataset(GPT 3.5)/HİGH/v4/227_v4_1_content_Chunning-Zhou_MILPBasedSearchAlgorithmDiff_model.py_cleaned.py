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
        self.b7 = f"model/{self.b1.b22}/{self.b2}/{self.b3}_round_{self.b4}{self.b5}_model.lp"
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
                self.fonk7(b29)
                self.b4 = []
            else:
                for i in range(len(self.b4)):
                    r1, r2, b13 = self.b4[i]
                    if self.b1.b14 = = "sp" and b13 >= b29:
                        self.b1.lowbound_of_sbox(self.b2, self.b7, r1, r2, b13)
                    elif self.b1.b14 = = "feistel" and b13 >= 1:
                        self.b1.lowbound_of_sbox(self.b2, self.b7, r1, r2, b13)
        if self.b5 != []:
            diff_type, diff_round, b15 = self.b5
            self.b1.fix_diff(self.b2, self.b7, diff_type, diff_round, b15)
        if self.b1.b14 = = "sp":
            self.fonk5()
        elif self.b1.b14 = = "feistel":
            self.fonk6()
        self.fonk8()
    def fonk5(self):
        b16 = self.b1.gen_input_state()
        for r in range(1, self.b3 + 1):
            b17 = self.b1.get_state_through_sbox(r)
            self.b1.diff_propagation_of_sbox(self.b2, self.b7, r, b16, b17)
            b18 = self.b1.get_state_through_per(b17)
            b16 = copy.deepcopy(b18)
    def fonk6(self):
        b16 = self.b1.gen_input_state(self.b2)
        if self.b2 = = "LBAS" and self.b1.oriented == "byte":
            b19 = b16[0:len(b16)
            b20 = b16[len(b16)
        else:
            b20 = b16[0:len(b16)
            b19 = b16[len(b16)
        for r in range(1, self.b3 + 1):
            if self.b2 = = "LBAS" and self.b1.oriented == "byte":
                b21 = copy.deepcopy(b20)
            else:
                b21 = self.b1.get_state_through_sbox(self.b2, r)
            if self.b1.b22 = = "lblock":
                b23 = self.b1.get_state_through_per_right(self.b2, b19)
                b24 = self.b1.get_state_through_per_left(self.b2, b21)
                self.b1.diff_propagation_of_sbox(self.b2, self.b7, r, b20, b21)
                if r < self.b3:
                    b19 = b20
                    b25 = self.b1.get_state_through_xor(self.b2, r)
                    self.b1.diff_propagation_of_xor(self.b2, self.b7, r, b24, b23, b25)
                    b20 = b25
            elif self.b1.b22 = = "twine":
                self.b1.diff_propagation_of_sbox(self.b2, self.b7, r, b20, b21)
                if r < self.b3:
                    b25 = self.b1.get_state_through_xor(self.b2, r)
                    self.b1.diff_propagation_of_xor(self.b2, self.b7, r, b21, b19, b25)
                    b19 = self.b1.get_state_through_per_right(self.b2, b20)
                    b20 = self.b1.get_state_through_per_left(self.b2, b25)
    def fonk7(self, b27):
        b26 = f"result/{self.b1.b22}/{self.b2}/{self.b3 - 1}_round_[][]_optimal_solution.txt"
        if b27 = = 1:
            a1 = 0
        elif b27 = = b29:
            a1 = self.b1.nibble
        if self.b2 = = "AS":
            with open(b26, "r") as fr:
                for v in fr:
                    if v[0] == "A":
                        var_index, b28 = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                        with open(self.b7, "a") as f:
                            f.write(f"A{var_index + a1} = {b28}\n")
        elif self.b2 = = "DC":
            if self.b1.b22 in ["present", "rectangle", "lblock", "twine"]:
                with open(b26, "r") as fr:
                    for v in fr:
                        if v[0] == "p":
                            var_index, b28 = int(re.findall(r'(-?[\d]+)', v)[0]), int(
                                re.findall(r'(-?[\d]+)', v)[1])
                            if var_index % b29 = = 0:
                                with open(self.b7, "a") as f:
                                    f.write(f"p{var_index + a1 * b29} = {b28}\n")
            elif self.b1.b22 = = "gift":
                b30 = [0 for i in range(self.b1.nibble * b31 * (self.b3 - 1))]
                with open(b26, "r") as fr:
                    for v in fr:
                        if v[0] == "p":
                            var_index, b28 = int(re.findall(r'(-?[\d]+)', v)[0]), int(
                                re.findall(r'(-?[\d]+)', v)[1])
                            b30[var_index - 1] = b28
                    for i in range(self.b1.nibble * b31 * (self.b3 - 1)):
                        if i % b31 = = 0:
                            with open(self.b7, "a") as f:
                                f.write(f"p{i + 1 + a1 * b31} + p{i + b29 + a1 * b31} + p{i + b31 + a1 * b31} = {max(b30[i:i + b31])}\n")
    def fonk8(self):
        if self.b2 = = "LBAS" and self.b1.oriented == "byte":
            for i in range(1, self.b1.nibble * b29):
                with open(self.b7, "a") as f:
                    f.write(f"A{i} + ")
            with open(self.b7, "a") as f:
                f.write(f"A{self.b1.nibble * b29} >= 1\n")
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
            b32 = self.b1.var_and_num_LBAS.copy()
            b33 = self.b1.var_and_num_LBAS.keys()
        elif self.b2 = = "AS":
            b32 = self.b1.var_and_num_AS.copy()
            b33 = self.b1.var_and_num_AS.keys()
        elif self.b2 = = "DC":
            b32 = self.b1.var_and_num_DC.copy()
            b33 = self.b1.var_and_num_DC.keys()
        for i in b33:
            for j in range(1, self.b3 * b32[i][0] + b32[i][1] + 1):
                with open(self.b7, "a") as f:
                    f.write(f"{i}{j}\n")
        with open(self.b7, "a") as f:
            f.write("End")
    def fonk10(self):
        b34 = time.time()
        b35 = read(self.b7)
        b35.Params.a2 = b29
        b35.optimize()
        b36 = time.time()
        b37 = b36 - b34
        if b35.b38 = = b29:
            b39 = int(round(b35.objVal))
        elif b35.b38 = = b31:
            b39 = 25600
        if b39 < self.b6:
            if self.b1.b14 = = "sp":
                b40 = f"txt/{self.b1.b22}/{self.b2}/optimal_solution_of_submodel/{self.b3}_round_{self.b4}{self.b5}_optimal_solution.txt"
            elif self.b1.b14 = = "feistel":
                b40 = f"txt/{self.b1.b22}/{self.b2}/optimal_solution_of_submodel/{self.b3}_round_[][]_optimal_solution.txt"
            with open(b40, "w") as f:
                f.write(f"solving the model {self.b7}\n")
                f.write(f'obj is: {b35.objVal}\n')
                f.write(f'time is {b37} s.\n')
                for v in b35.getVars():
                    f.write(f"{v.varName} = {int(round(v.x))}\n")
        function.remove_file(self.b7)
        return b39