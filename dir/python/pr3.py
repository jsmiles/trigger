from datetime import datetime
import os
import glob

# Prepare date variable
date_var = datetime.today().strftime('%Y%m%d')

# Set paths
path = "/usr/local/airflow/dir/input_dir/"
dest = "/usr/local/airflow/dir/processed_dir/"
os.chdir(path)

# Rename and move file to new location
for file in glob.glob('*.csv'):
    os.rename(f"{path}{file}", f"{dest}{date_var}_{file}")
