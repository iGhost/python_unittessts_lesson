from unittest import TestCase

from functions.plus import plus


class PlusFunctionTestCase(TestCase):
    def test_1_plus_1_returns_2(self):
        self.assertTrue(2, plus(1, 1))

    def test_5_plus_5_is_10(self):
        self.assertEqual(10, plus(5, 5))

    def test_1555_plus_445_is_2000(self):
        self.assertEqual(2000, plus(1555, 445))

