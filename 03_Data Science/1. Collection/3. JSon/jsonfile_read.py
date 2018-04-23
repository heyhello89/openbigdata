import json
from pprint import pprint

with open('이명박_naver_news.json','r',encoding='utf8') as data_file:
    data = json.load(data_file)

pprint(data)

print(data["items"][0]["title"])
print(data["items"][1]["title"])
