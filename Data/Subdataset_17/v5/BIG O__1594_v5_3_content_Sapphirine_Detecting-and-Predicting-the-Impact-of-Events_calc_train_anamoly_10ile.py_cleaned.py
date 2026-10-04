import psycopg2
import pandas as pd
import datetime
def fetch_data(query, conn):
    with conn.cursor() as cursor:
        cursor.execute(query)
        return pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
def process_anomalies(from_id, to_id):
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="swapnil",
        host="35.190.146.57",
        port="5432"
    )
    connw = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="swapnil",
        host="35.190.146.57",
        port="5432"
    )
    security_df = fetch_data('SELECT * FROM domain_security', conn)
    sql_anomalies = (
        f"SELECT tickdate, security, id, anamoly_score FROM tick_anomalies "
        f"WHERE id BETWEEN {from_id} AND {to_id} ORDER BY id;"
    )
    anomalies = fetch_data(sql_anomalies, conn)
    count = 0
    for row in anomalies.itertuples(index=False):
        anodate, security, anomid, anoscore = row
        security_id = int(security_df.loc[security_df['security'] == security, 'security_id'].iloc[0])
        sql_ticks = (
            f"SELECT tickdate, field, value FROM import_raw_ticks "
            f"WHERE security = '{security}' AND field IN ('PX_LAST', 'VOLUME') "
            f"AND tickdate BETWEEN to_timestamp('{anodate.date()}', 'YYYY-MM-DD') - interval '30 day' "
            f"AND to_timestamp('{anodate.date()}', 'YYYY-MM-DD') + interval '10 day' "
            f"ORDER BY field, tickdate;"
        )
        result_df = fetch_data(sql_ticks, conn)
        process_anomaly(anodate, anomid, anoscore, security, security_id, result_df, connw)
        count += 1
        if count % 1000 == 0:
            connw.commit()
            print(f"{datetime.datetime.now().time()} Count: {count}")
    conn.commit()
    conn.close()
    connw.commit()
    connw.close()
    print("DONE..........")
def process_anomaly(anodate, anomid, anoscore, security, security_id, result_df, connw):
    price_df = result_df[result_df['field'] == 'PX_LAST']
    ffidx = price_df.index[price_df['tickdate'] == anodate]
    fidx = ffidx[0] if not ffidx.empty else 0
    if 10 < fidx < len(price_df) - 2:
        label = 1 if price_df['value'].iloc[fidx + 1] > price_df['value'].iloc[fidx] else -1
        vol_df = result_df[result_df['field'] == 'VOLUME']
        vvidx = vol_df.index[vol_df['tickdate'] == anodate]
        vidx = vvidx[0] if not vvidx.empty else 0
        if vidx > 10:
            sql_insert = (
                "INSERT INTO train_tick_data VALUES ("
                f"{anomid}, '{anodate}', {anoscore}, '{security}', {security_id}, {label}, "
                f"{', '.join(map(str, price_df['value'].iloc[fidx-9:fidx+1]))}, "
                f"{', '.join(map(str, vol_df['value'].iloc[vidx-9:vidx+1]))}"
                ");"
            )
            with connw.cursor() as curw:
                curw.execute(sql_insert)
if __name__ == '__main__':
    process_anomalies(0, 200000)