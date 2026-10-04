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
        b6 = cur.fetchone()
        while b6:
            anodate, security, anomid, b7 = b6
            b8 = int(b4.loc[b4['security'] == security, 'b8'].iloc[0])
            b5 = f
            b9 = b2.cursor()
            b9.execute(b5)
            b10 = pd.DataFrame(b9.fetchall(), columns=[desc[0] for desc in b9.description])
            b11 = b10[b10['field'] == 'PX_LAST']
            b12 = b11.index[b11['tickdate'] == anodate]
            b13 = b12[0] if not b12.empty else 0
            if 10 < b13 < b11.shape[0] - 2:
                b14 = 1 if b11['value'].iloc[b13 + 1] > b11['value'].iloc[b13] else -1
                b15 = b10[b10['field'] == 'VOLUME']
                b16 = b15.index[b15['tickdate'] == anodate]
                b17 = b16[0] if not b16.empty else 0
                if b17 > 10:
                    b18 = f
                    curw.execute(b18)
            b6 = cur.fetchone()
            a1 += 1
            if a1 % b19 = = 0:
                b3.commit()
                print(f"{datetime.datetime.now().time()} Count: {a1}")
        b3.commit()
    b2.close()
    b3.close()
    print("DONE..........")
if b20 = = "__main__":
    fonk1(400001, 450000)