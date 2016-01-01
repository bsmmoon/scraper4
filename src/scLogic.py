from scScrapper import scScrapper
from scParser import scParser
from scStorage import scStorage


class scLogic:
    def __init__(self):
        print("scLogic")
        self.scrapper = scScrapper()
        self.parser = scParser()
        self.storage = scStorage()

    def run(self, year):
        addresses = self.makeAddresses(year)
        print(addresses)

        for address in addresses:
            source = self.scrapper.run(address)
            data = self.parser.run(source)
            self.storage.run(data)

    def makeAddresses(self, year):
        addresses = []
        categories = ["K", "E"]
        for category in categories:
            addresses.append("http://www.gaonchart.co.kr/main/section/chart/album.gaon?termGbn=year&hitYear={}&targetTime=13&nationGbn={}".format(year, category))
        return addresses
