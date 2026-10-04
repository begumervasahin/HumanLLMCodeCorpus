import psycopg2
import pandas as pd
import datetime
def process_anomalies(from_id, to_id):
    db_params = {
        "database": "postgres",
        "user": "postgres",
        "password": "swapnil",
        "host": "35.190.146.57",
        "port": "5432"
    }
    conn = psycopg2.connect(**db_params)
    connw = psycopg2.connect(**db_params)
    with conn.cursor() as cursec:
        cursec.execute('SELECT * FROM domain_security')
        security_df = pd.DataFrame(cursec.fetchall(), columns=[desc[0] for desc in cursec.description])
    sql_anomalies = f
    print(sql_anomalies)
    with conn.cursor() as cur:
        cur.execute(sql_anomalies)
        anomalies = cur.fetchall()
    count = 0
    for anodate, security, anomid, anoscore in anomalies:
        security_id = int(security_df[security_df['security'] == security]['security_id'])
        sql_ticks = f
        with conn.cursor() as curread:
            curread.execute(sql_ticks)
            result_df = pd.DataFrame(curread.fetchall(), columns=[desc[0] for desc in curread.description])
        price_df = result_df[result_df['field'] == 'PX_LAST']
        ffidx = price_df.index[price_df['tickdate'] == anodate]
        fidx = ffidx[0] if not ffidx.empty else 0
        if fidx > 10 and fidx < len(price_df) - 2:
            label = 1 if price_df['value'].iloc[fidx + 1] > price_df['value'].iloc[fidx] else -1
            vol_df = result_df[result_df['field'] == 'VOLUME']
            vvidx = vol_df.index[vol_df['tickdate'] == anodate]
            vidx = vvidx[0] if not vvidx.empty else 0
            if vidx > 10:
                values = [anomid, anodate, anoscore, security, security_id, label] + \
                         price_df['value'].iloc[fidx-9:fidx+1].tolist() + \
                         vol_df['value'].iloc[vidx-9:vidx+1].tolist()
                sql_insert = f
                with connw.cursor() as curw:
                    curw.execute(sql_insert)
        count += 1
        if count % 1000 == 0:
            connw.commit()
            print(f"{datetime.datetime.now().time()} - Count: {count}")
    connw.commit()
    conn.close()
    connw.close()
    print("DONE..........")
if __name__ == '__main__':
    process_anomalies(0, 200000)