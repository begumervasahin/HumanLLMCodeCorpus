import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import time
import datetime
def fetch_data(engine):
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
    return pd.read_sql_query(sql, engine)
def filter_pool_data(dataset, pool_id):
    return dataset[dataset.pool_id == pool_id]
def prepare_data(pool_data):
    X = pool_data.iloc[:, 1:2].values.astype(np.int64) / 10**9
    y = pool_data.iloc[:, 2].values
    return X, y
def polynomial_regression(X, y, degree=6):
    poly_reg = PolynomialFeatures(degree=degree)
    X_poly = poly_reg.fit_transform(X)
    lin_reg = LinearRegression()
    lin_reg.fit(X_poly, y)
    return poly_reg, lin_reg
def generate_future_timestamps():
    today = datetime.date.today()
    yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
    today_start_time = yesterday_end_time + 1
    return [today_start_time + i * 300 for i in range(864)]
def plot_data(X, y, t, predicted_values, title, xlabel, ylabel):
    plt.scatter(X, y, color='green')
    plt.plot(X, lin_reg.predict(poly_reg.fit_transform(X)), color='blue')
    plt.plot(t, predicted_values, color='red')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
if __name__ == "__main__":
    engine = create_engine('mysql+pymysql:
    dataset = fetch_data(engine)
    pool1 = filter_pool_data(dataset, 1)
    print(pool1)
    X, y = prepare_data(pool1)
    print(X)
    print(y)
    poly_reg, lin_reg = polynomial_regression(X, y)
    days_to_come = generate_future_timestamps()
    df = pd.DataFrame({'future3ds': days_to_come})
    t = df.values
    predicted_values = lin_reg.predict(poly_reg.fit_transform(t))
    print(predicted_values.tolist())
    plot_data(X, y, t, predicted_values, 'SGW Users Shenzhen Pool (Polynomial Regression)', 'Position Level', 'SGW Users')