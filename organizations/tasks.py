from celery import shared_task
import requests
from .models import Organization, CryptoPrice

@shared_task
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url).json()

    btc_price = response["bitcoin"]["usd"]
    eth_price = response["ethereum"]["usd"]

    for org in Organization.objects.all():
        CryptoPrice.objects.create(org=org, symbol="BTC", price=btc_price)
        CryptoPrice.objects.create(org=org, symbol="ETH", price=eth_price)
