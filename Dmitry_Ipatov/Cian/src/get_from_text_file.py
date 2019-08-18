from bs4 import BeautifulSoup
import requests


class Flat(object):
    def __init__(self):
        self.metro = ''
        self.square_meters_total = 0.0
        self.square_meters_living_room = 0.0
        self.content = ''
        self.soup = None


    def get_content_from_file(self, file):
        with open(file) as f:
            lst = []
            for row in f:
                lst.append(row)
            text = '\n'.join(lst)

        self.soup = BeautifulSoup(text, 'lxml')
        self.content = self.soup.contents

    def get_metro(self):
        metro = self.soup.findAll('a', class_="a10a3f92e9--underground_link--AzxRC")[0].text
        self.metro = metro






    def get_square_meters_total(self):
        text = self.soup.findAll('div', class_="a10a3f92e9--info-text--2uhvD")[0].text
        # '38,5 м²'
        square_meters = float(text.replace(',', '.').split(' ')[0])
        self.square_meters_total = square_meters

    def get_square_meters_living_room(self):
        text = self.soup.findAll('div', class_="a10a3f92e9--info-text--2uhvD")[0].text
        square_meters = float(text.replace(',', '.').split(' ')[0])
        self.square_meters_living_room = square_meters


    def float_from_square_meters(self, text):
        return float(text.replace(',', '.').split(' ')[0])


    def get_square(self):
        text = self.soup.findAll('div', class_="a10a3f92e9--info-block--3hCay")[0].text
        print(text)

        try:
            total = self.soup.find(text="Общая")
            tag = total.parent.parent
            text = tag.contents[0].text # 38,5 м²
            square_meters = self.float_from_square_meters(text)
            print('Total square: ',square_meters)
        except Exception:
            print('total square error')

        try:
            living = self.soup.find(text="Жилая")
            tag = living.parent.parent
            text = tag.contents[0].text
            square_meters = self.float_from_square_meters(text)
            print('Living square: ', square_meters)
        except Exception:
            print('living square error')

        try:
            kitchen = self.soup.find(text="Кухня")
            tag = kitchen.parent.parent
            text = tag.contents[0].text
            square_meters = self.float_from_square_meters(text)
            print('Kitchen: ', square_meters)
        except Exception:
            print('kitchen square error')


        try:
            floor = self.soup.find(text="Этаж")
            tag = floor.parent.parent
            text = tag.contents[0].text
            current_floor = (int(str.split(text, ' ')[0]))
            total_floors = (int(str.split(text, ' ')[-1]))
            print('Floor: ', current_floor)
            print('Floors total: ',total_floors)
        except Exception:
            print('floor error')



    def get_city(self):
        address = self.soup.findAll(class_='a10a3f92e9--link--1t8n1 a10a3f92e9--address-item--1clHr')
        self.city = address[0].text
        # print(address[0].text) Москва
        # print(address[1].text) ЮВАО
        # print(address[2].text) р-н Некрасовка
        # print(address[3].text) ул. Лавриненко
        # print(address[4].text) 5




    def get_time_to_metro_on_foot(self):
        time = self.soup.findAll('span', class_='a10a3f92e9--underground_time--1fKft')
        if 'пешком' in str(time).lower():
            print('ok')
            print((str(time)))
            print(str.strip(str.split(time[0].text)[1]))




    def get_type(self):
        type = self.soup.find(text='Тип жилья')
        tag = type.parent.nextSibling
        text = tag.contents[0]
        print(text)


    def get_bathroom(self):
        bathroom = self.soup.find(text='Санузел')
        tag = bathroom.parent.nextSibling
        text = tag.contents[0]
        print(str.split(text, ' ')[0])
        print(type(text))
        if 'раздел' in str(text).lower():
            print('p')
        elif 'совмещен' in str(text).lower():
            print('c')






f = Flat()
f.get_content_from_file('nekrasovka.txt')
# f.get_metro()
# f.get_square_meters_total()
# f.get_square_meters_living_room()
#f.get_square()

#f.get_time_to_metro_on_foot()

f.get_type()
#f.get_bathroom()



# print(f.metro)
# print(f.square_meters_total)
# print(f.square_meters_living_room)


# l = 'https://www.cian.ru/sale/flat/212633712/'
# flat = requests.get(l)
# soup = BeautifulSoup(flat.text, 'lxml')
# print(soup)

