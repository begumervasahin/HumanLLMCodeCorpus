import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
import time
import datetime
b1 = create_engine('mysql+pymysql:
b2 = '''
SELECT pool_id,datatimestr,sum(sgwusers),sum(pgwusers)
FROM `saegw_users`,`saegw_name`
where DATEDIFF(datatimestr,NOW())<=0 AND DATEDIFF(datatimestr,NOW())>-6 and b3 = database_name and pool_id in (1,2,3,4)
GROUP BY pool_id,datatimestr
ORDER BY datatimestr
      '''
b4 = pd.read_sql_query(b2, b1)
b5 = b4[b4.pool_id==1]
b6 = b4[b4.pool_id==2]
b7 = b4[b4.pool_id==3]
b8 = b4[b4.pool_id==4]
print (b5)
b9 = b5.iloc[:,1:2].values.astype(np.int64)/ 10 ** 9
b10 = b5.iloc[:,2].values/1
print(b9)
print(b10)
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b11 = PolynomialFeatures(degree = 6)
b12 = b11.fit_transform(b9)
b11.fit(b12, b10)
b13 = LinearRegression()
b13.fit(b12, b10)
b14 = datetime.date.b14()
b15 = b14 + datetime.timedelta(days=1)
b16 = int(time.mktime(time.strptime(str(b14), '%Y-%m-%d'))) - 1
b17 = b16 + 1
print(b17)
b18 = []
for i in range(0,864):
    b18.append(b17+i*300)
b19 = pd.DataFrame({'future3ds':b18})
print(b19)
b20 = b19.values
b21 = b13.predict(b11.fit_transform(b20))
print(b21.tolist())
plt.scatter(b9, b10, b22 = 'green')
plt.plot(b9, b13.predict(b11.fit_transform(b9)), b22 = 'blue')
plt.plot(b20, b13.predict(b11.fit_transform(b20)), b22 = 'red')
plt.title('sgw users shenzhen pool(Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('sgwusers')
plt.show()