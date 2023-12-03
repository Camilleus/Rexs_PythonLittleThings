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
    base_url = "http://api.nbp.pl/api/exchangerates/tables/C/{start_date}/{end_date}/?format=json"
    today = datetime.now()
    start_date = (today - timedelta(days=days_ago)).strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")
    url = base_url.format(start_date=start_date, end_date=end_date)

    async with aiohttp.ClientSession() as session:
        for date in dates:
            date_str = date.strftime("%Y-%m-%d")
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


if __name__ == "__main__":
    asyncio.run(main())
