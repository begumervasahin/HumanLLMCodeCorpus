import psycopg2
import pandas as pd
import datetime
def fonk1(from_id, to_id):
    b1 = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    b2 = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    b3 = b1.cursor()
    b4 = b2.cursor()
    b3.execute('SELECT * FROM domain_security')
    b5 = pd.DataFrame(b3.fetchall(), columns=[desc[0] for desc in b3.description])
    b3.execute(f"SELECT tickdate, security, id, anamoly_score FROM tick_anomalies WHERE id BETWEEN {from_id} AND {to_id} ORDER BY id;")
    a1 = 0
    while True:
        b6 = b3.fetchone()
        if not b6:
            break
        anodate, security, anom_id, b7 = b6
        b8 = int(b5.loc[b5['security'] == security, 'b8'])
        b9 = f"SELECT tickdate, field, value FROM import_raw_ticks WHERE security=E'{security}' AND field IN (E'PX_LAST', E'VOLUME') AND " \
                   f"tickdate BETWEEN to_timestamp(E'{str(anodate.date())}','YYYY-MM-DD') - interval '30 day' AND " \
                   f"to_timestamp(E'{str(anodate.date())}','YYYY-MM-DD') + interval '+10 day' ORDER BY field, tickdate;"
        b3.execute(b9)
        b10 = pd.DataFrame(b3.fetchall(), columns=[desc[0] for desc in b3.description])
        b11 = b10.loc[b10['field'] == 'PX_LAST']
        b12 = b11.index[b11['tickdate'] == anodate]
        b13 = b12[0] if b12.shape[0] > 0 else 0
        if 10 < b13 < b11.shape[0]-2:
            b14 = +1 if b11['value'][b13+1] > b11['value'][b13] else -1
            b15 = b10.loc[b10['field'] == 'VOLUME']
            b16 = b15.index[b15['tickdate'] == anodate]
            b17 = b16[0] if b16.shape[0] > 0 else 0
            if b17 > 10:
                b18 = f"INSERT INTO train_tick_data VALUES ({anom_id}, '{anodate}', {b7}, '{security}', {b8}, {b14}, " \
                             f"{', '.join(map(str, b11['value'].loc[b13-9:b13].tolist() + b15['value'].loc[b17-9:b17].tolist()))});"
                b4.execute(b18)
        a1 += 1
        if a1 % b19 = = 0:
            b2.commit()
            print(f"{datetime.datetime.now().time()} Count: {a1}")
    b1.commit()
    b1.close()
    b2.commit()
    b2.close()
    print("DONE..........")
fonk1(400001, 450000)