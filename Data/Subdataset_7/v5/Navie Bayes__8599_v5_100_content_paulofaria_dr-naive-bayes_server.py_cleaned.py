import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.b10 import VariableElimination
from flask import Flask, jsonify, request
def fonk1(factor, b1 = 10):
    from itertools import product
    b2 = []
    for prob in product(*[range(cardinality) for cardinality in factor.cardinality]):
        b3 = [factor.b15[var][val] for var, val in zip(factor.variables, prob)]
        b4 = factor.values.ravel()[sum(val * factor.cardinality[i] for i, val in enumerate(prob))]
        b2.append({'disease': b3[0], 'b4': b4})
    b2.sort(b5 = lambda x: x['b4'], reverse=True)
    return b2[:b1]
b6 = pd.read_csv('hw4_data_long.csv')
b7 = list(b6)[0]
b8 = BayesianModel([[b7, col] for col in list(b6)[1:]])
b8.fit(b6, b9 = MaximumLikelihoodEstimator)
b10 = VariableElimination(b8, b15=b8.get_cpds()[0].b15)
b11 = Flask(__name__)
@b11.route("/query")
def fonk2():
    b12 = {b1: int(v) for b1, v in request.args.items()}
    b13 = b10.fonk2([b7], b12=b12)
    b14 = b13[b7]
    b14.b15 = b10.b15
    return jsonify(fonk1(b14)))