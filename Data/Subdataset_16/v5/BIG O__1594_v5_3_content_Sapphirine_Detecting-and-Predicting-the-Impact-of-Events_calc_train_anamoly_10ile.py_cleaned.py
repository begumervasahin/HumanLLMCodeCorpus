import psycopg2
import pandas as pd
import datetime
def fonk1(query, b2):
    with b2.cursor() as cursor:
        cursor.execute(query)
        return pd.DataFrame(cursor.fetchall(), b1 = [desc[0] for desc in cursor.description])
def fonk2(from_id, to_id):
    b2 = psycopg2.connect(
        b3 = "postgres",
        b4 = "postgres",
        b5 = "swapnil",
        b6 = "35.190.146.57",
        b7 = "5432"
    )
    b8 = psycopg2.connect(
        b3 = "postgres",
        b4 = "postgres",
        b5 = "swapnil",
        b6 = "35.190.146.57",
        b7 = "5432"
    )
    b9 = fonk1('SELECT * FROM domain_security', b2)
    b10 = (
        f"SELECT tickdate, b16, id, anamoly_score FROM tick_anomalies "
        f"WHERE id BETWEEN {from_id} AND {to_id} ORDER BY id;"
    )
    b11 = fonk1(b10, b2)
    a1 = 0
    for row in b11.itertuples(b12 = False):
        anodate, b16, anomid, b13 = row
        b14 = int(b9.loc[b9['b16'] == b16, 'b14'].iloc[0])
        b15 = (
            f"SELECT tickdate, field, value FROM import_raw_ticks "
            f"WHERE b16 = '{b16}' AND field IN ('PX_LAST', 'VOLUME') "
            f"AND tickdate BETWEEN to_timestamp('{anodate.date()}', 'YYYY-MM-DD') - interval '30 day' "
            f"AND to_timestamp('{anodate.date()}', 'YYYY-MM-DD') + interval '10 day' "
            f"ORDER BY field, tickdate;"
        )
        b17 = fonk1(b15, b2)
        fonk3(anodate, anomid, b13, b16, b14, b17, b8)
        a1 += 1
        if a1 % b18 = = 0:
            b8.commit()
            print(f"{datetime.datetime.now().time()} Count: {a1}")
    b2.commit()
    b2.close()
    b8.commit()
    b8.close()
    print("DONE..........")
def fonk3(anodate, anomid, b13, b16, b14, b17, b8):
    b19 = b17[b17['field'] == 'PX_LAST']
    b20 = b19.b12[b19['tickdate'] == anodate]
    b21 = b20[0] if not b20.empty else 0
    if 10 < b21 < len(b19) - 2:
        b22 = 1 if b19['value'].iloc[b21 + 1] > b19['value'].iloc[b21] else -1
        b23 = b17[b17['field'] == 'VOLUME']
        b24 = b23.b12[b23['tickdate'] == anodate]
        b25 = b24[0] if not b24.empty else 0
        if b25 > 10:
            b26 = (
                "INSERT INTO train_tick_data VALUES ("
                f"{anomid}, '{anodate}', {b13}, '{b16}', {b14}, {b22}, "
                f"{', '.join(map(str, b19['value'].iloc[b21-9:b21+1]))}, "
                f"{', '.join(map(str, b23['value'].iloc[b25-9:b25+1]))}"
                ");"
            )
            with b8.cursor() as curw:
                curw.execute(b26)
if b27 = = '__main__':
    fonk2(0, 200000)