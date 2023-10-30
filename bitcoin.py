import requests
import sys
r = (requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')).json()
try:
    amount = float(sys.argv[1]) * ((r['bpi'])['USD'])['rate_float']
    print("$" + '{:,}'.format(amount))
except IndexError:
    sys.exit('no arg, try again')