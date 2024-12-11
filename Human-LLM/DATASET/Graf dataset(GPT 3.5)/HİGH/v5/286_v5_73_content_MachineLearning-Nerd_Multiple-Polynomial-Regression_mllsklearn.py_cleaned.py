
import pandas as pd
from sklearn.linear_model import LinearRegression
b1 = {
    'Year': [2017]*12 + [2016]*12,
    'Month': list(range(12, 0, -1))*2,
    'Interest_Rate': [2.75, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.25, 2.25, 2.25, 2, 2,
                      2, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75],
    'Unemployment_Rate': [5.3]*12 + [5.9]*12,
    'Stock_Index_Price': [1464, 1394, 1357, 1293, 1256, 1254, 1234, 1195, 1159, 1167, 1130, 1075,
                          1047, 965, 943, 958, 971, 949, 884, 866, 876, 822, 704, 719]
}
b2 = pd.DataFrame(b1)
b3 = b2[['Interest_Rate', 'Unemployment_Rate', 'Month']]
b4 = b2['Stock_Index_Price']
b5 = LinearRegression()
b5.fit(b3, b4)
print('Intercept:', b5.intercept_)
print('Coefficients:', b5.coef_)
a1 = 2.75
a2 = 5.3
b6 = b5.predict([[a1, a2]])
print('Predicted Stock Index Price:', b6)