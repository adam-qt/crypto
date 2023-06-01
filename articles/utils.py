import requests
from .models import Article
from django.db import Error
import requests


def parse_articles():
    url = 'https://min-api.cryptocompare.com/data/v2/news/?lang=EN'
    key = '2f304d772b4e6eb693e903cd01cdee17f9dcc121315d4389f22261048a5b2598'
    headers = {
        'Apikey ': f'{key}'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.RequestException as e:
        data = e
    for article in data['Data']:
        name = article['title']
        unit, _ = Article.objects.get_or_create(name=name)
        try:
            unit.url = article['url']
            unit.save()

        except Error:
            continue
        except requests.exceptions.RequestException:
            continue
        except BaseException:
            continue
