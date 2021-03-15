import pandas as pd
from datetime import datetime


# Read files
raw_data = pd.read_csv("/usr/local/airflow/dir/input_dir/raw_data.csv") # read raw data
ref_data = pd.read_csv("/usr/local/airflow/dir/lookup_dir/ref.csv") # read reference data

# Merge data and munge the df
nu_df = raw_data.merge(ref_data, left_on="id", right_on="id")

# Create new variable
nu_df["profit"] = nu_df["count"] * nu_df["val"]

# Calculate
profit = nu_df["profit"].sum()

# Generate date variable
date_var = datetime.today().strftime('%Y%m%d')

# Write to new file
f = open(f"/usr/local/airflow/dir/output_dir/{date_var}_output.txt", "w") # open
f.write(f"Todays total profit has been {profit} GBP") # input
f.close() # close
