import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import time
import datetime
engine = create_engine('mysql+pymysql:
sql_query = '''
SELECT pool_id, datatimestr, SUM(sgwusers) AS sgwusers, SUM(pgwusers) AS pgwusers
FROM `saegw_users`, `saegw_name`
WHERE DATEDIFF(datatimestr, NOW()) <= 0 AND DATEDIFF(datatimestr, NOW()) > -6
  AND ggsnname = database_name
  AND pool_id IN (1, 2, 3, 4)
GROUP BY pool_id, datatimestr
ORDER BY datatimestr
'''
data = pd.read_sql_query(sql_query, engine)
pool_data = {pool_id: data[data.pool_id == pool_id] for pool_id in range(1, 5)}
print(pool_data[1])
X = pool_data[1].iloc[:, 1:2].values.astype(np.int64) / 10**9
y = pool_data[1].iloc[:, 2].values
print(X)
print(y)
poly_features = PolynomialFeatures(degree=6)
X_poly = poly_features.fit_transform(X)
linear_regressor = LinearRegression()
linear_regressor.fit(X_poly, y)
today = datetime.date.today()
yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
today_start_time = yesterday_end_time + 1
print(today_start_time)
future_timestamps = [today_start_time + i * 300 for i in range(864)]
future_df = pd.DataFrame({'future_timestamps': future_timestamps})
print(future_df)
future_X = future_df.values
predicted_values = linear_regressor.predict(poly_features.fit_transform(future_X))
print(predicted_values.tolist())
plt.scatter(X, y, color='green', label='Actual Data')
plt.plot(X, linear_regressor.predict(poly_features.fit_transform(X)), color='blue', label='Polynomial Fit')
plt.plot(future_X, predicted_values, color='red', label='Predicted Values')
plt.title('SGW Users Shenzhen Pool (Polynomial Regression)')
plt.xlabel('Timestamp')
plt.ylabel('SGW Users')
plt.legend()
plt.show()