import requests
import json

url_coffe_futures = 'https://www.quandl.com/api/v3/datasets/CHRIS/ICE_KC1'
rjson = requests.get(url_coffe_futures).json()

print (rjson['dataset']['name'])
Coffee C Futures, Continuous Contract #1 (KC1) (Front Month)

print (rjson['dataset']['description'])
Historical Futures Prices: Coffee C Futures, Continuous Contract #1. Non-adjusted price based on spot-month continuous contract calculations. Raw data from ICE.

print (rjson['dataset']['column_names'])
['Date', 'Open', 'High', 'Low', 'Settle', 'Change', 'Wave', 'Volume', 'Prev. Day Open Interest', 'EFP Volume', 'EFS Volume', 'Block Volume']

print (rjson['dataset']['data'][0])
['2017-06-02', 128.0, 128.15, 125.25, 125.55, -2.15, 126.78, 22408.0, 96836.0, 455.0, 52.0, None]