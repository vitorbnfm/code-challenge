import sqlite3
from sqlite3 import Error
import pandas as pd
import sys

date = sys.argv[1][:10]

def create_conn(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection successful")
    except Error as e:
            print("The error % occurred.".format(e))
    return conn
    
conn = create_conn(r"/data/output.db") 
cur = conn.cursor()


orders = pd.read_csv(f"/data/postgres/orders/{date}/orders_{date}.csv")
orders_details = pd.read_csv(f"/data/csv/{date}/order_details_{date}.csv")
orders.to_sql(f"orders_{date}", conn, if_exists='replace', index=False)
orders_details.to_sql(f"orders_details_{date}", conn, if_exists='replace', index=False)
final_query = orders.merge(orders_details,on=["order_id"])
final_query.to_csv("/data/final_query.csv", index=False)

