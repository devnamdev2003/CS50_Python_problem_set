import requests
import sys

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate = r.json()["bpi"]["USD"]["rate"]
except requests.RequestException:
    pass

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

price_float = float(rate.replace(",", "")) * n
price_string = "{:,.4f}".format(price_float)
print(f"${price_string}")