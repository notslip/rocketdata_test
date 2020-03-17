import requests
from bs4 import BeautifulSoup as bs
import json
import os

response = requests.get("https://www.mebelshara.ru/contacts")
c = response.content
c = c.decode()
soup = bs(c, 'lxml')
phone = soup.find('a', class_='head-text-2').text.strip()
cityes = soup.find_all('div', class_='city-item')

json_list = []
for city in cityes:
    city_name = city.find('h4', class_='js-city-name').text
    shop_list = city.find_all('div', class_='shop-list-item')
    for shop in shop_list:
        phones = [phone]
        working_hours=['{} {}'.format(shop.attrs['data-shop-mode1'],
                                      shop.attrs['data-shop-mode2'])]
        latlon = [shop.attrs['data-shop-latitude'],
                  shop.attrs['data-shop-longitude']]
        json_dict = {
            "address": "{}, {}".format(city_name, shop.attrs['data-shop-address']),
            "latlon":latlon,
            "name": shop.attrs['data-shop-name'],
            "phones": phones,
            "working_hours": working_hours
        }
        json_list.append(json_dict)

get_path = os.path.dirname(__file__)
path = os.path.join(get_path, 'json1.json',)
with open(path, 'w') as wf:
    json.dump(json_list, wf, ensure_ascii=False, indent=4)











