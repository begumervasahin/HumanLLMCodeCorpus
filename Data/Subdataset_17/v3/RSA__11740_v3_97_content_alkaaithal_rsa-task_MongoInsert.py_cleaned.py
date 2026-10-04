import pandas as pd
import glob
from pymongo import MongoClient
import shutil
def dbconnect():
    client = MongoClient('localhost', 27017)
    db = client['your_database_name']
    return db
def insert_data_bulk(data_list, collection):
    try:
        collection.insert_many(data_list)
        print(f"Inserted {len(data_list)} records successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
def process_stock_data(file_name, db, dest):
    df = pd.read_csv(file_name, index_col=None, header=0)
    data_list = []
    for _, row in df.iterrows():
        header_data = {"symbol": row["SYMBOL"], "series": row[" SERIES"]}
        primary_data = db.company_info.find_one(header_data)
        if primary_data is None:
            primary_id = str(db.company_info.insert_one(header_data).inserted_id)
        else:
            primary_id = primary_data.get('_id')
        try:
            data_list.append({
                "company_id": primary_id,
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
    insert_data_bulk(data_list, db.stock_info)
    shutil.move(file_name, dest)
def main():
    db = dbconnect()
    path = r'C:\Users\aithaa\Documents\nse'
    all_files = glob.glob(path + "/*.csv")
    dest = r"C:\Users\aithaa\Documents\tempo"
    print("Starting data insertion...")
    for file_name in all_files:
        process_stock_data(file_name, db, dest)
    print("Data insertion completed.")
if __name__ == "__main__":
    main()