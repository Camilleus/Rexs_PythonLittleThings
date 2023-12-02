# import requests
# from datetime import datetime

# response = requests.get(
#     "http://api.nbp.pl/api/exchangerates/tables/a?format=json")

# if response.ok == True:
#     data = response.json()[0]
#     table = data['table']
#     no = data["no"]
#     effectiveDate = data["effectiveDate"]
#     print(f"Exchange rates for {effectiveDate}: \n",
#           "table:", table, "\n number:", no)

#     rates = data["rates"]
#     for rate in rates:
#         currency = rate["currency"]
#         code = rate["code"]
#         mid = rate["mid"]
#         print(currency, " code:", code, "value:", mid)


import aiohttp
from datetime import datetime, timedelta
import asyncio
import sys


async def fetch_exchange_rates(days_ago):
    base_url = "http://api.nbp.pl/api/exchangerates/tables/C/"
    today = datetime.now()
    dates = [today - timedelta(days=i) for i in range(min(days_ago, 10))]
    results = []

    async with aiohttp.ClientSession() as session:
        for date in dates:
            date_str = date.strftime("%Y-%m-%d")
            url = f"{base_url}{date_str}/?format=json"
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        try:
                            data = await response.json()
                            if data:
                                rates = {}
                                for rate in data[0]['rates']:
                                    rates[rate['code']] = {
                                        'sale': rate['ask'], 'purchase': rate['bid']}

                                result = {date_str: rates}
                                results.append(result)
                        except aiohttp.ContentTypeError:
                            print(f"Response for {date_str} is not JSON")
                    else:
                        print(
                            f"Error fetching data for {date_str}: {response.status}")
            except Exception as e:
                print(f"Error fetching data for {date_str}: {e}")
    return results


async def main():
    if len(sys.argv) != 2:
        print("Usage: python NBPExchangeRates.py <number_of_days>")
        return

    days_ago = int(sys.argv[1])
    results = await fetch_exchange_rates(days_ago)
    print(results)


asyncio.run(main())
