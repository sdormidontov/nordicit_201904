import requests
from bs4 import BeautifulSoup


class Flat(object):
    def __init__(self):
        self.metro = ''
        self.square_meters = 0.0
        self.content = ''
        self.soup = None

    def get_content(self, link):
        flat = requests.get(link)
        if flat.ok:
            soup = BeautifulSoup(flat.text, 'lxml')
            self.content = self.soup.contents
        else:
            print('Bad request')

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

    def get_square_meters(self):
        square_meters = self.soup.findAll('div', class_="a10a3f92e9--info-text--2uhvD")[0].text
        print(square_meters)


flat = Flat()
flat.get_content_from_file(
    'flat1.txt'
)

flat.get_metro()
flat.get_square_meters()