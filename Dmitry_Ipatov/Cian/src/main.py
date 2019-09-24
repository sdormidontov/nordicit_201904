from bs4 import BeautifulSoup
import requests
import time
import src.flat as f
import csv
import src.page_urls as page_urls
import random
import datetime


# получение страниц, например с 1 по 3
pages = page_urls.get_page_urls_list(10, 50)

print(pages)

for page in pages:
    url = page
    # url = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&region=1&room1=1&room2=1'
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

        # links_to_flats = ['https://www.cian.ru/sale/flat/211834401/',
                          # 'https://www.cian.ru/sale/flat/212633712/',
                          # 'https://www.cian.ru/sale/flat/212836793/',
                          # 'https://www.cian.ru/sale/flat/200112159/',  # рядом с 4мя станциями
                          # 'https://krasnogorsk.cian.ru/sale/flat/213030063/'
                          # ]  # время до метро на транспорте

        for i in links:
            link = i
            print('обработка квартиры {} из {}'.format(links.index(i), len(links)), i)
            flat = f.Flat()
            flat.get_content(link)
            now = datetime.datetime.now()

            try:
                flat.get_metro()
                print('Метро: ', flat.metro)
            except Exception:
                print('get_metro error')

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

            try:
                flat.get_gas_suply()
                print('gas: ', flat.gas_suply)
            except Exception:
                print('get_gas_suply error')

            try:
                flat.get_description()
            except Exception:
                print('get_description error')

            try:
                flat.get_price()
                print('price: ', flat.price)
            except Exception:
                print('get_price error')

            print('========')
            sleep = random.randint(100, 120)
            time.sleep(sleep)

            # write to csv
            with open('flats_9.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',')

                filewriter.writerow([url,
                                     links.index(i),
                                     link,
                                     now.strftime("%Y-%m-%d %H:%M:%S"),
                                     flat.metro,  # метро
                                     flat.square_meters_total,  # общая площадь
                                     flat.square_meters_living,  # жилая площадь
                                     flat.square_meters_kitchen,  # площадь кухни
                                     flat.current_floor,  # этаж
                                     flat.total_floors,  # всего этажей в доме
                                     flat.city,  # город
                                     flat.district,  # округ
                                     flat.neighborhood,  # район
                                     flat.street,  # улица
                                     flat.house_number,  # дом
                                     flat.time_to_metro_on_foot,  # время до метро пешком
                                     flat.time_to_metro_by_transport,  # время до метро на транспорте
                                     flat.number_of_bathrooms,  # кол-во санузлов
                                     flat.is_combined_bathroom,  # совмещенный санузел
                                     flat.is_separate_bathroom,  # раздельный санузел
                                     flat.flat_type,  # тип жилья - Первичка и т д
                                     flat.planning,  # планировка
                                     flat.ceiling_height,  # высота потолков
                                     flat.balcony_quantity,  # кол-во балконов
                                     flat.loggia_quantity,  # кол-во лоджий
                                     flat.repair,  # ремонт
                                     flat.view,  # вид
                                     flat.year_of_construction,  # год постройки
                                     flat.house_type,  # тип дома
                                     flat.overlap_type,  # тип перекрытий
                                     flat.entrances_number,  # кол-во подъездов
                                     flat.cargo_elevators_quantity,  # кол-во грузовых лифтов
                                     flat.passengers_elevators_quantity,  # кол-во пассажирских лифтов
                                     flat.heating,  # отопление
                                     flat.accident_rate,  # аварийность
                                     flat.parking,  # парковка
                                     flat.garbage_chute,  # мусоропровод
                                     flat.gas_suply,  # газоснабжение
                                     flat.description,
                                     flat.price])

    else:
        print('Bad request')






    # получение ссылок на квартиры на данной странице


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








# обрабатываем ссылки в файле



