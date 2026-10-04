import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import time
import datetime
b1 = create_engine('mysql+pymysql:
b2 = '''
SELECT pool_id, datatimestr, SUM(sgwusers) AS sgwusers, SUM(pgwusers) AS pgwusers
FROM `saegw_users`, `saegw_name`
WHERE DATEDIFF(datatimestr, NOW()) <= 0 AND DATEDIFF(datatimestr, NOW()) > -6
  AND b3 = database_name
  AND pool_id IN (1, 2, 3, 4)
GROUP BY pool_id, datatimestr
ORDER BY datatimestr
'''
b4 = pd.read_sql_query(b2, b1)
b5 = {pool_id: b4[b4.pool_id == pool_id] for pool_id in range(1, 5)}
print(b5[1])
b6 = b5[1].iloc[:, 1:2].values.astype(np.int64) / 10**9
b7 = b5[1].iloc[:, 2].values
print(b6)
print(b7)
b8 = PolynomialFeatures(degree=6)
b9 = b8.fit_transform(b6)
b10 = LinearRegression()
b10.fit(b9, b7)
b11 = datetime.date.b11()
b12 = int(time.mktime(time.strptime(str(b11), '%Y-%m-%d'))) - 1
b13 = b12 + 1
print(b13)
b14 = [b13 + i * 300 for i in range(864)]
b15 = pd.DataFrame({'b14': b14})
print(b15)
b16 = b15.values
b17 = b10.predict(b8.fit_transform(b16))
print(b17.tolist())
plt.scatter(b6, b7, b18 = 'green', label='Actual Data')
plt.plot(b6, b10.predict(b8.fit_transform(b6)), b18 = 'blue', label='Polynomial Fit')
plt.plot(b16, b17, b18 = 'red', label='Predicted Values')
plt.title('SGW Users Shenzhen Pool (Polynomial Regression)')
plt.xlabel('Timestamp')
plt.ylabel('SGW Users')
plt.legend()
plt.show()