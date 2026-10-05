import psycopg2
import pandas as pd
import time
import datetime
def process_anomalies(from_id, to_id):
    conn = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    connw = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    cur_sec = conn.cursor()
    cur_sec.execute('SELECT * FROM domain_security')
    security_df = pd.DataFrame(cur_sec.fetchall(), columns=[desc[0] for desc in cur_sec.description])
    cur = conn.cursor()
    curw = connw.cursor()
    sql_stmt = f"SELECT tickdate, security, id, anamoly_score FROM tick_anomalies WHERE id BETWEEN {from_id} AND {to_id} ORDER BY id;"
    print(sql_stmt)
    cur.execute(sql_stmt)
    count = 0
    row = cur.fetchone()
    sql_stmt = ''
    while row:
        anodate, security, anom_id, anoscore = row
        security_id = int(security_df[security_df['security'] == security]['security_id'])
        sql_stmt = f"SELECT tickdate, field, value FROM import_raw_ticks WHERE security=E'{security}' AND field IN (E'PX_LAST', E'VOLUME') AND " \
                   f"tickdate BETWEEN to_timestamp(E'{str(anodate.date())}','YYYY-MM-DD') - interval '30 day' AND " \
                   f"to_timestamp(E'{str(anodate.date())}','YYYY-MM-DD') + interval '+10 day' ORDER BY field, tickdate;"
        curread = conn.cursor()
        curread.execute(sql_stmt)
        result_df = pd.DataFrame(curread.fetchall(), columns=[desc[0] for desc in curread.description])
        price_df = result_df.loc[result_df['field'] == 'PX_LAST']
        ffidx = price_df.index[price_df['tickdate'] == anodate]
        fidx = ffidx[0] if ffidx.shape[0] > 0 else 0
        if fidx > 10 and fidx < price_df.shape[0]-2:
            label = +1 if price_df['value'][fidx+1] > price_df['value'][fidx] else -1
            vol_df = result_df.loc[result_df['field'] == 'VOLUME']
            vvidx = vol_df.index[vol_df['tickdate'] == anodate]
            vidx = vvidx[0] if vvidx.shape[0] > 0 else 0
            if vidx > 10:
                sql_insert = f"INSERT INTO train_tick_data VALUES ({anom_id}, '{anodate}', {anoscore}, '{security}', {security_id}, {label}, " \
                             f"{', '.join(map(lambda x: str(x), price_df['value'].loc[fidx-9:fidx].tolist() + vol_df['value'].loc[vidx-9:vidx].tolist()))});"
                curw.execute(sql_insert)
        row = cur.fetchone()
        count += 1
        if count % 1000 == 0:
            connw.commit()
            print(f"{datetime.datetime.now().time()} Count: {count}")
    conn.commit()
    conn.close()
    connw.commit()
    connw.close()
    print("DONE..........")
process_anomalies(400001, 450000)