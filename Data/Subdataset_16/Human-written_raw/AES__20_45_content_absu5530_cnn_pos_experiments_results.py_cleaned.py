import os
import pandas as pd
import json
import pickle
def fonk1():
    b1 = []
    for exp_no, variable_list in zip([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13],
                                     [[5, 10, 20, 30, 50, 70, 100], [234, 456, 789, 141516, 333],
                                      [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], [2, 3, 4, 5], [3, 4, 5, 6],
                                      [3, 4, 5, 6], [''], [''], [''], ['random-normal', 'he-normal', 'xavier'], [''],
                                      ['']]):
        for set_no in range(1, 9):
            for run in range(0, 5):
                for variable in variable_list:
                    b2 = "experiment_" + str(exp_no) + "_" + str(set_no) + "_" + str(variable)
                    b3 = open(os.path.join("models_data", b2, "b4", "prediction_summary.json")).read()
                    b4 = json.loads(b3)
                    b1.append([exp_no, variable, set_no, run, 'dev', b4['dev'][str(run)]['QWK']])
                    b1.append(
                        [exp_no, variable, set_no, run, 'holdout', b4['holdout'][str(run)]['QWK']])
    return b1
b1 = fonk1()
b5 = pd.DataFrame(b1)
b5 = b5.rename(index=str,
                                                     b6 = {0: "experiment_number", 1: "variable", 2: "essay_set",
                                                              3: "run", 4: "dev_or_holdout", 5: "QWK"})
b7 = \
b5.groupby(["experiment_number", "variable", "essay_set", "dev_or_holdout"]).mean().reset_index()[
    ["experiment_number", "variable", "essay_set", "dev_or_holdout", 'QWK']]
with open('expt_results.pkl', 'wb') as f:
    pickle.dump(b7, f)