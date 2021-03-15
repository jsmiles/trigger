import requests
from datetime import datetime

# Get a Chuck Norris joke from the API
x = requests.get('https://api.chucknorris.io/jokes/random')
joke  = x.json()['value']

# Prep date variable
date_var = datetime.today().strftime('%Y%m%d')

# Append the joke to my filename
f = open(f"/usr/local/airflow/dir/output_dir/{date_var}_output.txt", "a")
f.write("\n")
f.write(f"{joke}")
f.close
