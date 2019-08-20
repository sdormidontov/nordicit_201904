import requests
from bs4 import BeautifulSoup


class Flat(object):
    def __init__(self):
        self.content = ''
        self.soup = None

        self.metro = ''

        self.square_meters_total = 0.0
        self.square_meters_living = 0.0
        self.square_meters_kitchen = 0.0
        self.current_floor = 0
        self.total_floors = 0


        self.addressclass = 'a10a3f92e9--link--1t8n1 a10a3f92e9--address-item--1clHr'
        self.city = ''
        self.district = '' # административный округ
        self.neighborhood= '' # район
        self.street = ''
        self.house_number = 0

        self.time_to_metro_on_foot = 0
        self.time_to_metro_by_transport = 0

        self.is_combined_bathroom = False
        self.is_separate_bathroom = False
        self.number_of_bathrooms = 0

        self.flat_type = ''
        self.planning = ''
        self.ceiling_height = 0.0
        self.balcony_quantity = 0
        self.loggia_quantity = 0
        self.repair = ''
        self.view = ''

        self.year_of_construction = 0
        self.house_type = ''
        self.overlap_type = ''
        self.entrances_number = 0

        self.cargo_elevators_quantity = 0
        self.passengers_elevators_quantity = 0
        self.heating = ''
        self.accident_rate = ''
        self.parking = ''
        self.garbage_chute = ''
        self.gas_suply = ''




        # получение контента конкретной квартиры
    def get_content(self, link):
        flat = requests.get(link)
        if flat.ok:
            soup = BeautifulSoup(flat.text, 'lxml')

            self.soup = soup
            self.content = soup.contents

        else:
            print('Bad request')

    # def get_content_from_file(self, file):
    #     with open(file) as f:
    #         lst = []
    #         for row in f:
    #             lst.append(row)
    #         text = '\n'.join(lst)
    #
    #     self.soup = BeautifulSoup(text, 'lxml')
    #     self.content = self.soup.contents


    #text = self.soup.findAll('div', class_="a10a3f92e9--info-text--2uhvD")[0].text
    # '38,5 м²'
    #square_meters = self.float_from_square_meters(text)
    #self.square_meters_total = square_meters

    def float_from_square_meters(self, text):
        return float(text.replace(',', '.').split(' ')[0])


    def get_metro(self):
        metro = self.soup.findAll('a', class_="a10a3f92e9--underground_link--AzxRC")[0].text
        self.metro = metro

    def get_square_meters_total(self):
        total = self.soup.find(text="Общая")
        tag = total.parent.parent
        text = tag.contents[0].text  # 38,5 м²
        square_meters = self.float_from_square_meters(text)
        self.square_meters_total = square_meters


    def get_square_meters_living(self):
        living = self.soup.find(text="Жилая")
        tag = living.parent.parent
        text = tag.contents[0].text
        square_meters = self.float_from_square_meters(text)
        self.square_meters_living = square_meters

    def get_square_meters_kitchen(self):
        kitchen = self.soup.find(text="Кухня")
        tag = kitchen.parent.parent
        text = tag.contents[0].text
        square_meters = self.float_from_square_meters(text)
        self.square_meters_kitchen = square_meters

    def get_floor(self):
        floor = self.soup.find(text="Этаж")
        tag = floor.parent.parent
        text = tag.contents[0].text
        current_floor = (int(str.split(text, ' ')[0]))
        total_floors = (int(str.split(text, ' ')[-1]))
        self.current_floor = current_floor
        self.total_floors = total_floors




    def get_city(self):
        address = self.soup.findAll(class_= self.addressclass)
        self.city = address[0].text

    def get_district(self):
        address = self.soup.findAll(class_= self.addressclass)
        self.district = address[1].text

    def get_neighborhood(self):
        address = self.soup.findAll(class_= self.addressclass)
        self.neighborhood = address[2].text

    def get_street(self):
        address = self.soup.findAll(class_= self.addressclass)
        self.street = address[3].text

    def get_house_number(self):
        address = self.soup.findAll(class_= self.addressclass)
        self.house_number = address[4].text

    def get_time_to_metro(self):
        time = self.soup.findAll('span', class_='a10a3f92e9--underground_time--1fKft')
        if 'пешком' in str(time).lower():
            self.time_to_metro_on_foot = str.strip(str.split(time[0].text)[1])
        elif 'транспорт' in str(time).lower():
            self.time_to_metro_by_transport = str.strip(str.split(time[0].text)[1])


# ========= ОБЩАЯ ИНФОРМАЦИЯ ==========

    # Тип жилья - get_flat_type
    # Планировка - get_planning
    # Высота потолков - get_ceiling_height
    # Санузел - get_bathroom
    # Балкон/лоджия - get_balcony
    # Ремонт - get_repair
    # Вид из окон - get_view


    def get_flat_type(self):
        type = self.soup.find(text='Тип жилья')
        tag = type.parent.nextSibling
        self.flat_type = str(tag.contents[0])

    def get_planning(self):
        planning = self.soup.find(text='Планировка')
        tag = planning.parent.nextSibling
        self.planning = str(tag.contents[0])

    def get_bathroom(self):
        bathroom = self.soup.find(text='Санузел')
        tag = bathroom.parent.nextSibling
        text = tag.contents[0]
        self.number_of_bathrooms = (str.split(text, ' ')[0])
        if 'раздел' in str(text).lower():
            self.is_separate_bathroom = True
        elif 'совмещен' in str(text).lower():
            self.is_combined_bathroom = True

    def get_ceiling_height(self):
        ceiling_height = self.soup.find(text='Высота потолков')
        tag = ceiling_height.parent.nextSibling
        self.ceiling_height = float(
                (str.split(
                    str(tag.contents[0]), ' ')[0]
                ).replace(',', '.')
            )

    def get_balcony(self):
        balcony = self.soup.find(text='Балкон/лоджия')
        tag = balcony.parent.nextSibling
        s = str(tag.contents[0])
        lst = (s.split(' '))
        # https://stackoverflow.com/questions/13779526/finding-a-substring-within-a-list-in-python
        try:
            sub_balcony = 'балк'
            elem = next((s for s in lst if sub_balcony in s), None)
            self.balcony_quantity = int(lst[lst.index(elem) - 1])
        except Exception:
            print('no balcony info')

        try:
            sub_loggia = 'лодж'
            elem = next((s for s in lst if sub_loggia in s), None)
            self.loggia_quantity = int(lst[lst.index(elem) - 1])
        except Exception:
            print('no loggia info')

    def get_repair(self):
        repair = self.soup.find(text='Ремонт')
        tag = repair.parent.nextSibling
        self.repair = str(tag.contents[0])

    def get_view(self):
        view = self.soup.find(text='Вид из окон')
        tag = view.parent.nextSibling
        self.view = str(tag.contents[0])



# ========= О ДОМЕ ==========
#год постройки
    def get_year_of_construction(self):
        year_of_construction = self.soup.find(text='Год постройки')
        tag = year_of_construction.parent.nextSibling
        self.year_of_construction = int(tag.contents[0])


# тип дома
    def get_house_type(self):
        house_type = self.soup.find(text='Тип дома')
        tag = house_type.parent.nextSibling
        self.house_type = str(tag.contents[0])



# тип перекрытий
    def get_overlap_type(self):
        overlap_type = self.soup.find(text='Тип перекрытий')
        tag = overlap_type.parent.nextSibling
        self.overlap_type = str(tag.contents[0])

# число подъездов
    def get_entrances_number(self):
        entrances_number = self.soup.find(text='Подъезды')
        tag = entrances_number.parent.nextSibling
        self.entrances_number = int(tag.contents[0])

# лифты - пассажирский/грузовой
    def get_elevators(self):
        elevators = self.soup.find(text='Лифты')
        tag = elevators.parent.nextSibling
        s = str(tag.contents[0])
        lst = (s.split(' '))
        try:
            sub_cargo= 'грузов'
            elem = next((s for s in lst if sub_cargo in s), None)
            self.cargo_elevators_quantity = int(lst[lst.index(elem) - 1])
        except Exception:
            print('no cargo elevators info')

        try:
            sub_passengers = 'пассажирск'
            elem = next((s for s in lst if sub_passengers in s), None)
            self.passengers_elevators_quantity = int(lst[lst.index(elem) - 1])
        except Exception:
            print('no passenger elevators info')

# отопление
    def get_heating(self):
        heating = self.soup.find(text='Отопление')
        tag = heating.parent.nextSibling
        self.heating = str(tag.contents[0])

# аварийность
    def get_accident_rate(self):
        accident_rate = self.soup.find(text='Аварийность')
        tag = accident_rate.parent.nextSibling
        self.accident_rate = str(tag.contents[0])

# парковка
    def get_parking(self):
        parking = self.soup.find(text='Парковка')
        tag = parking.parent.nextSibling
        self.parking = str(tag.contents[0])

# мусоропровод
    def get_garbage_chute(self):
        garbage_chute = self.soup.find(text='Мусоропровод')
        tag = garbage_chute.parent.nextSibling
        self.garbage_chute = str(tag.contents[0])

#Газоснабжение
    def get_gas_suply(self):
        gas_suply = self.soup.find(text='Газоснабжение')
        tag = gas_suply.parent.nextSibling
        self.gas_suply = str(tag.contents[0])

#
# Полезные ссылки
# https://www.cian.ru/sale/flat/212633712/
# https://www.cian.ru/sale/flat/211834401/
# https://www.cian.ru/sale/flat/211180392/
# https://www.cian.ru/sale/flat/213792979/
# https://krasnogorsk.cian.ru/sale/flat/213030063/
# https://krasnogorsk.cian.ru/sale/flat/202139647/
# https://www.cian.ru/rent/flat/214273524/



