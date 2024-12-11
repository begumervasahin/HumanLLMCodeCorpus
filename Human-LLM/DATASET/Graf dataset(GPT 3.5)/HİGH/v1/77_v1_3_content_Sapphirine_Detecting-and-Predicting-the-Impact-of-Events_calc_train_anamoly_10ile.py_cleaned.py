import psycopg2
import pandas as pd
import time
import datetime
def fonk1(from_id, to_id):
    b1 = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    b2 = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    b3 = b1.cursor()
    b3.execute('SELECT * FROM domain_security')
    b4 = pd.DataFrame(b3.fetchall(), columns=[desc[0] for desc in b3.description])
    b5 = b1.cursor()
    b6 = b2.cursor()
    b7 = f"SELECT tickdate, b11, id, anomaly_score FROM tick_anomalies WHERE id BETWEEN {from_id} AND {to_id} ORDER BY id;"
    print(b7)
    b5.execute(b7)
    a1 = 0
    b8 = b5.fetchone()
    b7 = ''
    while b8:
        anodate, b11, anom_id, b9 = b8
        b10 = int(b4[b4['b11'] == b11]['b10'])
        b7 = "SELECT tickdate, field, value FROM import_raw_ticks " \
                   f"WHERE b11 = E'{b11}' AND field IN (E'PX_LAST', E'VOLUME') AND " \
                   f"tickdate BETWEEN to_timestamp(E'{str(anodate.date())}','YYYY-MM-DD') - INTERVAL '30 day' AND " \
                   f"to_timestamp(E'{str(anodate.date())}','YYYY-MM-DD') + INTERVAL '10 day' ORDER BY field, tickdate;"
        b12 = b1.cursor()
        b12.execute(b7)
        b13 = pd.DataFrame(b12.fetchall(), columns=[desc[0] for desc in b12.description])
        b14 = b13.loc[b13['field'] == 'PX_LAST']
        b15 = b14.index[b14['tickdate'] == anodate]
        b16 = b15[0] if b15.shape[0] > 0 else 0
        if 10 < b16 < b14.shape[0] - 2:
            b17 = +1 if b14['value'][b16 + 1] > b14['value'][b16] else -1
            b18 = b13.loc[b13['field'] == 'VOLUME']
            b19 = b18.index[b18['tickdate'] == anodate]
            b20 = b19[0] if b19.shape[0] > 0 else 0
            if b20 > 10:
                b21 = "INSERT INTO train_tick_data VALUES (" + ",".join(map(str, [anom_id, "'" + str(anodate) + "'", b9,
                                                                                         "'" + b11 + "'", b10, b17] +
                                                                       b14['value'].loc[b16 - 9:b16].tolist() +
                                                                       b18['value'].loc[b20 - 9:b20].tolist())) + ");"
                b6.execute(b21)
        b8 = b5.fetchone()
        a1 += 1
        if a1 % b22 = = 0:
            b2.commit()
            print(str(datetime.datetime.now().time()), 'Count:', a1)
    b1.commit()
    b1.close()
    b2.commit()
    b2.close()
    print("DONE..........")
fonk1(0, 200000)