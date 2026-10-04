import pandas as pd
import glob
from pymongo import MongoClient
import shutil
def fonk1():
    b1 = MongoClient('localhost', 27017)
    b2 = b1['your_database_name']
    return b2
def fonk2(b4, collection):
    try:
        collection.insert_many(b4)
        print(f"Inserted {len(b4)} records successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
def fonk3(file_name, b2, b10):
    b3 = pd.read_csv(file_name, index_col=None, header=0)
    b4 = []
    for _, row in b3.iterrows():
        b5 = {"symbol": row["SYMBOL"], "series": row[" SERIES"]}
        b6 = b2.company_info.find_one(b5)
        if b6 is None:
            b7 = str(b2.company_info.insert_one(b5).inserted_id)
        else:
            b7 = b6.get('_id')
        try:
            b4.append({
                "company_id": b7,
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
    fonk2(b4, b2.stock_info)
    shutil.move(file_name, b10)
def fonk4():
    b2 = fonk1()
    b8 = r'C:\Users\aithaa\Documents\nse'
    b9 = glob.glob(b8 + "/*.csv")
    b10 = r"C:\Users\aithaa\Documents\tempo"
    print("Starting data insertion...")
    for file_name in b9:
        fonk3(file_name, b2, b10)
    print("Data insertion completed.")
if b11 = = "__main__":
    fonk4()