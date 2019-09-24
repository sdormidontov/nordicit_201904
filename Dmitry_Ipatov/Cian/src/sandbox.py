import requests
from bs4 import BeautifulSoup
import datetime
import csv

# s = '38,5 м²'
# lst = s.split(' ')
# s1 = lst[0]
# s2 = s1.replace(',', '.')
# n = float(s2)
# print (n)
#
# el = float(s.replace(',', '.').split(' ')[0])
# print(type(el))


# links_to_flats = ['https://www.cian.ru/sale/flat/212633712/', 'https://www.cian.ru/sale/flat/211834401/']
#
# for i in links_to_flats:
#
#     link = i
#     print(link)



#filewriter.writerow(['Link', 'Metro', 'TotalSquare'])



# получить номер следующей страницы
# for i in range(1, 4):
#
#     print(i)

# def get_next_page_url(current_page):
#     s = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&region=1&room1=1&room2=1&p='
#     num = str(current_page + 1)
#     return s + num


# for i in range(0, 3):
#     print(get_next_page_url(i))



# def get_content(link):
#     flat = requests.get(link)
#     if flat.ok:
#         soup = BeautifulSoup(flat.text, 'lxml')
#         print(soup.contents)
#     else:
#         print('Bad request')
#
# get_content('https://krasnogorsk.cian.ru/sale/flat/213030063/')


# lst = ['1', 'test,', '1', 'лоджия']
# if 'test' in str(lst):
#     print (str(lst).index('test'))
# else:
#     print('not ok')
#
#
# print (["foo", "bar", "baz"].index("bar"))
#
# print(["1", "test","1", "werewr"].index('test')-1)


# lst = ['1', 'балкон,', '1', 'лоджия']
# sub = 'балк'
# print any(sub in mystring for mystring in lst)

# lst = ['1', 'балкон,', '3', 'лоджия']
# # https://stackoverflow.com/questions/13779526/finding-a-substring-within-a-list-in-python
# sub_balcony = 'балк'
# elem = next((s for s in lst if sub_balcony in s), None)
# balcony_quantity = lst[lst.index(elem) - 1]
# print(balcony_quantity)
#
# sub_loggia = 'лодж'
# elem = next((s for s in lst if sub_loggia in s), None)
# loggia_quantity = lst[lst.index(elem) - 1]
# print(loggia_quantity)





# for i in lst:
#
#      if str(i).__contains__('балкон'):
#          print(lst.index(i))
#          balcony_q_index = lst.index(i)-1
#          balciny_q = lst[balcony_q_index]
#          print(balciny_q)
#      else:
#          print('not')



# print(now.strftime("%Y-%m-%d %H:%M:%S"))



# links_to_flats = ['https://www.cian.ru/sale/flat/211834401/',
#                   'https://www.cian.ru/sale/flat/212633712/',
#                   'https://www.cian.ru/sale/flat/212836793/',
#                   #'https://www.cian.ru/sale/flat/200112159/',  # рядом с 4мя станциями
#                   #'https://krasnogorsk.cian.ru/sale/flat/213030063/'
#                   ]
#
# for i in links_to_flats:
#     print(i)
#     print('обработка № {} из {}'.format(links_to_flats.index(i),
#                                         len(links_to_flats))
#                                         ,i)

pages = [
    'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&region=1&room1=1&room2=1&p=6',
    'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&region=1&room1=1&room2=1&p=7',
    'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&region=1&room1=1&room2=1&p=8']

for i in pages:
    url = i
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print(url)
    r = requests.get(url)
    if r.ok:
        print('made url request to url', url)
        soup = BeautifulSoup(r.text, 'lxml')

        lst = soup.findAll('a', class_="c6e8ba5398--header--1fV2A")
        links = []
        for i in lst:
            links.append(i.attrs['href'])

        print('получили ссылки на квартиры по урлу: ', url, len(links))
        print(links)

        for i in links:
            link = i
            print('обработка квартиры {} из {}'.format(links.index(i), len(links)), i)

            with open('flats_test.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',')
                filewriter.writerow([url,
                                     link,
                                     links.index(i),
                                     now.strftime("%Y-%m-%d %H:%M:%S"),
                                     ])

    else:
        print('Bad request')