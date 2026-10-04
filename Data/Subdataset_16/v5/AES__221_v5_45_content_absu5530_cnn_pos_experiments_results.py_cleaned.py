import os
import pandas as pd
import json
import pickle
def fonk1(b7, run):
    b1 = os.path.join("models_data", b7, "b2", "prediction_summary.json")
    with open(b1) as file:
        b2 = json.load(file)
        b3 = b2['dev'][str(run)]['QWK']
        b4 = b2['holdout'][str(run)]['QWK']
    return b3, b4
def fonk2():
    b5 = []
    b6 = [
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
    for exp_no, variable_list in b6:
        for set_no in range(1, 9):
            for run in range(5):
                for variable in variable_list:
                    b7 = f"experiment_{exp_no}_{set_no}_{variable}"
                    b3, b4 = fonk1(b7, run)
                    b5.append([exp_no, variable, set_no, run, 'dev', b3])
                    b5.append([exp_no, variable, set_no, run, 'holdout', b4])
    return b5
def fonk3(b5):
    b8 = pd.DataFrame(b5, columns=[
        "experiment_number", "variable", "essay_set", "run", "dev_or_holdout", "QWK"
    ])
    b9 = b8.groupby(
        ["experiment_number", "variable", "essay_set", "dev_or_holdout"]
    ).mean().reset_index()
    with open('expt_results.pkl', 'wb') as file:
        pickle.dump(b9, file)
if b10 = = "__main__":
    b5 = fonk2()
    fonk3(b5)