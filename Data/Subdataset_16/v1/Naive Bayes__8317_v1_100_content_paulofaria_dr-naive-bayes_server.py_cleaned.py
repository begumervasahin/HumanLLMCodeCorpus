import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.b10 import VariableElimination
from flask import Flask, jsonify, request
def fonk1(factor, b1 = 10):
    from itertools import product
    b2 = []
    a1 = 0
    for prob in product(*[range(cardinality) for cardinality in factor.cardinality]):
        b3 = [
            "{b3}".format(b3 = factor.b15[list(factor.variables)[i]][prob[i]])
            for i in range(len(factor.variables))
        ]
        b4 = factor.values.ravel()[a1]
        b2.append({'disease': b3[0], 'b4': b4})
        a1 += 1
    b2.sort(b5 = lambda x: x['b4'], reverse=True)
    return b2[:b1]
b6 = pd.read_csv('hw4_data_long.csv')
b7 = b6.columns[0]
b8 = BayesianModel([[b7, col] for col in b6.columns[1:]])
b8.fit(b6, b9 = MaximumLikelihoodEstimator)
b10 = VariableElimination(b8, b15=b8.get_cpds()[0].b15)
b11 = Flask(b16)
@b11.route("/b13")
def fonk2():
    b12 = {b1: int(v) for b1, v in request.args.items()}
    b13 = b10.fonk2([b7], b12=b12)
    b14 = b13[b7]
    b14.b15 = b10.b15
    return jsonify(fonk1(b14))
if b16 = = "__main__":
    b11.run(b17 = True)