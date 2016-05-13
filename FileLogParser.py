from LineLogParser import LineLogParser


class FileLogParser:
    def __init__(self):
        self.parser = LineLogParser()

    def parseFile(self, filename):
        lines = open(filename, "r")
        parsedLogs = []

        for line in lines:
            parsedLogs.append(self.parser.parseLine(line))

        return parsedLogs