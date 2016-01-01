import re


class scParser:
    def __init__(self):
        print("scParser")

    def run(self, html):
        table = self.findTable(html)
        return ""

    def findTable(self, html):
        html = html.replace("\n", "")
        html = self.find(html, "<table>", "</table>")
        table = re.findall("<tr(.*?)</tr", html)
        print(len(table))
        for index in range(len(table)):
            table[index] = re.findall("<td(.*?)</td", table[index])
        print(len(table[10]))
        return table

    def find(self, text, front, back):
        startIdx = text.find(front) + len(front)
        offset = text[startIdx:].find(back)
        endIdx = startIdx + offset
        return text[startIdx:endIdx]

    # def writeLog(self, text):
    #     with open('log.html', 'w', encoding='UTF-8') as f:
    #         f.write(text)
