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
        self.b7 = f"model/{self.b1.b15}/{self.b2}/{self.b3}_round_{self.b4}{self.b5}_model.lp"
        self.fonk2()
    def fonk2(self):
        self.fonk3()
        self.fonk4()
        self.fonk16()
        self.fonk17()
    def fonk3(self):
        with open(self.b7, "w") as f:
            f.write("Minimize\n")
        self.b1.fonk3(self.b2, self.b7, 1, self.b3)
        with open(self.b7, "a") as f:
            f.write("\n")
    def fonk4(self):
        with open(self.b7, "a") as f:
            f.write("Subject To\n")
        self.fonk5()
        self.fonk6()
        self.fonk7()
        self.fonk15()
    def fonk5(self):
        if self.b4 != []:
            if self.b4 = = "get_upperbound_1":
                self.fonk12(1)
                self.b4 = []
            elif self.b4 = = "get_upperbound_2":
                self.fonk12(b23)
                self.b4 = []
            else:
                for r1, r2, Na in self.b4:
                    if self.b1.b8 = = "sp" and Na >= b23:
                        self.b1.create_lowerbound_of_sbox_constraint(self.b2, self.b7, r1, r2, Na)
                    elif self.b1.b8 = = "feistel" and Na >= 1:
                        self.b1.create_lowerbound_of_sbox_constraint(self.b2, self.b7, r1, r2, Na)
    def fonk6(self):
        if self.b5 != []:
            diff_type, diff_round, b9 = self.b5
            self.b1.fix_difference_constraint(self.b2, self.b7, diff_type, diff_round, b9)
    def fonk7(self):
        if self.b1.b8 = = "sp":
            self.fonk8()
        elif self.b1.b8 = = "feistel":
            self.fonk9()
    def fonk8(self):
        b10 = self.b1.generate_input_state()
        for r in range(1, self.b3 + 1):
            b11 = self.b1.get_state_through_sbox(r)
            self.b1.diff_propagation_of_sbox_constraint(self.b2, self.b7, r, b10, b11)
            b12 = self.b1.get_state_through_permutation(b11)
            b10 = copy.deepcopy(b12)
    def fonk9(self):
        b10 = self.b1.generate_input_state(self.b2)
        b19, b13 = self.fonk10(b10)
        for r in range(1, self.b3 + 1):
            b14 = self.fonk11(r, b19)
            if self.b1.b15 = = "lblock":
                b16 = self.b1.get_state_through_permutation_right(self.b2, b13)
                b17 = self.b1.get_state_through_permutation_left(self.b2, b14)
                self.b1.diff_propagation_of_sbox_constraint(self.b2, self.b7, r, b19, b14)
                if r < self.b3:
                    b13 = b19
                    b18 = self.b1.get_state_through_xor(self.b2, r)
                    self.b1.diff_propagation_of_xor_constraint(self.b2, self.b7, r, b17, b16, b18)
                    b19 = b18
            elif self.b1.b15 = = "twine":
                self.b1.diff_propagation_of_sbox_constraint(self.b2, self.b7, r, b19, b14)
                if r < self.b3:
                    b18 = self.b1.get_state_through_xor(self.b2, r)
                    self.b1.diff_propagation_of_xor_constraint(self.b2, self.b7, r, b14, b13, b18)
                    b13 = self.b1.get_state_through_permutation_right(self.b2, b19)
                    b19 = self.b1.get_state_through_permutation_left(self.b2, b18)
    def fonk10(self, b10):
        if self.b2 = = "LBAS" and self.b1.oriented == "byte":
            b19 = b10[0:len(b10)
            b13 = b10[len(b10)
        else:
            b19 = b10[0:len(b10)
            b13 = b10[len(b10)
        return b19, b13
    def fonk11(self, round_num, b10):
        if self.b2 = = "LBAS" and self.b1.oriented == "byte":
            return copy.deepcopy(b10)
        else:
            return self.b1.get_state_through_sbox(self.b2, round_num)
    def fonk12(self, order):
        b20 = f"result/{self.b1.b15}/{self.b2}/{self.b3-1}_round_[][]_optimal_solution.txt"
        b21 = 0 if order == 1 else self.b1.nibble
        if self.b2 = = "AS":
            with open(b20, "r") as fr:
                for v in fr:
                    if v[0] == "A":
                        var_index, b22 = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                        with open(self.b7, "a") as f:
                            f.write(f"A{var_index+b21} = {b22}\n")
        elif self.b2 = = "DC":
            self.fonk13(b20, b21)
    def fonk13(self, b20, b21):
        if self.b1.b15 = = "present" or self.b1.b15 == "rectangle" or self.b1.b15 == "lblock" or self.b1.b15 == "twine":
            with open(b20, "r") as fr:
                for v in fr:
                    if v[0] == "p":
                        var_index, b22 = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                        if var_index % b23 = = 0:
                            with open(self.b7, "a") as f:
                                f.write(f"p{var_index+b21*b23} = {b22}\n")
        elif self.b1.b15 = = "gift":
            self.fonk14(b20, b21)
    def fonk14(self, b20, b21):
        b24 = [0 for i in range(self.b1.nibble*b25*(self.b3-1))]
        with open(b20, "r") as fr:
            for v in fr:
                if v[0] == "p":
                    var_index, b22 = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                    b24[var_index-1] = b22
        for i in range(self.b1.nibble*b25*(self.b3-1)):
            if i % b25 = = 0:
                with open(self.b7, "a") as f:
                    f.write(f"p{i+1+b21*b25} + p{i+b23+b21*b25} + p{i+b25+b21*b25} = {max(b24[i:i+b25])}\n")
    def fonk15(self):
        b26 = range(1, self.b1.nibble*b23) if self.b2 == "LBAS" and self.b1.oriented == "byte" else range(1, self.b1.block_size)
        with open(self.b7, "a") as f:
            f.write("A{i} + ".join(map(str, b26)))
            f.write(f"A{self.b1.nibble*b23} >= 1\n" if self.b2 = = "LBAS" and self.b1.oriented == "byte" else f"x{self.b1.block_size} >= 1\n")
    def fonk16(self):
        with open(self.b7, "a") as f:
            f.write("Binary\n")
        b27 = getattr(self.b1, f"var_and_num_{self.b2}")
        b28 = b27.keys()
        for i in b28:
            for j in range(1, self.b3 * b27[i][0] + b27[i][1] + 1):
                with open(self.b7, "a") as f:
                    f.write(f"{i}{j}\n")
        with open(self.b7, "a") as f:
            f.write("End")
    def fonk17(self):
        b29 = time.time()
        b30 = read(self.b7)
        b30.Params.a1 = b23
        b30.optimize()
        b31 = time.time()
        b32 = b31 - b29
        if b30.b33 = = b23:
            b34 = int(round(b30.objVal))
        elif b30.b33 = = b25:
            b34 = 25600
        if b34 < self.b6:
            b35 = self.fonk18()
            self.fonk19(b30, b35, b32)
        function.remove_file(self.b7)
        return b34
    def fonk18(self):
        b36 = f"{self.b3}_round_{self.b4}{self.b5}_optimal_solution.txt"
        if self.b1.b8 = = "sp":
            return f"txt/{self.b1.b15}/{self.b2}/optimal_solution_of_submodel/{b36}"
        elif self.b1.b8 = = "feistel":
            return f"txt/{self.b1.b15}/{self.b2}/optimal_solution_of_submodel/{self.b3}_round_[][]_optimal_solution.txt"
    def fonk19(self, model, b35, b32):
        with open(b35, "w") as f:
            f.write(f"Solving the model {self.b7}\n")
            f.write(f'Objective value is: {model.objVal}\n')
            f.write(f'Time taken: {b32} seconds.\n')
            for v in model.getVars():
                f.write(f"{v.varName} = {int(round(v.x))}\n")