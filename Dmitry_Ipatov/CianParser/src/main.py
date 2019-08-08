from bs4 import BeautifulSoup
import requests
import time

# url = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&region=1&room1=1&room2=1'
# r = requests.get(url)
# if r.ok:
#     soup = BeautifulSoup(r.text, 'lxml')
#     print(soup.contents)
# else:
#     print('Bad request')

# https://www.cian.ru/sale/flat/213470278/

with open('page1.txt', 'r') as inf:
    lst = []
    for row in inf:
        lst.append(row)
    text = '\n'.join(lst)
    #print(text)

soup = BeautifulSoup(text, 'lxml')
#print(soup.contents)



lst = soup.findAll('a', class_="c6e8ba5398--header--1fV2A")

links = []
for i in lst:
    links.append(i.attrs['href'])

for i in links:
    print(i)

# flat = requests.get(links[0])
# if flat.ok:
#     soup = BeautifulSoup(flat.text, 'lxml')
#     print(soup.contents)
# else:
#     print('Bad request')


отсюда вызываем флеты по линкам
писать try catch на получение каждой квартиры
написать Сергею список атрибутов

#TODO

поставить time.sleep(30)
запускать алгоритм пачками
писать квартиру сразу в файлик после каждого считывания

