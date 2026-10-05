
import pandas as pd
from sklearn.linear_model import LinearRegression
stock_market_data = {
    'Year': [2017]*12 + [2016]*12,
    'Month': list(range(12, 0, -1))*2,
    'Interest_Rate': [2.75, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.25, 2.25, 2.25, 2, 2,
                      2, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75],
    'Unemployment_Rate': [5.3]*12 + [5.9]*12,
    'Stock_Index_Price': [1464, 1394, 1357, 1293, 1256, 1254, 1234, 1195, 1159, 1167, 1130, 1075,
                          1047, 965, 943, 958, 971, 949, 884, 866, 876, 822, 704, 719]
}
df = pd.DataFrame(stock_market_data)
X = df[['Interest_Rate', 'Unemployment_Rate', 'Month']]
Y = df['Stock_Index_Price']
model = LinearRegression()
model.fit(X, Y)
print('Intercept:', model.intercept_)
print('Coefficients:', model.coef_)
new_interest_rate = 2.75
new_unemployment_rate = 5.3
predicted_price = model.predict([[new_interest_rate, new_unemployment_rate]])
print('Predicted Stock Index Price:', predicted_price)