from scScrapper import scScrapper
from scParser import scParser
from scStorage import scStorage


class scLogic:
    def __init__(self):
        print('scLogic')
        self.scrapper = scScrapper()
        self.parser = scParser()
        self.storage = scStorage()

    def run(self):
        source = self.scrapper.run()
        data = self.parser.run(source)
        self.storage.run(data)
