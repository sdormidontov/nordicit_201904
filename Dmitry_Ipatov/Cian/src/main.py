from bs4 import BeautifulSoup
import requests
import time
import src.flat as f
import csv
import src.page_urls as page_urls


# получение страниц, например с 1 по 3
pages = page_urls.get_page_urls_list(1, 3)

for i in pages:
    url = i


#url = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&region=1&room1=1&room2=1'
    r = requests.get(url)
    if r.ok:
        soup = BeautifulSoup(r.text, 'lxml')

    #print(soup.contents)
    else:
        print('Bad request')

# https://www.cian.ru/sale/flat/213470278/



# with open('page1.txt', 'r') as inf:
#     lst = []
#     for row in inf:
#         lst.append(row)
#     text = '\n'.join(lst)
    #print(text)

#soup = BeautifulSoup(text, 'lxml')
#print(soup.contents)



    lst = soup.findAll('a', class_="c6e8ba5398--header--1fV2A")


# next_page = soup.findAll('a', class_="_93444fe79c--list-itemLink--3o7_6")
# print(next_page)
# print('next page text: ', next_page[0].text)
# print('next page href: ', next_page[0].attrs['href'])


    # получение ссылок на квартиры на данной странице
    links = []
    for i in lst:
       links.append(i.attrs['href'])

    print('links of page: ', url)
    print (links)

# for i in links:
#     print(i)

# flat = requests.get(links[0])
# if flat.ok:
#     soup = BeautifulSoup(flat.text, 'lxml')
#     print(soup.contents)
# else:
#     print('Bad request')


# отсюда вызываем флеты по линкам
# писать try catch на получение каждой квартиры
# написать Сергею список атрибутов

#TODO

# поставить time.sleep(30)
# запускать алгоритм пачками
# писать квартиру сразу в файлик после каждого считывания






#допустим у нас ссылки в файле
links_to_flats = ['https://www.cian.ru/sale/flat/212633712/',
                  'https://www.cian.ru/sale/flat/211834401/',
                  'https://www.cian.ru/sale/flat/212836793/']






# обрабатываем ссылки в файле
# for i in links_to_flats:
#
#     link = i
#     print('link to the flat: ', link)
#     flat = f.Flat()
#     flat.get_content(link)
#
#     try:
#         flat.get_metro()
#         print('Метро: ', flat.metro)
#     except Exception:
#         print('exception on get_metro')
#
#     time.sleep(2)
#
#     flat.get_square_meters_total()
#     print('total square: ', flat.square_meters_total)
#
#     print('========')
#     time.sleep(2)
#
#     # write to csv
#     with open('flats.csv', 'a') as csvfile:
#         filewriter = csv.writer(csvfile, delimiter=',')
#
#         filewriter.writerow([link, flat.metro, flat.square_meters_total])
#
#     # delete link
#     links_to_flats.remove(i)


# если в текущей пачке больше ссылок не осталось, то надо получить следующую порцию
# if len(links_to_flats) == 0:
#     get_next_links_pack()
# else:
#     print('some links didnt proceeded')







# flat.get_square_meters_living_room()
# print('living square', flat.square_meters_living_room)

