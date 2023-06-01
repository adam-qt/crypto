import requests
from .models import Crypto
from django.db import Error
import requests


def parse_data_from_api():
    """данная функция делает запрос на API для получения данных о криптовалютах и заносит эти данные в базу данных"""

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=2000&sort=price'
    key = 'd522595b-2111-45cb-b1a9-dc636086ca6d'
    headers = {
        'X-CMC_PRO_API_KEY': f'{key}'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.RequestException as e:
        data = e

    # следующий код заносит полученные данные в БД

    for coin in data['data']:
        name = coin['name']
        unit, _ = Crypto.objects.get_or_create(name=name)
        try:
            unit.slug = coin['symbol']
            unit.total_supply = coin['total_supply']
            unit.price = int(coin['quote']['USD']['price'])
            unit.market_cap = int(coin['quote']['USD']['market_cap'])
            unit.volume_change_24h = float("{:.2f}".format(
                coin['quote']['USD']['volume_change_24h']))
            unit.percent_change_24h = float("{:.2f}".format(
                coin['quote']['USD']['percent_change_24h']))
            unit.save()

        except Error:
            continue
        except requests.exceptions.RequestException:
            continue
        except BaseException:
            continue
