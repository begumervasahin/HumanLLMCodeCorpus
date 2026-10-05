import psycopg2
import pandas as pd
import datetime
def process_anomalies(from_id, to_id):
    conn = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    connw = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    cur_sec = conn.cursor()
    cur_sec.execute('SELECT * FROM domain_security')
    security_df = pd.DataFrame(cur_sec.fetchall(), columns=[desc[0] for desc in cur_sec.description])
    cur = conn.cursor()
    curw = connw.cursor()
    sql_stmt = f"SELECT tickdate, security, id, anomaly_score FROM tick_anomalies WHERE id BETWEEN {from_id} AND {to_id} ORDER BY id;"
    print(sql_stmt)
    cur.execute(sql_stmt)
    count = 0
    row = cur.fetchone()
    while row:
        anodate, security, anom_id, anom_score = row
        security_id = int(security_df[security_df['security'] == security]['security_id'])
        sql_stmt = f"SELECT tickdate, field, value FROM import_raw_ticks WHERE security = E'{security}' AND field IN (E'PX_LAST', E'VOLUME') AND " \
                   f"tickdate BETWEEN to_timestamp(E'{str(anodate.date())}','YYYY-MM-DD') - INTERVAL '30 day' AND " \
                   f"to_timestamp(E'{str(anodate.date())}','YYYY-MM-DD') + INTERVAL '10 day' ORDER BY field, tickdate;"
        curread = conn.cursor()
        curread.execute(sql_stmt)
        result_df = pd.DataFrame(curread.fetchall(), columns=[desc[0] for desc in curread.description])
        price_df = result_df.loc[result_df['field'] == 'PX_LAST']
        ff_idx = price_df.index[price_df['tickdate'] == anodate]
        f_idx = ff_idx[0] if ff_idx.shape[0] > 0 else 0
        if 10 < f_idx < price_df.shape[0] - 2:
            label = +1 if price_df['value'][f_idx + 1] > price_df['value'][f_idx] else -1
            vol_df = result_df.loc[result_df['field'] == 'VOLUME']
            vv_idx = vol_df.index[vol_df['tickdate'] == anodate]
            v_idx = vv_idx[0] if vv_idx.shape[0] > 0 else 0
            if v_idx > 10:
                values = [anom_id, str(anodate), anom_score, security, security_id, label]
                values += price_df['value'].loc[f_idx - 9:f_idx].tolist() + vol_df['value'].loc[v_idx - 9:v_idx].tolist()
                sql_insert = "INSERT INTO train_tick_data VALUES (" + ",".join(map(str, values)) + ");"
                curw.execute(sql_insert)
        row = cur.fetchone()
        count += 1
        if count % 1000 == 0:
            connw.commit()
            print(datetime.datetime.now().time(), 'Count:', count)
    conn.commit()
    conn.close()
    connw.commit()
    connw.close()
    print("DONE..........")
process_anomalies(0, 200000)