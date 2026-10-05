from gurobipy import *
import time
import copy
import function
import math
import re
class ClassModel:
    def __init__(self, cipher, model_param):
        self.cipher = cipher
        self.model_goal = model_param["model_goal"]
        self.model_round = model_param["model_round"]
        self.const_sbox = model_param["const_sbox"]
        self.const_diff = model_param["const_diff"]
        self.obj_compare = model_param["obj_compare"]
        self.model_filename = f"model/{self.cipher.name}/{self.model_goal}/{self.model_round}_round_{self.const_sbox}{self.const_diff}_model.lp"
        self.build_model()
    def build_model(self):
        self.create_objective_function()
        self.create_constraints()
        self.create_binary_variables()
        self.solve_model()
    def create_objective_function(self):
        with open(self.model_filename, "w") as f:
            f.write("Minimize\n")
        self.cipher.create_objective_function(self.model_goal, self.model_filename, 1, self.model_round)
        with open(self.model_filename, "a") as f:
            f.write("\n")
    def create_constraints(self):
        with open(self.model_filename, "a") as f:
            f.write("Subject To\n")
        self.handle_sbox_constraints()
        self.handle_difference_constraint()
        self.handle_state_constraints()
        self.create_input_non_zero_constraint()
    def handle_sbox_constraints(self):
        if self.const_sbox != []:
            if self.const_sbox == "get_upperbound_1":
                self.create_upperbound_constraint(1)
                self.const_sbox = []
            elif self.const_sbox == "get_upperbound_2":
                self.create_upperbound_constraint(2)
                self.const_sbox = []
            else:
                for r1, r2, Na in self.const_sbox:
                    if self.cipher.structure == "sp" and Na >= 2:
                        self.cipher.create_lowerbound_of_sbox_constraint(self.model_goal, self.model_filename, r1, r2, Na)
                    elif self.cipher.structure == "feistel" and Na >= 1:
                        self.cipher.create_lowerbound_of_sbox_constraint(self.model_goal, self.model_filename, r1, r2, Na)
    def handle_difference_constraint(self):
        if self.const_diff != []:
            diff_type, diff_round, diff_value = self.const_diff
            self.cipher.fix_difference_constraint(self.model_goal, self.model_filename, diff_type, diff_round, diff_value)
    def handle_state_constraints(self):
        if self.cipher.structure == "sp":
            self.create_state_constraints_sp()
        elif self.cipher.structure == "feistel":
            self.create_state_constraints_feistel()
    def create_state_constraints_sp(self):
        state = self.cipher.generate_input_state()
        for r in range(1, self.model_round + 1):
            state_through_sbox = self.cipher.get_state_through_sbox(r)
            self.cipher.diff_propagation_of_sbox_constraint(self.model_goal, self.model_filename, r, state, state_through_sbox)
            state_through_per = self.cipher.get_state_through_permutation(state_through_sbox)
            state = copy.deepcopy(state_through_per)
    def create_state_constraints_feistel(self):
        state = self.cipher.generate_input_state(self.model_goal)
        state_l, state_r = self.extract_state_parts(state)
        for r in range(1, self.model_round + 1):
            sc_state_l = self.get_state_through_sbox_feistel(r, state_l)
            if self.cipher.name == "lblock":
                ls_state_r = self.cipher.get_state_through_permutation_right(self.model_goal, state_r)
                p_state_l = self.cipher.get_state_through_permutation_left(self.model_goal, sc_state_l)
                self.cipher.diff_propagation_of_sbox_constraint(self.model_goal, self.model_filename, r, state_l, sc_state_l)
                if r < self.model_round:
                    state_r = state_l
                    xor_state = self.cipher.get_state_through_xor(self.model_goal, r)
                    self.cipher.diff_propagation_of_xor_constraint(self.model_goal, self.model_filename, r, p_state_l, ls_state_r, xor_state)
                    state_l = xor_state
            elif self.cipher.name == "twine":
                self.cipher.diff_propagation_of_sbox_constraint(self.model_goal, self.model_filename, r, state_l, sc_state_l)
                if r < self.model_round:
                    xor_state = self.cipher.get_state_through_xor(self.model_goal, r)
                    self.cipher.diff_propagation_of_xor_constraint(self.model_goal, self.model_filename, r, sc_state_l, state_r, xor_state)
                    state_r = self.cipher.get_state_through_permutation_right(self.model_goal, state_l)
                    state_l = self.cipher.get_state_through_permutation_left(self.model_goal, xor_state)
    def extract_state_parts(self, state):
        if self.model_goal == "LBAS" and self.cipher.oriented == "byte":
            state_l = state[0:len(state)
            state_r = state[len(state)
        else:
            state_l = state[0:len(state)
            state_r = state[len(state)
        return state_l, state_r
    def get_state_through_sbox_feistel(self, round_num, state):
        if self.model_goal == "LBAS" and self.cipher.oriented == "byte":
            return copy.deepcopy(state)
        else:
            return self.cipher.get_state_through_sbox(self.model_goal, round_num)
    def create_upperbound_constraint(self, order):
        filename = f"result/{self.cipher.name}/{self.model_goal}/{self.model_round-1}_round_[][]_optimal_solution.txt"
        add_num = 0 if order == 1 else self.cipher.nibble
        if self.model_goal == "AS":
            with open(filename, "r") as fr:
                for v in fr:
                    if v[0] == "A":
                        var_index, var_value = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                        with open(self.model_filename, "a") as f:
                            f.write(f"A{var_index+add_num} = {var_value}\n")
        elif self.model_goal == "DC":
            self.handle_upperbound_constraint_dc(filename, add_num)
    def handle_upperbound_constraint_dc(self, filename, add_num):
        if self.cipher.name == "present" or self.cipher.name == "rectangle" or self.cipher.name == "lblock" or self.cipher.name == "twine":
            with open(filename, "r") as fr:
                for v in fr:
                    if v[0] == "p":
                        var_index, var_value = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                        if var_index % 2 == 0:
                            with open(self.model_filename, "a") as f:
                                f.write(f"p{var_index+add_num*2} = {var_value}\n")
        elif self.cipher.name == "gift":
            self.handle_upperbound_constraint_gift(filename, add_num)
    def handle_upperbound_constraint_gift(self, filename, add_num):
        var = [0 for i in range(self.cipher.nibble*3*(self.model_round-1))]
        with open(filename, "r") as fr:
            for v in fr:
                if v[0] == "p":
                    var_index, var_value = int(re.findall(r'(-?[\d]+)', v)[0]), int(re.findall(r'(-?[\d]+)', v)[1])
                    var[var_index-1] = var_value
        for i in range(self.cipher.nibble*3*(self.model_round-1)):
            if i % 3 == 0:
                with open(self.model_filename, "a") as f:
                    f.write(f"p{i+1+add_num*3} + p{i+2+add_num*3} + p{i+3+add_num*3} = {max(var[i:i+3])}\n")
    def create_input_non_zero_constraint(self):
        indices_range = range(1, self.cipher.nibble*2) if self.model_goal == "LBAS" and self.cipher.oriented == "byte" else range(1, self.cipher.block_size)
        with open(self.model_filename, "a") as f:
            f.write("A{i} + ".join(map(str, indices_range)))
            f.write(f"A{self.cipher.nibble*2} >= 1\n" if self.model_goal == "LBAS" and self.cipher.oriented == "byte" else f"x{self.cipher.block_size} >= 1\n")
    def create_binary_variables(self):
        with open(self.model_filename, "a") as f:
            f.write("Binary\n")
        var_dict = getattr(self.cipher, f"var_and_num_{self.model_goal}")
        var_key = var_dict.keys()
        for i in var_key:
            for j in range(1, self.model_round * var_dict[i][0] + var_dict[i][1] + 1):
                with open(self.model_filename, "a") as f:
                    f.write(f"{i}{j}\n")
        with open(self.model_filename, "a") as f:
            f.write("End")
    def solve_model(self):
        time_start = time.time()
        m = read(self.model_filename)
        m.Params.MIPFocus = 2
        m.optimize()
        time_end = time.time()
        timespend = time_end - time_start
        if m.Status == 2:
            temp = int(round(m.objVal))
        elif m.Status == 3:
            temp = 25600
        if temp < self.obj_compare:
            optimal_solution_file = self.get_optimal_solution_file_path()
            self.save_optimal_solution(m, optimal_solution_file, timespend)
        function.remove_file(self.model_filename)
        return temp
    def get_optimal_solution_file_path(self):
        submodel_desc = f"{self.model_round}_round_{self.const_sbox}{self.const_diff}_optimal_solution.txt"
        if self.cipher.structure == "sp":
            return f"txt/{self.cipher.name}/{self.model_goal}/optimal_solution_of_submodel/{submodel_desc}"
        elif self.cipher.structure == "feistel":
            return f"txt/{self.cipher.name}/{self.model_goal}/optimal_solution_of_submodel/{self.model_round}_round_[][]_optimal_solution.txt"
    def save_optimal_solution(self, model, optimal_solution_file, timespend):
        with open(optimal_solution_file, "w") as f:
            f.write(f"Solving the model {self.model_filename}\n")
            f.write(f'Objective value is: {model.objVal}\n')
            f.write(f'Time taken: {timespend} seconds.\n')
            for v in model.getVars():
                f.write(f"{v.varName} = {int(round(v.x))}\n")