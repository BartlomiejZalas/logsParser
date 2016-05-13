from unittest import TestCase

import datetime

from LineLogParser import LineLogParser


class TestLineLogParser(TestCase):
    def setUp(self):
        self.lineLogParser = LineLogParser()

    def test_parseLine(self):
        line = '13.sesja.linuksowa.pl:80 192.168.0.1 - - [19/Jan/2016:18:02:21 +0100] "GET / HTTP/1.0" 403 179 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.106 Chrome/47.0.2526.106 Safari/537.36"'

        log = self.lineLogParser.parseLine(line)

        self.assertEqual(log.client_ip, '192.168.0.1')
        self.assertEqual(log.client_identd, '-')
        self.assertEqual(log.user_id, '-')
        self.assertEqual(log.date_time.day, 19)
        self.assertEqual(log.date_time.month, 1)
        self.assertEqual(log.date_time.year, 2016)
        self.assertEqual(log.date_time.hour, 18)
        self.assertEqual(log.date_time.minute, 2)
        self.assertEqual(log.date_time.second, 21)
        self.assertEqual(log.request_type,'GET')
        self.assertEqual(log.requested_resource, '/')
        self.assertEqual(log.response_code, 403)
        self.assertEqual(log.content_size, 179)
        self.assertEqual(log.agent, 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.106 Chrome/47.0.2526.106 Safari/537.36')


    def test_parseLine_whenThereIsNoSize(self):
        line = '13.sesja.linuksowa.pl:80 192.168.0.1 - - [19/Jan/2016:18:02:21 +0100] "GET / HTTP/1.0" 403 - "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.106 Chrome/47.0.2526.106 Safari/537.36"'

        log = self.lineLogParser.parseLine(line)

        self.assertEqual(log.client_ip, '192.168.0.1')
        self.assertEqual(log.client_identd, '-')
        self.assertEqual(log.user_id, '-')
        self.assertEqual(log.date_time.day, 19)
        self.assertEqual(log.date_time.month, 1)
        self.assertEqual(log.date_time.year, 2016)
        self.assertEqual(log.date_time.hour, 18)
        self.assertEqual(log.date_time.minute, 2)
        self.assertEqual(log.date_time.second, 21)
        self.assertEqual(log.request_type, 'GET')
        self.assertEqual(log.requested_resource, '/')
        self.assertEqual(log.response_code, 403)
        self.assertEqual(log.content_size, 0)
        self.assertEqual(log.agent,
                         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.106 Chrome/47.0.2526.106 Safari/537.36')