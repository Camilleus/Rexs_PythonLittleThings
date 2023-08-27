import requests
from datetime import datetime

response = requests.get(
    "http://api.nbp.pl/api/exchangerates/tables/a?format=json")

if response.ok == True:
    data = response.json()[0]
    print(data)

    table = data['table']
    no = data["no"]
    effectiveDate = data["effectiveDate"]
    print(f"Exchange rates for {effectiveDate}: \n", "table:",table, "\n number:",no)

    rates = data["rates"]
    for rate in rates:
        currency = rate["currency"]
        code = rate["code"]
        mid = rate["mid"]
        print(currency, " code:", code, "value:", mid)
