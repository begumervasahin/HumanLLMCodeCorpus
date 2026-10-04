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
b5 = b4[b4.pool_id == 1]
b6 = b4[b4.pool_id == 2]
b7 = b4[b4.pool_id == 3]
b8 = b4[b4.pool_id == 4]
print(b5)
b9 = b5.iloc[:, 1:2].values.astype(np.int64) / 10**9
b10 = b5.iloc[:, 2].values / 1
print(b9)
print(b10)
b11 = PolynomialFeatures(degree=6)
b12 = b11.fit_transform(b9)
b11.fit(b12, b10)
b13 = LinearRegression()
b13.fit(b12, b10)
b14 = datetime.date.b14()
b15 = int(time.mktime(time.strptime(str(b14), '%Y-%m-%d'))) - 1
b16 = b15 + 1
print(b16)
b17 = [b16 + i * 300 for i in range(864)]
b18 = pd.DataFrame({'future3ds': b17})
print(b18)
b19 = b18.values
b20 = b13.predict(b11.fit_transform(b19))
print(b20.tolist())
plt.scatter(b9, b10, b21 = 'green')
plt.plot(b9, b13.predict(b11.fit_transform(b9)), b21 = 'blue')
plt.plot(b19, b13.predict(b11.fit_transform(b19)), b21 = 'red')
plt.title('SGW Users Shenzhen Pool (Polynomial Regression)')
plt.xlabel('Timestamp')
plt.ylabel('SGW Users')
plt.show()