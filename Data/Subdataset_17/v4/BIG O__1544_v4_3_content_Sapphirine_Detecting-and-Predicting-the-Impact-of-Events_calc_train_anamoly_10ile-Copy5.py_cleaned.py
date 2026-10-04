import psycopg2
import pandas as pd
import time
import datetime
def process_anomalies(from_id, to_id):
    conn = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    connw = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    cursec = conn.cursor()
    cursec.execute('SELECT * FROM domain_security')
    security_df = pd.DataFrame(cursec.fetchall(), columns=[desc[0] for desc in cursec.description])
    cur = conn.cursor()
    curw = connw.cursor()
    sql_stmt = f
    print(sql_stmt)
    cur.execute(sql_stmt)
    count = 0
    row = cur.fetchone()
    while row:
        anodate, security, anomid, anoscore = row
        security_id = int(security_df[security_df['security'] == security]['security_id'])
        sql_stmt = f
        curread = conn.cursor()
        curread.execute(sql_stmt)
        result_df = pd.DataFrame(curread.fetchall(), columns=[desc[0] for desc in curread.description])
        price_df = result_df[result_df['field'] == 'PX_LAST']
        ffidx = price_df.index[price_df['tickdate'] == anodate]
        fidx = ffidx[0] if ffidx.shape[0] > 0 else 0
        if fidx > 10 and fidx < price_df.shape[0] - 2:
            label = +1 if price_df['value'][fidx + 1] > price_df['value'][fidx] else -1
            vol_df = result_df[result_df['field'] == 'VOLUME']
            vvidx = vol_df.index[vol_df['tickdate'] == anodate]
            vidx = vvidx[0] if vvidx.shape[0] > 0 else 0
            if vidx > 10:
                sql_insert = f
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