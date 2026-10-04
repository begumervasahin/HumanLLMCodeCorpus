import os
import pandas as pd
import json
import pickle
def fonk1():
    b1 = []
    b2 = [
        (1, [5, 10, 20, 30, 50, 70, 100]),
        (2, [234, 456, 789, 141516, 333]),
        (3, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]),
        (4, [2, 3, 4, 5]),
        (5, [3, 4, 5, 6]),
        (6, [3, 4, 5, 6]),
        (7, ['']),
        (8, ['']),
        (9, ['']),
        (10, ['random-normal', 'he-normal', 'xavier']),
        (11, ['']),
        (13, [''])
    ]
    for exp_no, variable_list in b2:
        for set_no in range(1, 9):
            for run in range(5):
                for variable in variable_list:
                    b3 = f"experiment_{exp_no}_{set_no}_{variable}"
                    b4 = os.b4.join("models_data", b3, "b5", "prediction_summary.json")
                    if not os.b4.exists(b4):
                        print(f"File not found: {b4}")
                        continue
                    with open(b4, 'r') as file:
                        b5 = json.load(file)
                    b6 = b5['dev'][str(run)]['QWK']
                    b7 = b5['holdout'][str(run)]['QWK']
                    b1.append([
                        exp_no, variable, set_no, run, 'dev', b6
                    ])
                    b1.append([
                        exp_no, variable, set_no, run, 'holdout', b7
                    ])
    return b1
def fonk2(b1, b8 = 'expt_results.pkl'):
    b9 = ["experiment_number", "variable", "essay_set", "run", "dev_or_holdout", "QWK"]
    b10 = pd.DataFrame(b1, b9=b9)
    b11 = b10.groupby([
        "experiment_number", "variable", "essay_set", "dev_or_holdout"
    ]).mean().reset_index()
    b12 = b11[[
        "experiment_number", "variable", "essay_set", "dev_or_holdout", 'QWK'
    ]]
    with open(b8, 'wb') as f:
        pickle.dump(b12, f)
def fonk3():
    b1 = fonk1()
    fonk2(b1)
if b13 = = "__main__":
    fonk3()