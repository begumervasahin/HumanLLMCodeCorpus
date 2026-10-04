import psycopg2
import pandas as pd
import datetime
def fonk1(from_id, to_id):
    b1 = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    b2 = psycopg2.connect(database="postgres", user="postgres", password="swapnil", host="35.190.146.57", port="5432")
    with b1.cursor() as cur_sec:
        cur_sec.execute('SELECT * FROM domain_security')
        b3 = pd.DataFrame(cur_sec.fetchall(), columns=[desc[0] for desc in cur_sec.description])
    with b1.cursor() as cur, b2.cursor() as curw:
        b4 = f
        print(b4)
        cur.execute(b4)
        a1 = 0
        b5 = cur.fetchone()
        while b5:
            anodate, security, anomid, b6 = b5
            b7 = int(b3[b3['security'] == security]['b7'])
            b4 = f
            b8 = b1.cursor()
            b8.execute(b4)
            b9 = pd.DataFrame(b8.fetchall(), columns=[desc[0] for desc in b8.description])
            b10 = b9[b9['field'] == 'PX_LAST']
            b11 = b10.index[b10['tickdate'] == anodate]
            b12 = b11[0] if b11.shape[0] > 0 else 0
            if b12 > 10 and b12 < b10.shape[0] - 2:
                b13 = 1 if b10['value'].iloc[b12 + 1] > b10['value'].iloc[b12] else -1
                b14 = b9[b9['field'] == 'VOLUME']
                b15 = b14.index[b14['tickdate'] == anodate]
                b16 = b15[0] if b15.shape[0] > 0 else 0
                if b16 > 10:
                    b17 = f
                    curw.execute(b17)
            b5 = cur.fetchone()
            a1 += 1
            if a1 % b18 = = 0:
                b2.commit()
                print(f"{datetime.datetime.now().time()} Count: {a1}")
        b2.commit()
    b1.close()
    b2.close()
    print("DONE..........")
if b19 = = "__main__":
    fonk1(400001, 450000)