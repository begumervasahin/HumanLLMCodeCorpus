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
    with b2.cursor() as cur_sec:
        cur_sec.execute('SELECT * FROM domain_security')
        b4 = pd.DataFrame(cur_sec.fetchall(), columns=[desc[0] for desc in cur_sec.description])
    with b2.cursor() as cur, b3.cursor() as curw:
        b5 = f
        print(b5)
        cur.execute(b5)
        a1 = 0
        for row in cur.fetchall():
            anodate, security, anomid, b6 = row
            b7 = int(b4.loc[b4['security'] == security, 'b7'].iloc[0])
            b5 = f
            b8 = b2.cursor()
            b8.execute(b5)
            b9 = pd.DataFrame(b8.fetchall(), columns=[desc[0] for desc in b8.description])
            b10 = b9[b9['field'] == 'PX_LAST']
            b11 = b10.index[b10['tickdate'] == anodate]
            b12 = b11[0] if not b11.empty else 0
            if 10 < b12 < b10.shape[0] - 2:
                b13 = 1 if b10['value'].iloc[b12 + 1] > b10['value'].iloc[b12] else -1
                b14 = b9[b9['field'] == 'VOLUME']
                b15 = b14.index[b14['tickdate'] == anodate]
                b16 = b15[0] if not b15.empty else 0
                if b16 > 10:
                    b17 = f
                    curw.execute(b17)
            a1 += 1
            if a1 % b18 = = 0:
                b3.commit()
                print(f"{datetime.datetime.now().time()} Count: {a1}")
        b3.commit()
    b2.close()
    b3.close()
    print("DONE..........")
if b19 = = "__main__":
    fonk1(400001, 450000)