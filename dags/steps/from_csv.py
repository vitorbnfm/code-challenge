import sys
import os
import shutil

date = sys.argv[1][:10]

input_file = "/data/order_details.csv"
output_dir = f"/data/csv/{date}"
output_file = f"{output_dir}/order_details_{date}.csv"
if not os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)

shutil.copy(input_file, output_file)