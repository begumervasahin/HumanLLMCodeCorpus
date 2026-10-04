import pandas as pd
import glob
import shutil
from dbconnection import dbconnect
db = dbconnect()
CSV_DIRECTORY_PATH = r'C:\Users\aithaa\Documents\nse'
DESTINATION_PATH = r'C:\Users\aithaa\Documents\tempo'
all_files = glob.glob(CSV_DIRECTORY_PATH + "/*.csv")
def insert_data_bulk(data_list):
    try:
        db.stock_info.insert_many(data_list)
    except Exception as e:
        print(f"Error during bulk insert: {e}")
def process_stock_data(file_name):
    df = pd.read_csv(file_name, index_col=None, header=0)
    data_list = []
    for index, row in df.iterrows():
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
            print(f"Error processing row {index}: {row}")
            print(e)
    insert_data_bulk(data_list)
    shutil.move(file_name, DESTINATION_PATH)
def main():
    for file_name in all_files:
        process_stock_data(file_name)
    print("Data insertion is done.")
if __name__ == "__main__":
    main()