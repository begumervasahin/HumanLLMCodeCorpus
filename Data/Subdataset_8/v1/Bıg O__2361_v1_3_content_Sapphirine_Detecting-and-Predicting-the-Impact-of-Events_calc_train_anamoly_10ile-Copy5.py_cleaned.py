import psycopg2
import pandas as pd
import datetime
def processAnomalies(fromid, toid):
    conn = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    connw = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    cursec = conn.cursor()
    cur = conn.cursor()
    curw = connw.cursor()
    cursec.execute('SELECT * FROM domain_security')
    securityDF = pd.DataFrame(cursec.fetchall(), columns=[desc[0] for desc in cursec.description])
    cur.execute("SELECT tickdate, security, id, anamoly_score FROM tick_anomalies WHERE id BETWEEN %s AND %s ORDER BY id;", (fromid, toid))
    count = 0
    row = cur.fetchone()
    while row:
        anodate, security, anomid, anoscore = row
        security_id = int(securityDF[securityDF['security'] == security]['security_id'])
        sql_stmt = "SELECT tickdate, field, value FROM import_raw_ticks " \
                   "WHERE security = %s AND field IN ('PX_LAST', 'VOLUME') AND " \
                   "tickdate BETWEEN %s - interval '30 day' AND %s + interval '10 day' " \
                   "ORDER BY field, tickdate;"
        curread = conn.cursor()
        curread.execute(sql_stmt, (security, anodate, anodate))
        resultDF = pd.DataFrame(curread.fetchall(), columns=[desc[0] for desc in curread.description])
        priceDF = resultDF.loc[resultDF['field'] == 'PX_LAST']
        ffidx = priceDF.index[priceDF['tickdate'] == anodate]
        fidx = ffidx[0] if ffidx.shape[0] > 0 else 0
        if 10 < fidx < priceDF.shape[0] - 2:
            label = +1 if priceDF['value'][fidx+1] > priceDF['value'][fidx] else -1
            volDF = resultDF.loc[resultDF['field'] == 'VOLUME']
            vvidx = volDF.index[volDF['tickdate'] == anodate]
            vidx = vvidx[0] if vvidx.shape[0] > 0 else 0
            if vidx > 10:
                sql_insert = "INSERT INTO train_tick_data VALUES (%s);"
                values = [anomid, anodate, anoscore, security, security_id, label] + priceDF['value'].loc[fidx-9:fidx].tolist() + volDF['value'].loc[vidx-9:vidx].tolist()
                curw.execute(sql_insert, values)
        row = cur.fetchone()
        count += 1
        if count % 1000 == 0:
            connw.commit()
            print(str(datetime.datetime.now().time()), 'Count:', count)
    conn.commit()
    conn.close()
    connw.commit()
    connw.close()
    print("DONE..........")
processAnomalies(400001, 450000)