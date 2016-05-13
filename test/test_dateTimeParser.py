from unittest import TestCase

from DateTimeParser import DateTimeParser


class TestDateTimeParser(TestCase):
    def setUp(self):
        self.dateTimeParser = DateTimeParser()

    def test_parse_shouldParseDate_whenDate1Given(self):
        date = self.dateTimeParser.parse('19/Jan/2016:18:02:21 +0100')
        self.assertEqual(date.day, 19)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.year, 2016)
        self.assertEqual(date.hour, 18)
        self.assertEqual(date.minute, 2)
        self.assertEqual(date.second, 21)

    def test_parse_shouldParseDate_whenDate2Given(self):
        date = self.dateTimeParser.parse('04/May/2016:21:48:12 +0200')
        self.assertEqual(date.day, 4)
        self.assertEqual(date.month, 5)
        self.assertEqual(date.year, 2016)
        self.assertEqual(date.hour, 21)
        self.assertEqual(date.minute, 48)
        self.assertEqual(date.second, 12)
