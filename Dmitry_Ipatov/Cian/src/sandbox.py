

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

def get_next_page_url(current_page):
    s = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&region=1&room1=1&room2=1&p='
    num = str(current_page + 1)
    return s + num


for i in range(0, 3):
    print(get_next_page_url(i))