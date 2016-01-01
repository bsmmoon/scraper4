import requests


class scScrapper:
    def __init__(self):
        print("scScrapper")

    def run(self, url):
        print(url)

        session = requests.Session()
        read = session.post(url)
        html = read.content.decode(read.encoding).strip()

        return html
