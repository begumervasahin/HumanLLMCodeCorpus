import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import time
import datetime
engine = create_engine('mysql+pymysql:
sql = '''
SELECT pool_id, datatimestr, SUM(sgwusers) AS sgwusers, SUM(pgwusers) AS pgwusers
FROM `saegw_users`, `saegw_name`
WHERE DATEDIFF(datatimestr, NOW()) <= 0
AND DATEDIFF(datatimestr, NOW()) > -6
AND ggsnname = database_name
AND pool_id IN (1, 2, 3, 4)
GROUP BY pool_id, datatimestr
ORDER BY datatimestr
'''
dataset = pd.read_sql_query(sql, engine)
pool1 = dataset[dataset.pool_id == 1]
pool2 = dataset[dataset.pool_id == 2]
pool3 = dataset[dataset.pool_id == 3]
pool4 = dataset[dataset.pool_id == 4]
print(pool1)
X = pool1.iloc[:, 1:2].values.astype(np.int64) / 10**9
y = pool1.iloc[:, 2].values
print(X)
print(y)
poly_reg = PolynomialFeatures(degree=6)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)
today = datetime.date.today()
yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
today_start_time = yesterday_end_time + 1
print(today_start_time)
daysToCome = [today_start_time + i * 300 for i in range(864)]
df = pd.DataFrame({'future3ds': daysToCome})
t = df.values
predicted_values = lin_reg.predict(poly_reg.fit_transform(t))
print(predicted_values.tolist())
plt.scatter(X, y, color='green')
plt.plot(X, lin_reg.predict(poly_reg.fit_transform(X)), color='blue')
plt.plot(t, lin_reg.predict(poly_reg.fit_transform(t)), color='red')
plt.title('SGW Users Shenzhen Pool (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('SGW Users')
plt.show()