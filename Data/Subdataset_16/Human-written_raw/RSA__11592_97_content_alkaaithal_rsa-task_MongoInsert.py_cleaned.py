import pandas as pd
import glob
from dbconnection import dbconnect
import shutil
b1 = dbconnect()
b2 = r'C:\Users\aithaa\Documents\nse'
b3 = glob.glob(b2 + "/*.csv")
def fonk1(b6):
    try:
        b1.stock_info.insert_many(b6)
    except Exception as e:
        print(e.with_traceback())
def fonk2(file_name):
    b4 = "C:/Users/aithaa/Documents/tempo/"
    b5 = pd.read_csv(file_name, index_col=None, header=0)
    b6 = []
    for index, row in b5.iterrows():
        b7 = {"symbol": row["SYMBOL"], "series": row[" SERIES"]}
        b8 = b1.company_info.find_one(b7)
        b9 = ''
        if b8 is None:
            b9 = str(b1.company_info.insert_one(b7).inserted_id)
        else:
            b9 = b8.get('_id')
        try:
            b6.append(
                {"company_id": b9,
                 "date": str(row[' DATE1']),
                 "prev_close": str(row[' PREV_CLOSE']),
                 "open_price": str(row[' OPEN_PRICE']),
                 "high_price": str(row[' HIGH_PRICE']),
                 "low_price": str(row[' LOW_PRICE']),
                 "last_price": str(row[' LAST_PRICE']),
                 "close_price": str(row[' CLOSE_PRICE']),
                 "avg_price": str(row[' AVG_PRICE']),
                 "ttl_trd_qnty": str(row[' TTL_TRD_QNTY']),
                 "turnover_lacs": str(row[' TURNOVER_LACS']),
                 "no_of_trades": str(row[' NO_OF_TRADES']),
                 "deliv_qty": str(row[' DELIV_QTY']),
                 "deliv_per": str(row[' DELIV_PER'])
                 })
        except Exception as e:
            print(row)
            print(e)
    fonk1(b6)
    shutil.move(file_name, b4)
print("Inserting is done")
for file_name in b3:
    fonk2(file_name)