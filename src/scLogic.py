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
        urls = self.makeUrls(year)

        for url in urls:
            html = self.scrapper.run(url)
            data = self.parser.run(html)
            self.storage.run(data)

    def makeUrls(self, year):
        urls = []
        categories = ["K", "E"]
        for category in categories:
            urls.append("http://www.gaonchart.co.kr/main/section/chart/album.gaon?termGbn=year&hitYear={}&targetTime=13&nationGbn={}".format(year, category))
        return urls
