import psycopg2
import pandas as pd
import datetime
def fonk1(fromid, toid):
    b1 = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    b2 = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    b3 = b1.cursor()
    b4 = b1.cursor()
    b5 = b2.cursor()
    b3.execute('SELECT * FROM domain_security')
    b6 = pd.DataFrame(b3.fetchall(), columns=[desc[0] for desc in b3.description])
    b4.execute("SELECT tickdate, b11, id, anamoly_score FROM tick_anomalies WHERE id BETWEEN %s AND %s ORDER BY id;", (fromid, toid))
    a1 = 0
    b7 = b4.fetchone()
    while b7:
        anodate, b11, anomid, b8 = b7
        b9 = int(b6[b6['b11'] == b11]['b9'])
        b10 = "SELECT tickdate, field, value FROM import_raw_ticks " \
                   "WHERE b11 = %s AND field IN ('PX_LAST', 'VOLUME') AND " \
                   "tickdate BETWEEN %s - interval '30 day' AND %s + interval '10 day' " \
                   "ORDER BY field, tickdate;"
        b12 = b1.cursor()
        b12.execute(b10, (b11, anodate, anodate))
        b13 = pd.DataFrame(b12.fetchall(), columns=[desc[0] for desc in b12.description])
        b14 = b13.loc[b13['field'] == 'PX_LAST']
        b15 = b14.index[b14['tickdate'] == anodate]
        b16 = b15[0] if b15.shape[0] > 0 else 0
        if 10 < b16 < b14.shape[0] - 2:
            b17 = +1 if b14['value'][b16+1] > b14['value'][b16] else -1
            b18 = b13.loc[b13['field'] == 'VOLUME']
            b19 = b18.index[b18['tickdate'] == anodate]
            b20 = b19[0] if b19.shape[0] > 0 else 0
            if b20 > 10:
                b21 = "INSERT INTO train_tick_data VALUES (%s);"
                b22 = [anomid, anodate, b8, b11, b9, b17] + b14['value'].loc[b16-9:b16].tolist() + b18['value'].loc[b20-9:b20].tolist()
                b5.execute(b21, b22)
        b7 = b4.fetchone()
        a1 += 1
        if a1 % b23 = = 0:
            b2.commit()
            print(str(datetime.datetime.now().time()), 'Count:', a1)
    b1.commit()
    b1.close()
    b2.commit()
    b2.close()
    print("DONE..........")
fonk1(400001, 450000)