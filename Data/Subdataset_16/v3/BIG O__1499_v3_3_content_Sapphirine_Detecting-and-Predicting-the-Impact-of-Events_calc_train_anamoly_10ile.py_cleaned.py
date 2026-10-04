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
    b4 = fonk2(b2)
    b5 = fonk3(b2, from_id, to_id)
    fonk4(b2, b3, b4, b5)
    b3.commit()
    b2.close()
    b3.close()
    print("DONE..........")
def fonk2(b2):
    with b2.cursor() as cursec:
        cursec.execute('SELECT * FROM domain_security')
        b4 = pd.DataFrame(cursec.fetchall(), columns=[desc[0] for desc in cursec.description])
    return b4
def fonk3(b2, from_id, to_id):
    b6 = f
    print(b6)
    with b2.cursor() as cur:
        cur.execute(b6)
        b5 = cur.fetchall()
    return b5
def fonk4(b2, b3, b4, b5):
    a1 = 0
    for anodate, security, anomid, anoscore in b5:
        b7 = fonk5(b4, security)
        b8 = fonk6(b2, security, anodate)
        if not b8.empty:
            b9 = fonk7(b8, anodate)
            if b9 is not None:
                b10 = fonk8(anomid, anodate, anoscore, security, b7, b9, b8)
                fonk9(b3, b10)
        a1 += 1
        if a1 % b11 = = 0:
            b3.commit()
            print(f"{datetime.datetime.now().time()} - Count: {a1}")
def fonk5(b4, security):
    return int(b4[b4['security'] == security]['b7'])
def fonk6(b2, security, anodate):
    b12 = f
    with b2.cursor() as curread:
        curread.execute(b12)
        b8 = pd.DataFrame(curread.fetchall(), columns=[desc[0] for desc in curread.description])
    return b8
def fonk7(b8, anodate):
    b13 = b8[b8['field'] == 'PX_LAST']
    b14 = b13.index[b13['tickdate'] == anodate]
    b15 = b14[0] if not b14.empty else 0
    if b15 > 10 and b15 < len(b13) - 2:
        return 1 if b13['value'].iloc[b15 + 1] > b13['value'].iloc[b15] else -1
    return None
def fonk8(anomid, anodate, anoscore, security, b7, b9, b8):
    b13 = b8[b8['field'] == 'PX_LAST']
    b16 = b8[b8['field'] == 'VOLUME']
    b15 = b13.index[b13['tickdate'] == anodate][0]
    b17 = b16.index[b16['tickdate'] == anodate][0]
    b10 = [anomid, anodate, anoscore, security, b7, b9] + \
             b13['value'].iloc[b15-9:b15+1].tolist() + \
             b16['value'].iloc[b17-9:b17+1].tolist()
    return b10
def fonk9(b3, b10):
    b18 = f
    with b3.cursor() as curw:
        curw.execute(b18)
if b19 = = '__main__':
    fonk1(0, 200000)