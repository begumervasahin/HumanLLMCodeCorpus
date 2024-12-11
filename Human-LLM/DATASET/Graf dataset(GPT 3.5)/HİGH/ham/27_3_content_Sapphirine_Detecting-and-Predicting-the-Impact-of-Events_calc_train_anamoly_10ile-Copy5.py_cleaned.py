import psycopg2
import pandas as pd
import time
import datetime
def fonk1(fromid, toid):
  b1 = psycopg2.connect(database="postgres", user = "postgres", password = "swapnil", host = "35.190.146.57", port = "5432")
  b2 = psycopg2.connect(database="postgres", user = "postgres", password = "swapnil", host = "35.190.146.57", port = "5432")
  b3 = b1.cursor()
  b3.execute('select * from domain_security')
  b4 = pd.DataFrame(b3.fetchall(), columns=[desc[0] for desc in b3.description])
  b5 = b1.cursor()
  b6 = b2.cursor()
  b7 = "select tickdate, security, id, anamoly_score from tick_anomalies where id between " + str(fromid) + " and " + str(toid) + " order by id;"
  print b7
  b5.execute(b7)
  a1 = 0
  b8 = b5.fetchone()
  b7 = ''
  while b8:
    anodate, security, anomid, b9 = b8
    b10 = int(b4[b4['security']==security]['b10'])
    b7 = "select tickdate, field, value from import_raw_ticks "       "where security=E'" + security + "'and field IN (E'PX_LAST', E'VOLUME') and "       "tickdate between to_timestamp(E'" + str(anodate.date()) + "','YYYY-MM-DD') - interval '30 day' and to_timestamp(E'"+str(anodate.date())+"','YYYY-MM-DD') + interval '+10 day' order by field, tickdate; "
    b11 = b1.cursor()
    b11.execute(b7)
    b12 = pd.DataFrame(b11.fetchall(), columns=[desc[0] for desc in b11.description])
    b13 = b12.loc[b12['field'] == 'PX_LAST']
    b14 = b13.index[b13['tickdate']==anodate]
    b15 = b14[0] if b14.shape[0] > 0 else 0
    if b15 > 10 and b15 < b13.shape[0]-2:
      b16 = +1 if b13['value'][b15+1] > b13['value'][b15] else -1
      b17 = b12.loc[b12['field'] == 'VOLUME']
      b18 = b17.index[b17['tickdate']==anodate]
      b19 = b18[0] if b18.shape[0] > 0 else 0
      if b19 > 10:
        b20 = "insert into train_tick_data values (" + ",".join(map(lambda x: str(x),[anomid, "'"+str(anodate)+"'", b9, "'"+security+"'", b10, b16] + b13['value'].loc[b15-9:b15].tolist() + b17['value'].loc[b19-9:b19].tolist())) + ");"
        b6.execute(b20)
    b8 = b5.fetchone()
    a1 = a1 + 1
    if a1 % b21 = = 0:
      b2.commit()
      print str(datetime.datetime.now().time()), 'Count:', a1
  b1.commit()
  b1.close()
  b2.commit()
  b2.close()
  print ("DONE..........")
fonk1(400001, 450000)