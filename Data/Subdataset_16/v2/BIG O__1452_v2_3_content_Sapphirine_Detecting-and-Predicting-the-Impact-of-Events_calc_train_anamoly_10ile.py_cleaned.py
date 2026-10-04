import psycopg2
import pandas as pd
import datetime
def fonk1(from_id, to_id):
    b1 = {
        "database": "postgres",
        "user": "postgres",
        "password": "swapnil",
        "host": "35.190.146.57",
        "port": "5432"
    }
    b2 = psycopg2.connect(**b1)
    b3 = psycopg2.connect(**b1)
    with b2.cursor() as cursec:
        cursec.execute('SELECT * FROM domain_security')
        b4 = pd.DataFrame(cursec.fetchall(), columns=[desc[0] for desc in cursec.description])
    b5 = f
    print(b5)
    with b2.cursor() as cur:
        cur.execute(b5)
        b6 = cur.fetchall()
    a1 = 0
    for anodate, security, anomid, anoscore in b6:
        b7 = int(b4[b4['security'] == security]['b7'])
        b8 = f
        with b2.cursor() as curread:
            curread.execute(b8)
            b9 = pd.DataFrame(curread.fetchall(), columns=[desc[0] for desc in curread.description])
        b10 = b9[b9['field'] == 'PX_LAST']
        b11 = b10.index[b10['tickdate'] == anodate]
        b12 = b11[0] if not b11.empty else 0
        if b12 > 10 and b12 < len(b10) - 2:
            b13 = 1 if b10['value'].iloc[b12 + 1] > b10['value'].iloc[b12] else -1
            b14 = b9[b9['field'] == 'VOLUME']
            b15 = b14.index[b14['tickdate'] == anodate]
            b16 = b15[0] if not b15.empty else 0
            if b16 > 10:
                b17 = [anomid, anodate, anoscore, security, b7, b13] + \
                         b10['value'].iloc[b12-9:b12+1].tolist() + \
                         b14['value'].iloc[b16-9:b16+1].tolist()
                b18 = f
                with b3.cursor() as curw:
                    curw.execute(b18)
        a1 += 1
        if a1 % b19 = = 0:
            b3.commit()
            print(f"{datetime.datetime.now().time()} - Count: {a1}")
    b3.commit()
    b2.close()
    b3.close()
    print("DONE..........")
if b20 = = '__main__':
    fonk1(0, 200000)