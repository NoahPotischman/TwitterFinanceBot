import requests

def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum&vs_currencies=usd&include_24hr_change=true"
    response = requests.get(url)
    return response.json()
