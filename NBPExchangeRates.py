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
import asyncio
import sys
from datetime import datetime, timedelta


async def fetch_exchange_rates(days_ago):
    base_url = "http://api.nbp.pl/api/exchangerates/tables/C/"
    today = datetime.now()
    dates = [today - timedelta(days=i) for i in range(min(days_ago, 10))]
    results = []

    async with aiohttp.ClientSession() as session:
        for date in dates:
            date_str = date.strftime("%d.%m.%Y")
            url = f"{base_url}{date_str}"

            try:
                async with session.get(url) as response:
                    data = await response.json()
                    if data:
                        rates = {}
                        for rate in data[0]['rates']:
                            rates[rate['code']] = {
                                'sale': rate['ask'], 'purchase': rate['bid']}
                        result = {date_str: rates}
                        results.append(result)
            except Exception as e:
                print(f"Error fetching data for {date_str}: {e}")

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <days>")
        return

    days_ago = int(sys.argv[1])

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(fetch_exchange_rates(days_ago))

    print(results)


if __name__ == "__main__":
    main()
