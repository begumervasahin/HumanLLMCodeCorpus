import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
from flask import Flask, jsonify, request
from itertools import product
def top_results(factor, k=10):
    factor_table = []
    value_index = 0
    for prob in product(*[range(cardinality) for cardinality in factor.cardinality]):
        state = [
            "{state}".format(state=factor.state_names[list(factor.variables)[i]][prob[i]])
            for i in range(len(factor.variables))
        ]
        probability = factor.values.ravel()[value_index]
        factor_table.append({'disease': state[0], 'probability': probability})
        value_index += 1
    factor_table.sort(key=lambda x: x['probability'], reverse=True)
    return factor_table[:k]
data = pd.read_csv('hw4_data_long.csv')
root = data.columns[0]
model = BayesianModel([[root, col] for col in data.columns[1:]])
model.fit(data, estimator=MaximumLikelihoodEstimator)
inference = VariableElimination(model)
for cpd in model.get_cpds():
    inference.state_names[cpd.variable] = cpd.state_names
app = Flask(__name__)
@app.route("/query")
def query():
    evidence = {k: int(v) for k, v in request.args.items()}
    query_result = inference.query([root], evidence=evidence)
    res = query_result[root]
    return jsonify(top_results(res))
if __name__ == "__main__":
    app.run(debug=True)