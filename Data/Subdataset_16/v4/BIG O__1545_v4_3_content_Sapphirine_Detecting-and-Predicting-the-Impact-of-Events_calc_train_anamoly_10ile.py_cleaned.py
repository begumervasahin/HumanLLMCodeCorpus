import psycopg2
import pandas as pd
import datetime
def fonk1(from_id, to_id):
    b1 = psycopg2.connect(
        b2 = "postgres",
        b3 = "postgres",
        b4 = "swapnil",
        b5 = "35.190.146.57",
        b6 = "5432"
    )
    b7 = psycopg2.connect(
        b2 = "postgres",
        b3 = "postgres",
        b4 = "swapnil",
        b5 = "35.190.146.57",
        b6 = "5432"
    )
    with b1.cursor() as cursec:
        cursec.execute('SELECT * FROM domain_security')
        b8 = pd.DataFrame(cursec.fetchall(), columns=[desc[0] for desc in cursec.description])
    with b1.cursor() as cur:
        b9 = (
            f"SELECT tickdate, b13, id, anamoly_score FROM tick_anomalies "
            f"WHERE id BETWEEN {from_id} AND {to_id} ORDER BY id;"
        )
        print(b9)
        cur.execute(b9)
        b10 = cur.fetchall()
    a1 = 0
    for row in b10:
        anodate, b13, anomid, b11 = row
        b12 = int(b8[b8['b13'] == b13]['b12'].iloc[0])
        b9 = (
            f"SELECT tickdate, field, value FROM import_raw_ticks "
            f"WHERE b13 = '{b13}' AND field IN ('PX_LAST', 'VOLUME') "
            f"AND tickdate BETWEEN to_timestamp('{anodate.date()}', 'YYYY-MM-DD') - interval '30 day' "
            f"AND to_timestamp('{anodate.date()}', 'YYYY-MM-DD') + interval '10 day' "
            f"ORDER BY field, tickdate;"
        )
        with b1.cursor() as curread:
            curread.execute(b9)
            b14 = pd.DataFrame(curread.fetchall(), columns=[desc[0] for desc in curread.description])
        b15 = b14[b14['field'] == 'PX_LAST']
        b16 = b15.index[b15['tickdate'] == anodate]
        b17 = b16[0] if not b16.empty else 0
        if 10 < b17 < len(b15) - 2:
            b18 = 1 if b15['value'].iloc[b17 + 1] > b15['value'].iloc[b17] else -1
            b19 = b14[b14['field'] == 'VOLUME']
            b20 = b19.index[b19['tickdate'] == anodate]
            b21 = b20[0] if not b20.empty else 0
            if b21 > 10:
                b22 = (
                    "INSERT INTO train_tick_data VALUES ("
                    f"{anomid}, '{anodate}', {b11}, '{b13}', {b12}, {b18}, "
                    f"{', '.join(map(str, b15['value'].iloc[b17-9:b17+1]))}, "
                    f"{', '.join(map(str, b19['value'].iloc[b21-9:b21+1]))}"
                    ");"
                )
                with b7.cursor() as curw:
                    curw.execute(b22)
        a1 += 1
        if a1 % b23 = = 0:
            b7.commit()
            print(f"{datetime.datetime.now().time()} Count: {a1}")
    b1.commit()
    b1.close()
    b7.commit()
    b7.close()
    print("DONE..........")
if b24 = = '__main__':
    fonk1(0, 200000)