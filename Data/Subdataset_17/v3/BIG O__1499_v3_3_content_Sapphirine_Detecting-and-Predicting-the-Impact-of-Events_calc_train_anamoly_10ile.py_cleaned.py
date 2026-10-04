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
    security_df = load_security_data(conn)
    anomalies = fetch_tick_anomalies(conn, from_id, to_id)
    process_each_anomaly(conn, connw, security_df, anomalies)
    connw.commit()
    conn.close()
    connw.close()
    print("DONE..........")
def load_security_data(conn):
    with conn.cursor() as cursec:
        cursec.execute('SELECT * FROM domain_security')
        security_df = pd.DataFrame(cursec.fetchall(), columns=[desc[0] for desc in cursec.description])
    return security_df
def fetch_tick_anomalies(conn, from_id, to_id):
    sql_anomalies = f
    print(sql_anomalies)
    with conn.cursor() as cur:
        cur.execute(sql_anomalies)
        anomalies = cur.fetchall()
    return anomalies
def process_each_anomaly(conn, connw, security_df, anomalies):
    count = 0
    for anodate, security, anomid, anoscore in anomalies:
        security_id = get_security_id(security_df, security)
        result_df = fetch_tick_data(conn, security, anodate)
        if not result_df.empty:
            label = determine_label(result_df, anodate)
            if label is not None:
                values = build_values_list(anomid, anodate, anoscore, security, security_id, label, result_df)
                insert_values(connw, values)
        count += 1
        if count % 1000 == 0:
            connw.commit()
            print(f"{datetime.datetime.now().time()} - Count: {count}")
def get_security_id(security_df, security):
    return int(security_df[security_df['security'] == security]['security_id'])
def fetch_tick_data(conn, security, anodate):
    sql_ticks = f
    with conn.cursor() as curread:
        curread.execute(sql_ticks)
        result_df = pd.DataFrame(curread.fetchall(), columns=[desc[0] for desc in curread.description])
    return result_df
def determine_label(result_df, anodate):
    price_df = result_df[result_df['field'] == 'PX_LAST']
    ffidx = price_df.index[price_df['tickdate'] == anodate]
    fidx = ffidx[0] if not ffidx.empty else 0
    if fidx > 10 and fidx < len(price_df) - 2:
        return 1 if price_df['value'].iloc[fidx + 1] > price_df['value'].iloc[fidx] else -1
    return None
def build_values_list(anomid, anodate, anoscore, security, security_id, label, result_df):
    price_df = result_df[result_df['field'] == 'PX_LAST']
    vol_df = result_df[result_df['field'] == 'VOLUME']
    fidx = price_df.index[price_df['tickdate'] == anodate][0]
    vidx = vol_df.index[vol_df['tickdate'] == anodate][0]
    values = [anomid, anodate, anoscore, security, security_id, label] + \
             price_df['value'].iloc[fidx-9:fidx+1].tolist() + \
             vol_df['value'].iloc[vidx-9:vidx+1].tolist()
    return values
def insert_values(connw, values):
    sql_insert = f
    with connw.cursor() as curw:
        curw.execute(sql_insert)
if __name__ == '__main__':
    process_anomalies(0, 200000)