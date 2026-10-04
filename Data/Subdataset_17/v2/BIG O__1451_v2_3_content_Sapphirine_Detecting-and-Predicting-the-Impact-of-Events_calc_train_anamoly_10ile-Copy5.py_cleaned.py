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
    with conn.cursor() as cur_sec:
        cur_sec.execute('SELECT * FROM domain_security')
        security_df = pd.DataFrame(cur_sec.fetchall(), columns=[desc[0] for desc in cur_sec.description])
    with conn.cursor() as cur, connw.cursor() as curw:
        sql_stmt = f
        print(sql_stmt)
        cur.execute(sql_stmt)
        count = 0
        row = cur.fetchone()
        while row:
            anodate, security, anomid, anoscore = row
            security_id = int(security_df.loc[security_df['security'] == security, 'security_id'].iloc[0])
            sql_stmt = f
            cur_read = conn.cursor()
            cur_read.execute(sql_stmt)
            result_df = pd.DataFrame(cur_read.fetchall(), columns=[desc[0] for desc in cur_read.description])
            price_df = result_df[result_df['field'] == 'PX_LAST']
            ffidx = price_df.index[price_df['tickdate'] == anodate]
            fidx = ffidx[0] if not ffidx.empty else 0
            if 10 < fidx < price_df.shape[0] - 2:
                label = 1 if price_df['value'].iloc[fidx + 1] > price_df['value'].iloc[fidx] else -1
                vol_df = result_df[result_df['field'] == 'VOLUME']
                vvidx = vol_df.index[vol_df['tickdate'] == anodate]
                vidx = vvidx[0] if not vvidx.empty else 0
                if vidx > 10:
                    sql_insert = f
                    curw.execute(sql_insert)
            row = cur.fetchone()
            count += 1
            if count % 1000 == 0:
                connw.commit()
                print(f"{datetime.datetime.now().time()} Count: {count}")
        connw.commit()
    conn.close()
    connw.close()
    print("DONE..........")
if __name__ == "__main__":
    process_anomalies(400001, 450000)