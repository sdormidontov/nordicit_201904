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
# links_to_flats = ['https://www.cian.ru/sale/flat/212633712/',
#                   'https://www.cian.ru/sale/flat/211834401/',
#                   'https://www.cian.ru/sale/flat/212836793/',
#                   ]


links_to_flats = ['https://www.cian.ru/sale/flat/211834401/',
                  'https://www.cian.ru/sale/flat/212633712/',
                  'https://www.cian.ru/sale/flat/212836793/',
                  'https://www.cian.ru/sale/flat/200112159/',  # рядом с 4мя станциями
                  'https://krasnogorsk.cian.ru/sale/flat/213030063/']  # время до метро на транспорте





# обрабатываем ссылки в файле
for i in links_to_flats:

    link = i
    print('link to the flat: ', link)
    flat = f.Flat()
    flat.get_content(link)

    try:
        flat.get_metro()
        print('Метро: ', flat.metro)
    except Exception:
        print('get_metro error')

    time.sleep(2)

    try:
        flat.get_square_meters_total()
    except Exception:
        print('get_square_meters_total error')
    print('total square: ', flat.square_meters_total)

    try:
        flat.get_square_meters_living()
    except Exception:
        print('get_square_meters_living error')
    print('living square: ', flat.square_meters_living)

    try:
        flat.get_square_meters_kitchen()
    except Exception:
        print('get_square_meters_kitchen error')
    print('kitchen square: ', flat.square_meters_kitchen)

    try:
        flat.get_floor()
    except Exception:
        print('get_floor error')
    print('current floor: ', flat.current_floor)
    print('total floors: ', flat.total_floors)


    try:
        flat.get_city()
    except Exception:
        print('get_city error')
    print('city: ', flat.city)

    try:
        flat.get_district()
    except Exception:
        print('get_district error')
    print('district: ', flat.district)

    try:
        flat.get_neighborhood()
    except Exception:
        print('get_neighborhood error')
    print('neighborhood: ', flat.neighborhood)

    try:
        flat.get_street()
    except Exception:
        print('get_street error')
    print('street: ', flat.street)

    try:
        flat.get_house_number()
    except Exception:
        print('get_house_number error')
    print('house number: ', flat.house_number)

    try:
        flat.get_time_to_metro()
    except Exception:
        print('get_time_to_metro error')
    print('time to metro on foot: ', flat.time_to_metro_on_foot)
    print('time to metro by transport: ', flat.time_to_metro_by_transport)

    try:
        flat.get_bathroom()
    except Exception:
        print('get_bathroom error')
    print('combined bathroom: ', flat.is_combined_bathroom)
    print('separate bathroom: ', flat.is_separate_bathroom)
    print('number of bathrooms: ', flat.number_of_bathrooms)


    try:
        flat.get_flat_type()
    except Exception:
        print('get_type error')
    print('type: ', flat.flat_type)

    try:
        flat.get_planning()
    except Exception:
        print('get_planning error')
    print('planning: ', flat.planning)

    try:
        flat.get_ceiling_height()
    except Exception:
        print('get_ceiling_height error')
    print('ceiling height: ', flat.ceiling_height)

    try:
        flat.get_balcony()
    except Exception:
        print('get_balcony error')

    try:
        flat.get_repair()
    except Exception:
        print('get_repair error')
    print('repair: ', flat.repair)

    try:
        flat.get_view()
    except Exception:
        print('get_view error')
    print('view: ', flat.view)

    try:
        flat.get_year_of_construction()
        print('year of construction: ', flat.year_of_construction)
    except Exception:
        print('get_year_of_construction error')

    try:
        flat.get_house_type()
        print('house type: ', flat.house_type)
    except Exception:
        print('get_house_type error')

    try:
        flat.get_overlap_type()
        print('overlap type: ', flat.overlap_type)
    except Exception:
        print('get_overlap_type error')

    try:
        flat.get_entrances_number()
        print('entrances number: ', flat.entrances_number)
    except Exception:
        print('get_entrances_number error')

    try:
        flat.get_elevators()
    except Exception:
        print('get_elevators error')

    try:
        flat.get_heating()
        print('heating: ', flat.heating)
    except Exception:
        print('get_heating error')

    try:
        flat.get_accident_rate()
        print('accident rate: ', flat.accident_rate)
    except Exception:
        print('get_accident_rate error')

    try:
        flat.get_parking()
        print('parking: ', flat.parking)
    except Exception:
        print('get_parking error')

    try:
        flat.get_garbage_chute()
        print('garbage: ', flat.garbage_chute)
    except Exception:
        print('get_garbage error')


    print('========')
    time.sleep(2)

    # write to csv
    with open('flats.csv', 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')

        filewriter.writerow([link,
                             flat.metro,
                             flat.square_meters_total,
                             flat.square_meters_living,
                             flat.square_meters_kitchen,
                             flat.current_floor,
                             flat.total_floors,
                             flat.city,
                             flat.district,
                             flat.neighborhood,
                             flat.street,
                             flat.house_number,
                             flat.time_to_metro_on_foot,
                             flat.time_to_metro_by_transport,
                             flat.number_of_bathrooms,
                             flat.is_combined_bathroom,
                             flat.is_separate_bathroom,
                             flat.flat_type,
                             flat.planning,
                             flat.ceiling_height,
                             flat.balcony_quantity,
                             flat.loggia_quantity,
                             flat.repair,
                             flat.view,
                             flat.year_of_construction,
                             flat.house_type,
                             flat.overlap_type,
                             flat.entrances_number,
                             flat.cargo_elevators_quantity,
                             flat.passengers_elevators_quantity,
                             flat.heating,
                             flat.accident_rate,
                             flat.parking,
                             flat.garbage_chute,
                             flat.gas_suply])

    # delete link
    #links_to_flats.remove(i)


# если в текущей пачке больше ссылок не осталось, то надо получить следующую порцию
# if len(links_to_flats) == 0:
#     get_next_links_pack()
# else:
#     print('some links didnt proceeded')







# flat.get_square_meters_living_room()
# print('living square', flat.square_meters_living_room)

