import psycopg2
import pandas as pd
import sys
import os

date = sys.argv[1][:10]
conn  = psycopg2.connect(host="northwind_db",database = "northwind", user = "northwind_user", password = "thewindisblowing")
cur = conn .cursor()
cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
tables = [table[0] for table in cur.fetchall()]

for table_name in tables:
    df = pd.read_sql(f"SELECT * FROM {table_name}", con=conn)
    path = f"/data/postgres/{table_name}/{date}/{table_name}_{date}.csv"
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    df.to_csv(path, index=False)

conn.close()


    


