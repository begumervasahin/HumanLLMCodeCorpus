import time
import numpy as np
from b10 import class_model
from parameter import b25
import function
global b25
global b11
global b26
global b1
global b2
global b3
global b4
global b14
global b22
global b6
def fonk1():
    global b25, b26
    global b1, b2, b3, b4
    b1 = np.zeros(b26, dtype=int)
    b2 = np.zeros((b26, 2, 1 + b26, 1 + b25.num_of_diff_pattern_all), dtype=int32)
    b3 = np.zeros_like(b2, dtype=int32)
    b4 = np.zeros((b26, 2, 1 + b26, b25.num_of_diff_pattern_all), dtype=int32)
def fonk2(b13, a2, b5, DP, a1):
    global b2
    b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] = max(b2[b13 - 1, a2 - 1, b5 - 1, DP - 1], a1)
def fonk3(b13, a2, b5, DP):
    global b2
    a1 = 0
    if b5 = = 0 and DP == 0:
        for a3 in range(1, b13):
            a1 = max(a1, b2[a3 - 1, a2 - 1, -1, -1] + b2[b13 - a3 - 1, a2 - 1, -1, -1])
    elif 1 <= b5 < b13:
        if 1 < b5 < b13:
            a1 = b2[b5 - 1, a2 - 1, b5 - 1, DP - 1] + b2[b13 - b5 + 1 - 1, a2 - 1, 0, DP - 1]
        for a3 in range(1, b5):
            a1 = max(a1, b2[a3 - 1, a2 - 1, -1, -1] + b2[b13 - a3 - 1, a2 - 1, b5 - a3 - 1, DP - 1])
        for a3 in range(b5 + 1, b13):
            a1 = max(a1, b2[a3 - 1, a2 - 1, b5 - 1, DP - 1] + b2[b13 - a3 - 1, a2 - 1, -1, -1])
    elif b5 = = b13:
        for a3 in range(1, b13 - 1):
            a1 = max(a1, b2[a3 - 1, a2 - 1, -1, -1] + b2[b13 - a3 - 1, a2 - 1, b13 - a3 - 1, DP - 1])
    fonk2(b13, a2, b5, DP, a1)
def fonk4(b13, a2, b5, DP):
    global b2, b14, b22, b6
    a1 = 0
    b6 = b22[np.where(b22 == b5)[0][0] - 1]
    if b5 < b22[0]:
        a1 = function.get_value(b5, b2[b5 - 1, a2 - 1, -1, -1]) + b2[b6 - b5 - 1, a2, -1, -1] + function.get_value(
            b13 - b6, b2[b13 - b6 - 1, a2 - 1, -1, -1])
        a1 = max(a1, function.get_value(b5, b2[b5 - 1, a2 - 1, b5 - 1, DP - 1]) + b2[b6 - b5 + 1 - 1, a2, 0, DP - 1] +
                   function.get_value(b13 - b6, b2[b13 - b6 - 1, a2 - 1, -1, -1]))
    elif b5 > b22[0]:
        a1 = function.get_value(b6 - 1, b2[b6 - 2, a2 - 1, -1, -1]) + b2[b5 - 1 - b6, a2, -1, -1] + function.get_value(
            b13 - b5 + 1, b2[b13 - b5 + 1 - 1, a2 - 1, -1, -1])
        a1 = max(a1, function.get_value(b6 - 1, b2[b6 - 1 - 1, a2 - 1, -1, -1]) + b2[b5 - b6, a2, b5 - b6, DP - 1] +
                   function.get_value(b13 - b5 + 1, b2[b13 - b5 + 1 - 1, a2 - 1, 0, DP - 1]))
    if a1 >= b14:
        fonk2(b13, a2, b5, DP, a1)
def fonk5(b13, a2, b5, DP, b7, obj_compare):
    global b25, b11, b26, b2, b3, b4
    if b7 = = 'Rough':
        if b25.b8 = = "bit" and b25.branch_num_of_sbox == 2:
            return 0
        if b4[b13 - 1, a2 - 1, b5 - 1, DP - 1] == 0:
            b9 = fonk6(b11, b13, b5, DP, a2, b7, obj_compare)
            b10 = class_model(b25, b9)
            if b11 = = "AS":
                fonk2(b13, a2, b5, DP, b10.model_obj)
            elif b11 = = "DC":
                fonk2(b13, a2, b5, DP, b10.model_obj * b25.min_weight_of_sbox)
            b4[b13 - 1, a2 - 1, b5 - 1, DP - 1] = 1
            for r2 in range(b13 + 1, b26 + 1):
                if b5 = = b13:
                    fonk3(r2, a2, r2, DP)
                elif 1 <= b5 <= b13:
                    fonk3(r2, a2, b5, DP)
            with open(f"b23/{b25.name}/{b11}/solved_LBAS_model.txt", "a") as f:
                f.write(f"{b9}: {b10.model_obj}\n")
    elif b7 = = 'Tightest':
        if b3[b13 - 1, a2 - 1, b5 - 1, DP - 1] == 0:
            b9 = fonk6(b11, b13, b5, DP, a2, b7, obj_compare)
            b10 = class_model(b25, b9)
            fonk2(b13, a2, b5, DP, b10.model_obj)
            b3[b13 - 1, a2 - 1, b5 - 1, DP - 1] = 1
            for r2 in range(b13 + 1, b26 + 1):
                if b5 = = b13:
                    fonk3(r2, a2, r2, DP)
                elif 1 <= b5 <= b13:
                    fonk3(r2, a2, b5, DP)
            with open(f"b23/{b25.name}/{b11}/solved_model.txt", "a") as f:
                f.write(f"{b9}: {b10.model_obj}\n")
def fonk6(b11, b13, b5, DP, a2, b7, obj_compare):
    global b25
    if b7 = = 'Rough':
        if b5 = = b13:
            b12 = {"model_goal": "LBAS", "model_round": b13, "const_diff": ["diff_pattern_front", b13,
                                                                                   b25.diff_pattern_all[DP - 1]],
                            "const_sbox": [[1, b13 - 1, a2]], "obj_compare": 0}
        elif 1 <= b5 < b13:
            b12 = {"model_goal": "LBAS", "model_round": b13, "const_diff": ["diff_pattern_next", b5,
                                                                                   b25.diff_pattern_all[DP - 1]],
                            "const_sbox": [[1, b5 - 1, a2], [b5 + 1, b13, a2]], "obj_compare": 0}
        elif b5 = = 0 and DP == 0:
            b12 = {"model_goal": "LBAS", "model_round": b13, "const_diff": [], "const_sbox": [[1, b13, a2]],
                            "obj_compare": 0}
    elif b7 = = 'Tightest':
        if b5 = = b13:
            b12 = {"model_goal": b11, "model_round": b13, "const_diff": ["diff_pattern_front", b13,
                                                                                b25.diff_pattern_all[DP - 1]],
                            "const_sbox": [[1, b13 - 1, a2]], "obj_compare": obj_compare}
        elif 1 <= b5 < b13:
            b12 = {"model_goal": b11, "model_round": b13, "const_diff": ["diff_pattern_next", b5,
                                                                                b25.diff_pattern_all[DP - 1]],
                            "const_sbox": [[1, b5 - 1, a2], [b5 + 1, b13, a2]], "obj_compare": obj_compare}
        elif b5 = = 0 and DP == 0:
            b12 = {"model_goal": b11, "model_round": b13, "const_diff": [], "const_sbox": [[1, b13, a2]],
                            "obj_compare": obj_compare}
    return b12
def fonk7(b13):
    global b25, b11, b1, b2, b14, b22
    if b13 = = 1:
        fonk8(b13)
        fonk5(b13, 0, 0, 0, 'Tightest', 25600)
        b1[b13 - 1] = b2[b13 - 1, -1, -1, -1]
    else:
        b14 = fonk9(b13)
        fonk8(b13)
        fonk10(b13)
        fonk13(b13)
        b1[b13 - 1] = b14
    with open(f"b23/{b25.name}/{b11}/{b13}_round_search_result.txt", "a") as f:
        f.write(f"From all of above, we obtain an optimal objective value: {b1[b13 - 1]}\n")
    b2[b13 - 1] = np.maximum(b2[b13 - 1], b1[b13 - 1])
def fonk8(b13):
    global b25, b11, b26, b2
    for a2 in [0, 1]:
        fonk3(b13, a2, 0, 0)
        max_num_of_round_to_solve_lbas, b15 = b25.get_max_num_of_round_to_solve(b11)
        if b13 <= max_num_of_round_to_solve_lbas:
            fonk5(b13, a2, 0, 0, 'Rough', 0)
        if b13 <= b15 and a2 > 0:
            fonk5(b13, a2, 0, 0, 'Tightest', 0)
def fonk9(b13):
    global b25, b11
    b16 = {"model_goal": b11, "model_round": b13, "const_diff": [], "const_sbox": "get_upperbound_1",
                     "obj_compare": 25600}
    b17 = class_model(b25, b16)
    b18 = b17.model_obj
    b19 = {"model_goal": b11, "model_round": b13, "const_diff": [], "const_sbox": "get_upperbound_2",
                     "obj_compare": b18}
    b20 = class_model(b25, b19)
    b21 = b20.model_obj
    with open(f"b23/{b25.name}/{b11}/{b13}_round_search_result.txt", "a") as f:
        f.write(f"initialized b14 = min({b18}, {b21}) = {min(b18, b21)}\n")
    return min(b18, b21)
def fonk10(b13):
    global b25, b11, b2, b14, b22, b6
    b22 = function.get_search_round(b13)
    a2 = 0
    for b5 in b22:
        for DP in range(1, 1 + b25.num_of_diff_pattern_all):
            b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] = max(b2[b13 - 1, a2 - 1, b5 - 1, DP - 1], b2[b13 - 1, a2 - 1, -1, -1])
            fonk3(b13, a2, b5, DP)
            fonk4(b13, a2, b5, DP)
            if b2[b13 - 1, 0 - 1, b5 - 1, DP - 1] < b14:
                fonk11(b13, a2, b5, DP)
                if b2[b13 - 1, 0 - 1, b5 - 1, DP - 1] < b14:
                    b14 = b2[b13 - 1, -1, b5 - 1, DP - 1]
                    with open(f"b23/{b25.name}/{b11}/{b13}_round_search_result.txt", "a") as f:
                        f.write("*****************************************************************\n")
                        f.write("(*_*) We update b14 = b2[{b13},{0},{b5},{DP}] = {b2[b13 - 1, -1, b5 - 1, DP - 1]}\n")
                        f.write("*****************************************************************\n")
def fonk11(b13, a2, b5, DP):
    global b25, b11, b26, b2, b14, b22, b6
    for b7 in ['Rough', 'Tightest']:
        a3 = 2
        while a3 <= max(b5, b13 - b5 + 1) and b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] < b14:
            if b5 = = b22[0]:
                if a3 <= b13 - b5 + 1:
                    fonk5(a3, a2, 1, DP, b7, 0)
                    fonk3(b13, a2, b5, DP)
                if a3 <= b5 and b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] < b14:
                    fonk5(a3, a2, a3, DP, b7, 0)
                    fonk3(b13, a2, b5, DP)
            elif b5 < b22[0]:
                if a3 <= b5 and b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] < b14:
                    fonk5(a3, a2, a3, DP, b7, 0)
                    fonk3(b13, a2, b5, DP)
                    fonk4(b13, a2, b5, DP)
                if a3 <= b6 - b5 + 1 and b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] < b14:
                    fonk5(a3, a2 + 1, 1, DP, b7, 0)
                    fonk4(b13, a2, b5, DP)
                if a3 <= b13 - b5 + 1 and b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] < b14:
                    fonk5(a3, a2, 1, DP, b7, 0)
                    fonk3(b13, a2, b5, DP)
            elif b5 > b22[0]:
                if a3 <= b13 - b5 + 1:
                    fonk5(a3, a2, 1, DP, b7, 0)
                    fonk3(b13, a2, b5, DP)
                    fonk4(b13, a2, b5, DP)
                if a3 <= b5 - b6 + 1 and b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] < b14:
                    fonk5(a3, a2 + 1, a3, DP, b7, 0)
                    fonk4(b13, a2, b5, DP)
                if a3 <= b5 and b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] < b14:
                    fonk5(a3, a2, a3, DP, b7, 0)
                    fonk3(b13, a2, b5, DP)
            a3 = a3 + 1
        if b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] < b14:
            fonk5(b13, a2, b5, DP, b7, b14)
        if b7 = = 'Rough' and b5 != b22[0] and b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] < b14:
            fonk12(b13, a2, b5, DP)
def fonk12(b13, a2, b5, DP):
    global b25, b11, b2, b14, b22, b6
    if b25.b8 = = 'bit' and b25.branch_num_of_sbox == 2:
        return 0
    else:
        if b5 < b22[0]:
            b9 = {"model_goal": "LBAS", "model_round": b13,
                           "const_diff": ["diff_pattern_next", b5, b25.diff_pattern_all[DP - 1]],
                           "const_sbox": [[1, b5, a2], [b5 + 1, b6, a2 + 1], [b6 + 1, b13, a2]],
                           "obj_compare": 0}
        elif b5 > b22[0]:
            b9 = {"model_goal": "LBAS", "model_round": b13,
                           "const_diff": ["diff_pattern_next", b5, b25.diff_pattern_all[DP - 1]],
                           "const_sbox": [[1, b6 - 1, a2], [b6, b5 - 1, a2 + 1], [b5, b13, a2]],
                           "obj_compare": 0}
        b10 = class_model(b25, b9)
        with open(f"b23/{b25.name}/{b11}/solved_LBAS_model.txt", "a") as f:
            f.write(f"{b9}: {b10.model_obj}\n")
        if b11 = = "AS":
            b23 = b10.model_obj
        elif b11 = = "DC":
            b23 = b10.model_obj * b25.min_weight_of_sbox
        if b23 >= b14:
            b2[b13 - 1, a2 - 1, b5 - 1, DP - 1] = max(b2[b13 - 1, a2 - 1, b5 - 1, DP - 1], b14)
def fonk13(b13):
    global b26, b14
    a2 = 1
    if b2[b13 - 1, a2 - 1, -1, -1] < b14:
        for b7 in ['Rough', 'Tightest']:
            a3 = 1
            while a3 <= b13 and b2[b13 - 1, a2 - 1, -1, -1] < b14:
                fonk5(a3, a2, 0, 0, b7)
                for r2 in range(a3 + 1, b26 + 1):
                    fonk3(r2, a2, 0, 0)
                a3 = a3 + 1
        b14 = min(b14, b2[b13 - 1, a2 - 1, -1, -1])
if b24 = = "__main__":
    global b25, b11, b26, b1
    b25 = parameter.b25
    b11 = parameter.b11
    b26 = b25.get_search_round(b11)
    b27 = []
    function.gen_filefolder(b25.name, b11)
    with open(f"b23/{b25.name}/{b11}/solved_LBAS_model.txt", "w") as f:
        f.write("models we solved:\n")
    with open(f"b23/{b25.name}/{b11}/solved_model.txt", "w") as f:
        f.write("models we solved:\n")
    init_array()
    for b13 in range(1, b26 + 1):
        b28 = time.time()
        fonk7(b13)
        b29 = time.time()
        b27.append(b29 - b28)
        with open(f"b23/{b25.name}/{b11}/search_time.txt", "a") as f:
            f.write(f"search {b13} round: {b29 - b28}s.\n")
    with open(f"b23/{b25.name}/{b11}/search_time.txt", "a") as f:
        f.write(f"total time is {sum(b27)}s.\n")