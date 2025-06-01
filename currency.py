# WE WILL USE REQUEST API
# we will also use free currency api

import requests
API_KEY='fca_live_WnmrHgAsC2Rpxhqph7vBw7kEjvPns0o1eA6gGaMy'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
# f string help embed variable inside curly braces
CURRENCIES ={"USD", "CAD", "EUR", "AUD", "CNY"}
def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    # join takes all the elements from list and combine them together in a string using whatever is delimiter-in this case ",". Its just a separator
    url=f"{BASE_URL}& base_currency={base}& currencies={currencies}"
# the above are the query parameter
    try:
        response = requests.get(url)
        data = response.json()
    
        return data["data"]

    except:
        print("Invalid currency")
        return None
while True:
    base = input("Enter the base currency (Q for quit): ").upper() #this for upper case
    if base == "Q":
        break

    data= convert_currency(base)
    if not data:
        continue
    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}:{value}")