import requests
import os
from cachetools import cached, TTLCache


cashe_ttl = TTLCache(maxsize=100, ttl=3*60*60) 


@cached(cashe_ttl) # Cache the results of this function for 3 hours
def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    api_key = os.getenv('EXCHANGERATE_API_KEY')
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()['conversion_rates'][to_currency]
    return(data)


def convert_currency(amount: float, exchange_rate: float) -> float:
    return amount * exchange_rate


