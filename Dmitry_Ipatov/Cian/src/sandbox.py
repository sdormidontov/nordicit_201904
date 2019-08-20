import requests
from bs4 import BeautifulSoup


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

lst = ['1', 'балкон,', '3', 'лоджия']
# https://stackoverflow.com/questions/13779526/finding-a-substring-within-a-list-in-python
sub_balcony = 'балк'
elem = next((s for s in lst if sub_balcony in s), None)
balcony_quantity = lst[lst.index(elem) - 1]
print(balcony_quantity)

sub_loggia = 'лодж'
elem = next((s for s in lst if sub_loggia in s), None)
loggia_quantity = lst[lst.index(elem) - 1]
print(loggia_quantity)





# for i in lst:
#
#      if str(i).__contains__('балкон'):
#          print(lst.index(i))
#          balcony_q_index = lst.index(i)-1
#          balciny_q = lst[balcony_q_index]
#          print(balciny_q)
#      else:
#          print('not')
