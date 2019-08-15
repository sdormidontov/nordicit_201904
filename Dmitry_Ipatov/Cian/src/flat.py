import requests
from bs4 import BeautifulSoup


class Flat(object):
    def __init__(self):
        self.metro = ''
        self.square_meters_total = 0.0
        square_meters_living_room = 0.0
        self.content = ''
        self.soup = None


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




