import requests

import json
import os


response = requests.get("https://www.tui.ru/api/office/cities/")
json_list=[]
for city in response.json():
    ofice_response= requests.get("https://www.tui.ru/api/office/list/?cityId={}".format(city['cityId']))
    for ofice in ofice_response.json():
        workdays=ofice['hoursOfOperation']['workdays']
        saturday=ofice['hoursOfOperation']['saturday']
        sunday=ofice['hoursOfOperation']['sunday']

        weekend = 'cб {}-{} вс {} - {}'.format(saturday['start'][:-3], saturday['end'][:-3], sunday['start'][:-3], sunday['end'][:-3])
        hours=['пн-пт {}-{}'.format(workdays['start'][:-3], workdays['end'][:-3]),
               weekend
               ]
        json_dict={
            'adress': ofice['address'],
            'latlon' : [ofice['latitude'], ofice['longitude'] ],
            "name": ofice['name'],
            "phones": [ phone['phone'] for phone in ofice['phones']],
            "working_hours": hours
        }
        json_list.append(json_dict)

get_path = os.path.dirname(__file__)
path = os.path.join(get_path, 'json2.json',)
with open(path, 'w') as wf:
    json.dump(json_list, wf, ensure_ascii=False, indent=4)









# response = requests.get("https://www.tui.ru/api/office/cities/")
#
# print(response.text)
# print(len(response.text))