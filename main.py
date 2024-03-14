import requests
from bs4 import BeautifulSoup
import re

number = 1
while number:
    response = requests.get(f'https://hard.rozetka.com.ua/ua/videocards/c80087/page={number}/')

    soup = BeautifulSoup(response.text, "html.parser")
    data = list(soup.findAll('a', class_='product-link goods-tile__heading'))

    name = []
    for i in range(len(data)):
        tmp_str = str(data[i])
        regex = re.compile(r'title="([^"]+)"')
        result = regex.search(tmp_str)
        if result:
            name.append(result.group(1))
            
    result = []        
    for i in name:
        if "asus" in i.lower():
            result.append(i)

    for item in result:
        print(item)

    number += 1
