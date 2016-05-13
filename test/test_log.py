from datetime import datetime
from unittest import TestCase

from Log import Log


class TestLog(TestCase):
    def test_str_shouldGenerateNiceStringXD(self):
        date = datetime.today()

        log = Log('a', 'b', 'c', date, 'e', 'f', '8', '7', 'i')

        self.assertEqual('a, b, c, '+date.strftime("%d/%b/%Y:%H:%M:%S %z")+', e, f, 8, 7, i', log.__str__())
