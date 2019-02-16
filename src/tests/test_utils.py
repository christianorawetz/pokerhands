import unittest

from utils import all_consecutive


class TestPokerUtils(unittest.TestCase):

    def test_all_consecutive(self):
        self.assertTrue(all_consecutive([8, 4, 5, 6, 7]))

    def test_all_not_consecutive(self):
        self.assertFalse(all_consecutive([13, 4, 5, 6, 7]))
