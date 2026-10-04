import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
from flask import Flask, jsonify, request
from itertools import product
def get_top_k_results(factor, k=10):
    factor_table = []
    for value_index, prob in enumerate(product(*[range(card) for card in factor.cardinality])):
        state = [
            factor.state_names[list(factor.variables)[i]][prob[i]]
            for i in range(len(factor.variables))
        ]
        probability = factor.values.ravel()[value_index]
        factor_table.append({'disease': state[0], 'probability': probability})
    factor_table.sort(key=lambda x: x['probability'], reverse=True)
    return factor_table[:k]
def load_data(filepath):
    return pd.read_csv(filepath)
def create_bayesian_model(data):
    root = data.columns[0]
    model = BayesianModel([[root, col] for col in data.columns[1:]])
    model.fit(data, estimator=MaximumLikelihoodEstimator)
    inference = VariableElimination(model, state_names=model.get_cpds()[0].state_names)
    return model, inference, root
def initialize_flask_app(inference, root):
    app = Flask(__name__)
    @app.route("/query")
    def query():
        evidence = {k: int(v) for k, v in request.args.items()}
        query_result = inference.query([root], evidence=evidence)
        res = query_result[root]
        res.state_names = inference.state_names
        return jsonify(get_top_k_results(res))
    return app
def main():
    data = load_data('hw4_data_long.csv')
    model, inference, root = create_bayesian_model(data)
    app = initialize_flask_app(inference, root)
    app.run(debug=True)
if __name__ == "__main__":
    main()