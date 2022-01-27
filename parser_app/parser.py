import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt


HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
URL = 'https://rezka.ag/films/comedy/page/1/'





@csrf_exempt
def get_html(URL, params=''):
    req = requests.get(URL, headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    film = []
    for i in items:
        film.append(
            {
                'title': i.find('div', class_='b-content__inline_item-link').get_text(),
                'image': i.find('div', class_='b-content__inline_item-cover').find('a').find('img').get('src')
            }
        )
    return film

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        film = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            film.extend(get_data(html.text))
            print(film)
            return film
    else:
        raise ValueError('Error')