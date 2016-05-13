import re

from DateTimeParser import DateTimeParser
from Log import Log

REGEX = '^(\S+) (\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S+)?\s*" (\d{3}) (\S+) "(.*?)" "(.*?)"'


class LineLogParser:
    def parseLine(self, line):

        data = re.match(REGEX, line).groups()
        client_ip = data[1]
        client_identd = data[2]
        user_id = data[3]
        date_time = DateTimeParser().parse(data[4])
        request_type = data[5]
        requested_resource = data[6]
        response_code = self.parseToIntOrZero(data[8])
        content_size = self.parseToIntOrZero(data[9])
        agent = data[11]

        return Log(client_ip, client_identd, user_id, date_time, request_type, requested_resource, response_code,
                   content_size, agent)

    def parseToIntOrZero(self, value):

        if value == '-':
            return 0
        else:
            return int(value)
