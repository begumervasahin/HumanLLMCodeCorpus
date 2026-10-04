import psycopg2
import pandas as pd
import datetime
def fonk1(b7):
    b1 = 'SELECT * FROM domain_security'
    b2 = pd.read_sql_query(b1, b7)
    return b2
def fonk2(b9, from_id, to_id):
    b1 = f
    b9.execute(b1)
    return b9.fetchall()
def fonk3(b7, b3, anomaly_date):
    b1 = f
    return pd.read_sql_query(b1, b7)
def fonk4(b16, b18):
    return +1 if b16['value'].iloc[b18 + 1] > b16['value'].iloc[b18] else -1
def fonk5(b10, row, b16, b17, b18, b19, b14):
    anomaly_id, anomaly_date, b13, b3 = row
    b4 = fonk4(b16, b18)
    b5 = ', '.join(map(str, b16['value'].iloc[b18-9:b18].tolist()))
    b6 = ', '.join(map(str, b17['value'].iloc[b19-9:b19].tolist()))
    b1 = f
    b10.execute(b1)
def fonk6(from_id, to_id):
    b7 = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    b8 = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    b9 = b7.cursor()
    b10 = b8.cursor()
    b11 = fonk1(b7)
    b12 = fonk2(b9, from_id, to_id)
    a1 = 0
    for row in b12:
        anomaly_date, b3, anomaly_id, b13 = row
        b14 = int(b11[b11['b3'] == b3]['b14'].values[0])
        b15 = fonk3(b7, b3, anomaly_date.date())
        b16 = b15[b15['field'] == 'PX_LAST']
        b17 = b15[b15['field'] == 'VOLUME']
        b18 = b16.index[b16['tickdate'] == anomaly_date].tolist()[0] if not b16.index[b16['tickdate'] == anomaly_date].empty else 0
        b19 = b17.index[b17['tickdate'] == anomaly_date].tolist()[0] if not b17.index[b17['tickdate'] == anomaly_date].empty else 0
        if b18 > 10 and b18 < len(b16) - 2 and b19 > 10:
            fonk5(b10, row, b16, b17, b18, b19, b14)
        a1 += 1
        if a1 % b20 = = 0:
            b8.commit()
            print(f"{datetime.datetime.now().time()} Count: {a1}")
    b7.commit()
    b7.close()
    b8.commit()
    b8.close()
    print("DONE..........")
if b21 = = "__main__":
    fonk6(400001, 450000)