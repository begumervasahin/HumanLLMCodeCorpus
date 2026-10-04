import psycopg2
import pandas as pd
import time
import datetime
def processAnomalies(fromid, toid):
  conn = psycopg2.connect(database="postgres", user = "postgres", password = "swapnil", host = "35.190.146.57", port = "5432")
  connw = psycopg2.connect(database="postgres", user = "postgres", password = "swapnil", host = "35.190.146.57", port = "5432")
  cursec = conn.cursor()
  cursec.execute('select * from domain_security')
  securityDF = pd.DataFrame(cursec.fetchall(), columns=[desc[0] for desc in cursec.description])
  cur = conn.cursor()
  curw = connw.cursor()
  sql_stmt = "select tickdate, security, id, anamoly_score from tick_anomalies where id between " + str(fromid) + " and " + str(toid) + " order by id;"
  print sql_stmt
  cur.execute(sql_stmt)
  count = 0
  row = cur.fetchone()
  sql_stmt = ''
  while row:
    anodate, security, anomid, anoscore = row
    security_id = int(securityDF[securityDF['security']==security]['security_id'])
    sql_stmt = "select tickdate, field, value from import_raw_ticks "       "where security=E'" + security + "'and field IN (E'PX_LAST', E'VOLUME') and "       "tickdate between to_timestamp(E'" + str(anodate.date()) + "','YYYY-MM-DD') - interval '30 day' and to_timestamp(E'"+str(anodate.date())+"','YYYY-MM-DD') + interval '+10 day' order by field, tickdate; "
    curread = conn.cursor()
    curread.execute(sql_stmt)
    resultDF = pd.DataFrame(curread.fetchall(), columns=[desc[0] for desc in curread.description])
    priceDF = resultDF.loc[resultDF['field'] == 'PX_LAST']
    ffidx = priceDF.index[priceDF['tickdate']==anodate]
    fidx = ffidx[0] if ffidx.shape[0] > 0 else 0
    if fidx > 10 and fidx < priceDF.shape[0]-2:
      label = +1 if priceDF['value'][fidx+1] > priceDF['value'][fidx] else -1
      volDF = resultDF.loc[resultDF['field'] == 'VOLUME']
      vvidx = volDF.index[volDF['tickdate']==anodate]
      vidx = vvidx[0] if vvidx.shape[0] > 0 else 0
      if vidx > 10:
        sql_insert = "insert into train_tick_data values (" + ",".join(map(lambda x: str(x),[anomid, "'"+str(anodate)+"'", anoscore, "'"+security+"'", security_id, label] + priceDF['value'].loc[fidx-9:fidx].tolist() + volDF['value'].loc[vidx-9:vidx].tolist())) + ");"
        curw.execute(sql_insert)
    row = cur.fetchone()
    count = count + 1
    if count % 1000 == 0:
      connw.commit()
      print str(datetime.datetime.now().time()), 'Count:', count
  conn.commit()
  conn.close()
  connw.commit()
  connw.close()
  print ("DONE..........")
processAnomalies(400001, 450000)