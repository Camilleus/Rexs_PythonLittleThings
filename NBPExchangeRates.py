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


async def fetch_exchange_rates(start_date, end_date):
    base_url = "http://api.nbp.pl/api/exchangerates/tables/C/{start_date}/{end_date}/?format=json"

    url = base_url.format(start_date=start_date, end_date=end_date)
    results = []

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    try:
                        data = await response.json()
                        if data:
                            rates = {}
                            for rate in data[0]['rates']:
                                if rate['code'] in ['USD', 'EUR']:
                                    rates[rate['code']] = {
                                        'sale': rate['ask'], 'purchase': rate['bid']}
                            result = {start_date: rates}
                            results.append(result)
                    except aiohttp.ContentTypeError:
                        print(f"Response is not JSON for {start_date}")
                else:
                    print(
                        f"Error fetching data for {start_date}: {response.status}")
        except Exception as e:
            print(f"Error fetching data for {start_date}: {e}")

    return results


async def main():
    if len(sys.argv) != 2:
        print("Usage: python NBPExchangeRates.py <number_of_days>")
        return

    days_ago = int(sys.argv[1])
    today = datetime.now()
    end_date = today.strftime("%Y-%m-%d")
    start_date = (today - timedelta(days=days_ago)).strftime("%Y-%m-%d")

    results = await fetch_exchange_rates(start_date, end_date)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
