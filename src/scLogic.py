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
        categories = ["K", "E"]
        urls = self.makeUrls(year, categories)

        for index in range(len(urls)):
            url = urls[index]
            html = self.scrapper.run(url)
            data = self.parser.run(html)
            lhs = [categories[index], str(year)]
            self.storage.run(lhs, data)

    def makeUrls(self, year, categories):
        urls = []
        for category in categories:
            urls.append("http://www.gaonchart.co.kr/main/section/chart/album.gaon?termGbn=year&hitYear={}&targetTime=13&nationGbn={}".format(year, category))
        return urls
