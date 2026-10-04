import os
import pandas as pd
import json
import pickle
def load_experiment_results():
    experiment_results = []
    experiments = [
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
    for exp_no, variable_list in experiments:
        for set_no in range(1, 9):
            for run in range(5):
                for variable in variable_list:
                    prefix = f"experiment_{exp_no}_{set_no}_{variable}"
                    path = os.path.join("models_data", prefix, "results", "prediction_summary.json")
                    if not os.path.exists(path):
                        print(f"File not found: {path}")
                        continue
                    with open(path, 'r') as file:
                        results = json.load(file)
                    dev_qwk = results['dev'][str(run)]['QWK']
                    holdout_qwk = results['holdout'][str(run)]['QWK']
                    experiment_results.append([exp_no, variable, set_no, run, 'dev', dev_qwk])
                    experiment_results.append([exp_no, variable, set_no, run, 'holdout', holdout_qwk])
    return experiment_results
def save_results_to_pickle(experiment_results, filename='expt_results.pkl'):
    columns = ["experiment_number", "variable", "essay_set", "run", "dev_or_holdout", "QWK"]
    df = pd.DataFrame(experiment_results, columns=columns)
    df_mean = df.groupby(["experiment_number", "variable", "essay_set", "dev_or_holdout"]).mean().reset_index()
    df_final = df_mean[["experiment_number", "variable", "essay_set", "dev_or_holdout", 'QWK']]
    with open(filename, 'wb') as f:
        pickle.dump(df_final, f)
def main():
    experiment_results = load_experiment_results()
    save_results_to_pickle(experiment_results)
if __name__ == "__main__":
    main()