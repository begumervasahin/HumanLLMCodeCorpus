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
        self.b7 = f"model/{self.b1.b17}/{self.b2}/{self.b3}_round_{self.b4}{self.b5}_model.lp"
        self.b8 = self.fonk2()
        self.b9 = self.fonk13()
    def fonk2(self):
        self.fonk3()
        self.fonk4()
        self.fonk12()
    def fonk3(self):
        with open(self.b7, "w") as f:
            f.write("Minimize\n")
        self.b1.fonk3(self.b2, self.b7, 1, self.b3)
        with open(self.b7, "a") as f:
            f.write("\n")
    def fonk4(self):
        with open(self.b7, "a") as f:
            f.write("Subject To\n")
        if self.b4:
            if self.b4 = = "get_upperbound_1":
                self.fonk9(1)
                self.b4 = []
            elif self.b4 = = "get_upperbound_2":
                self.fonk9(b24)
                self.b4 = []
            else:
                for r1, r2, Na in self.b4:
                    if self.b1.b10 = = "sp" and Na >= b24:
                        self.b1.lowbound_of_sbox(self.b2, self.b7, r1, r2, Na)
                    elif self.b1.b10 = = "feistel" and Na >= 1:
                        self.b1.lowbound_of_sbox(self.b2, self.b7, r1, r2, Na)
        if self.b5:
            diff_type, diff_round, b11 = self.b5
            self.b1.fix_diff(self.b2, self.b7, diff_type, diff_round, b11)
        if self.b1.b10 = = "sp":
            self.fonk5()
        elif self.b1.b10 = = "feistel":
            self.fonk6()
        self.fonk10()
    def fonk5(self):
        b12 = self.b1.gen_input_state()
        for r in range(1, self.b3 + 1):
            b13 = self.b1.get_state_through_sbox(r)
            self.b1.diff_propagation_of_sbox(self.b2, self.b7, r, b12, b13)
            b14 = self.b1.get_state_through_per(b13)
            b12 = copy.deepcopy(b14)
    def fonk6(self):
        b12 = self.b1.gen_input_state(self.b2)
        state_r, b15 = self.fonk7(b12)
        for r in range(1, self.b3 + 1):
            b16 = self.fonk8(b15, r) if self.b2 == "LBAS" and self.b1.oriented == "byte" else copy.deepcopy(b15)
            if self.b1.b17 = = "lblock":
                b18 = self.b1.get_state_through_per_right(self.b2, state_r)
                b19 = self.b1.get_state_through_per_left(self.b2, b16)
                self.b1.diff_propagation_of_sbox(self.b2, self.b7, r, b15, b16)
                if r < self.b3:
                    state_r, b20 = b15, self.b1.get_state_through_xor(self.b2, r)
                    self.b1.diff_propagation_of_xor(self.b2, self.b7, r, b19, b18, b20)
                    b15 = b20
            elif self.b1.b17 = = "twine":
                self.b1.diff_propagation_of_sbox(self.b2, self.b7, r, b15, b16)
                if r < self.b3:
                    b20 = self.b1.get_state_through_xor(self.b2, r)
                    self.b1.diff_propagation_of_xor(self.b2, self.b7, r, b16, state_r, b20)
                    state_r, b15 = self.b1.get_state_through_per_right(self.b2, b15), self.b1.get_state_through_per_left(self.b2, b20)
    def fonk7(self, b12):
        if self.b2 = = "LBAS" and self.b1.oriented == "byte":
            return b12[0:len(b12)
        return b12[0:len(b12)
    def fonk8(self, b12, round_num):
        return self.b1.get_state_through_sbox(self.b2, round_num)
    def fonk9(self, order):
        b21 = f"result/{self.b1.b17}/{self.b2}/{self.b3 - 1}_round_[][]_optimal_solution.txt"
        b22 = 0 if order == 1 else self.b1.nibble
        if self.b2 = = "AS":
            with open(b21, "r") as fr:
                for v in fr:
                    if v[0] == "A":
                        var_index, b23 = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                        with open(self.b7, "a") as f:
                            f.write(f"A{var_index + b22} = {b23}\n")
        elif self.b2 = = "DC":
            if self.b1.b17 in ["present", "rectangle", "lblock", "twine"]:
                with open(b21, "r") as fr:
                    for v in fr:
                        if v[0] == "p":
                            var_index, b23 = int(re.findall(r'(-?[\d]+)', v)[0]), int(
                                re.findall(r'(-?[\d]+)', v)[1])
                            if var_index % b24 = = 0:
                                with open(self.b7, "a") as f:
                                    f.write(f"p{var_index + b22 * b24} = {b23}\n")
            elif self.b1.b17 = = "gift":
                b25 = [0 for i in range(self.b1.nibble * b26 * (self.b3 - 1))]
                with open(b21, "r") as fr:
                    for v in fr:
                        if v[0] == "p":
                            var_index, b23 = int(re.findall(r'(-?[\d]+)', v)[0]), int(
                                re.findall(r'(-?[\d]+)', v)[1])
                            b25[var_index - 1] = b23
                    for i in range(self.b1.nibble * b26 * (self.b3 - 1)):
                        if i % b26 = = 0:
                            with open(self.b7, "a") as f:
                                f.write(f"p{i + 1 + b22 * b26} + p{i + b24 + b22 * b26} + p{i + b26 + b22 * b26} = {max(b25[i:i + b26])}\n")
    def fonk10(self):
        if self.b2 = = "LBAS" and self.b1.oriented == "byte":
            self.fonk11("A", self.b1.nibble * b24)
        else:
            self.fonk11("x", self.b1.block_size)
    def fonk11(self, prefix, end_value):
        for i in range(1, end_value):
            with open(self.b7, "a") as f:
                f.write(f"{prefix}{i} + ")
        with open(self.b7, "a") as f:
            f.write(f"{prefix}{end_value} >= 1\n")
    def fonk12(self):
        with open(self.b7, "a") as f:
            f.write("Binary\n")
        b27 = getattr(self.b1, f"var_and_num_{self.b2}").copy()
        b28 = getattr(self.b1, f"var_and_num_{self.b2}").keys()
        for i in b28:
            for j in range(1, self.b3 * b27[i][0] + b27[i][1] + 1):
                with open(self.b7, "a") as f:
                    f.write(f"{i}{j}\n")
        with open(self.b7, "a") as f:
            f.write("End")
    def fonk13(self):
        b29 = time.time()
        b30 = read(self.b7)
        b30.Params.a1 = b24
        b30.optimize()
        b31 = time.time()
        b32 = b31 - b29
        b33 = int(round(b30.objVal)) if b30.Status == b24 else 25600 if b30.Status == b26 else None
        if b33 is not None and b33 < self.b6:
            b34 = f"txt/{self.b1.b17}/{self.b2}/optimal_solution_of_submodel/{self.b3}_round_{self.b4}{self.b5}_optimal_solution.txt"
            with open(b34, "w") as f:
                f.write(f"solving the model {self.b7}\n")
                f.write(f'obj is: {b30.objVal}\n')
                f.write(f'time is {b32} s.\n')
                for v in b30.getVars():
                    f.write(f"{v.varName} = {int(round(v.x))}\n")
        function.remove_file(self.b7)
        return b33