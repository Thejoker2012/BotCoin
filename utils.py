import requests

base_url = "https://api.cryptonator.com/api/ticker/"

def get_crypto_coin(name, coin="usd"):
	url="{}{}-{}".format(base_url, name, coin)
	response = requests.get(url)
	return float(response.json()["ticker"]["price"])

