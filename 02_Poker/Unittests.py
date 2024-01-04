import unittest
from Poker import *


class TestPokerMethods(unittest.TestCase):

    def test_paar(self):
        self.assertTrue(paar([(0, 1), (1, 1), (0, 8), (0, 9), (0, 10)]))
        self.assertFalse(paar([(0, 1), (1, 11), (0, 8), (0, 9), (0, 10)]))
        self.assertFalse(paar([(0, 1), (0, 11), (0, 8), (0, 9), (0, 10)]))

    def test_2paar(self):
        self.assertTrue(zweipaar([(0, 1), (1, 1), (0, 8), (1,8), (0, 10)]))
        self.assertFalse(zweipaar([(0, 1), (0, 1), (0, 8), (0, 9), (0, 10)]))

    def test_drilling(self):
        self.assertTrue(drilling([(0, 1), (1, 1), (2, 1), (1, 8), (0, 10)]))
        self.assertFalse(drilling([(0, 1), (0, 1), (0, 8), (0, 9), (0, 10)]))

    def test_straight(self):
        self.assertTrue(straight([(0, 6), (2, 2), (1, 3), (3, 4), (0, 5)]))
        self.assertFalse(straight([(0, 1), (1, 0), (0, 12), (0, 11), (0, 10)]))
        self.assertFalse(straight([(0, 1), (1, 1), (0, 8), (0, 9), (0, 10)]))

    def test_flush(self):
        self.assertTrue(flush([(0, 6), (0, 0), (0, 12), (0, 9), (0, 5)]))
        self.assertFalse(flush([(0, 1), (1, 1), (0, 8), (0, 9), (0, 10)]))

    def test_fullhouse(self):
        self.assertTrue(fullhouse([(1, 0), (0, 0), (2, 0), (0, 9), (1, 9)]))
        self.assertFalse(fullhouse([(0, 1), (1, 1), (0, 8), (0, 9), (0, 10)]))

    def test_vierling(self):
        self.assertTrue(vierling([(1, 0), (0, 0), (2, 0), (3, 0), (1, 9)]))
        self.assertFalse(vierling([(0, 1), (1, 1), (0, 8), (0, 9), (0, 10)]))

    def test_straightflush(self):
        self.assertTrue(straight_flush([(0, 6), (0, 7), (0, 8), (0, 9), (0, 10)]))
        self.assertFalse(straight([(0, 1), (0, 0), (0, 12), (0, 11), (0, 10)]))
        self.assertFalse(straight_flush([(0, 1), (1, 1), (0, 8), (0, 9), (0, 10)]))

    def test_royaleflush(self):
        self.assertTrue(royale_flush([(0, 0), (0, 12), (0, 11), (0, 10), (0, 9)]))
        self.assertFalse(royale_flush([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]))
        self.assertFalse(royale_flush([(0, 1), (1, 1), (0, 8), (0, 9), (0, 10)]))


if __name__ == '__main__':
    unittest.main()
