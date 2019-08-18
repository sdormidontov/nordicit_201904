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

        self.type = ''




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


# Общая информация

    # Тип жилья - get_type
    # Планировка
    # Высота потолков
    # Санузел - get_bathroom
    # Балкон/лоджия
    # Ремонт
    # Вид из окон

    def get_bathroom(self):
        bathroom = self.soup.find(text='Санузел')
        tag = bathroom.parent.nextSibling
        text = tag.contents[0]
        self.number_of_bathrooms = (str.split(text, ' ')[0])
        if 'раздел' in str(text).lower():
            self.is_separate_bathroom = True
        elif 'совмещен' in str(text).lower():
            self.is_combined_bathroom = True

    def get_type(self):
        type = self.soup.find(text='Тип жилья')
        tag = type.parent.nextSibling
        self.type = str(tag.contents[0])


#TODO добавить О Доме - год постройки и т д  - пример - https://krasnogorsk.cian.ru/sale/flat/213030063/




