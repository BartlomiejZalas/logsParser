from datetime import datetime


class DateTimeParser:
    def parse(self, dateAsString):
        return datetime.strptime(dateAsString, '%d/%b/%Y:%H:%M:%S %z')
