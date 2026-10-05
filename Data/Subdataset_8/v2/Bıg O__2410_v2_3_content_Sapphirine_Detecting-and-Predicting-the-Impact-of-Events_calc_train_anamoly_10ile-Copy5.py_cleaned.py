import psycopg2
import pandas as pd
import datetime
def process_anomalies(from_id, to_id):
    conn = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    conn_write = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    cur_sec = conn.cursor()
    cur_read = conn.cursor()
    cur_write = conn_write.cursor()
    cur_sec.execute('SELECT * FROM domain_security')
    security_df = pd.DataFrame(cur_sec.fetchall(), columns=[desc[0] for desc in cur_sec.description])
    cur_read.execute("SELECT tickdate, security, id, anamoly_score FROM tick_anomalies WHERE id BETWEEN %s AND %s ORDER BY id;", (from_id, to_id))
    count = 0
    row = cur_read.fetchone()
    while row:
        anodate, security, anom_id, ano_score = row
        security_id = int(security_df[security_df['security'] == security]['security_id'])
        sql_stmt = "SELECT tickdate, field, value FROM import_raw_ticks " \
                   "WHERE security = %s AND field IN ('PX_LAST', 'VOLUME') AND " \
                   "tickdate BETWEEN %s - interval '30 day' AND %s + interval '10 day' " \
                   "ORDER BY field, tickdate;"
        cur_read_data = conn.cursor()
        cur_read_data.execute(sql_stmt, (security, anodate, anodate))
        result_df = pd.DataFrame(cur_read_data.fetchall(), columns=[desc[0] for desc in cur_read_data.description])
        price_df = result_df.loc[result_df['field'] == 'PX_LAST']
        f_idx = price_df.index[price_df['tickdate'] == anodate][0] if price_df.shape[0] > 0 else 0
        if 10 < f_idx < price_df.shape[0] - 2:
            label = +1 if price_df['value'][f_idx+1] > price_df['value'][f_idx] else -1
            vol_df = result_df.loc[result_df['field'] == 'VOLUME']
            v_idx = vol_df.index[vol_df['tickdate'] == anodate][0] if vol_df.shape[0] > 0 else 0
            if v_idx > 10:
                sql_insert = "INSERT INTO train_tick_data VALUES (%s);"
                values = [anom_id, anodate, ano_score, security, security_id, label] + price_df['value'].loc[f_idx-9:f_idx].tolist() + vol_df['value'].loc[v_idx-9:v_idx].tolist()
                cur_write.execute(sql_insert, values)
        row = cur_read.fetchone()
        count += 1
        if count % 1000 == 0:
            conn_write.commit()
            print(str(datetime.datetime.now().time()), 'Count:', count)
    conn.commit()
    conn.close()
    conn_write.commit()
    conn_write.close()
    print("DONE..........")
process_anomalies(400001, 450000)