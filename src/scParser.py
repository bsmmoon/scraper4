import re


class scParser:
    def __init__(self):
        print("scParser")

    def run(self, html):
        table = self.findTable(html)
        for i in range(0, 5):
            print(table[i])
        return table

    def pruneRow(self, row):
        return [row[0], row[2], row[3], row[4], row[5]]

    def findTable(self, html):
        html = html.replace("\n", "")
        html = self.find(html, "<table>", "</table>")
        table = re.findall("<tr(.*?)</tr", html)
        result = []
        for i in range(1, len(table)):
            row = table[i]
            row = re.findall(">(.*?)<", row)
            row = list(filter(lambda x: len(x.strip()) > 0, row))
            result.append(self.pruneRow(row))
        return result

    def find(self, text, front, back):
        startIdx = text.find(front) + len(front)
        offset = text[startIdx:].find(back)
        endIdx = startIdx + offset
        return text[startIdx:endIdx]
