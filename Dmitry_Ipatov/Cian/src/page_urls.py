def get_page_urls_list(page_from, page_to):
    s = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&region=1&room1=1&room2=1&p='
    lst = []

    for i in range(page_from, page_to + 1):
        url = s + str(i)
        lst.append(url)
    return lst



# page_urls = []
# for i in range(0, 3):
#     page_urls.append(get_page_urls(i))
#
# print(page_urls)

# l = get_page_urls_list(1, 3)
# print(l)