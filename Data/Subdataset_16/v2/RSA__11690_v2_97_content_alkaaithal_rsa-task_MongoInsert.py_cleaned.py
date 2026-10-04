import pandas as pd
import glob
from pymongo import MongoClient
import shutil
def fonk1():
    b1 = MongoClient('localhost', 27017)
    b2 = b1['your_database_name']
    return b2
b2 = fonk1()
b3 = r'C:\Users\aithaa\Documents\nse'
b4 = glob.glob(b3 + "/*.csv")
def fonk2(b7):
    try:
        b2.stock_info.insert_many(b7)
        print(f"Inserted {len(b7)} records successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
def fonk3(file_name):
    b5 = r"C:\Users\aithaa\Documents\tempo"
    b6 = pd.read_csv(file_name, index_col=None, header=0)
    b7 = []
    for index, row in b6.iterrows():
        b8 = {"symbol": row["SYMBOL"], "series": row[" SERIES"]}
        b9 = b2.company_info.find_one(b8)
        b10 = ''
        if b9 is None:
            b10 = str(b2.company_info.insert_one(b8).inserted_id)
        else:
            b10 = b9.get('_id')
        try:
            b7.append({
                "company_id": b10,
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
            print(f"Error processing row: {row}")
            print(f"Exception: {e}")
    fonk2(b7)
    shutil.move(file_name, b5)
if b11 = = "__main__":
    print("Starting data insertion...")
    for file_name in b4:
        fonk3(file_name)
    print("Data insertion completed.")