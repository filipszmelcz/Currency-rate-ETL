import requests
from datetime import datetime, timedelta
import csv


currency = ["USD", "PLN"]
base_url = "https://data.fixer.io/api/"

def get_currency(currency, date = "latest"):
    url = f"{base_url}{date}"
    params = {
        "access_key": "f918716b661f55ba265f232635220b2e",
        "symbols": ",".join(currency)
        }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def load_currency_history(start_date: str, end_date: str, load_to_csv = True):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = timedelta(days=1)
    field_names = ['success', 'timestamp', 'historical', 'base', 'date', 'rates']
    while start <= end:
        date = start.strftime("%Y-%m-%d")
        info = get_currency(currency, date)     
        start += delta
        if load_to_csv == True:
            with open("load_currency_history.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(info.keys())
                w.writerow(info.values())
                f.close()
                return "Data transfer complete"
    

print(load_currency_history('2013-04-03', '2013-04-06'))
