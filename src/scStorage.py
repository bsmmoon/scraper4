import os


class scStorage:
    def __init__(self):
        print("scStorage")
        self.dataDir = "./data"
        self.fileName = "/result.csv"
        self.fileDirectory = self.dataDir + self.fileName
        self.writeData(self.fileDirectory, "")

    def run(self, lhs, data):
        self.ensure_dir(self.dataDir)
        self.ensure_file(self.fileDirectory)
        self.appendData(self.fileDirectory, self.tableToString(lhs, data))

    def tableToString(self, lhs, table):
        result = ''
        for row in table:
            result += ';'.join(lhs)
            result += ';'
            result += ';'.join(row)
            result += '\n'
        return result

    def ensure_file(self, fileDirectory):
        if not os.path.isfile(fileDirectory):
            self.writeData(fileDirectory, "")

    def ensure_dir(self, directory):
        if not os.path.isdir(directory):
            os.makedirs(directory)
            return False
        else:
            return True

    def writeData(self, fileDirectory, text):
        with open(fileDirectory, 'w', encoding='UTF-8') as f:
            f.write(text)

    def appendData(self, fileDirectory, text):
        with open(fileDirectory, 'a', encoding='UTF-8') as f:
            f.write(text)
