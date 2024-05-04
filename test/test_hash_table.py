import unittest

from src.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.table = HashTable()
        self.table['AA'] = 1
        self.table['AAA'] = 2

    def test_getitem(self):
        self.assertEqual(self.table['AA'], 1)
        self.assertEqual(self.table['AAA'], 2)

    def test_getitem_key_error(self):
        self.assertRaises(KeyError, self.table.__getitem__, 'BB')
        self.assertRaises(KeyError, self.table.__getitem__, 'AAB')

    def test_setitem(self):
        self.table['BB'] = 3
        self.table['AAB'] = 4
        self.assertEqual(self.table['BB'], 3)
        self.assertEqual(self.table['AAB'], 4)

    def test_delitem(self):
        del self.table['AA']
        self.assertRaises(KeyError, self.table.__getitem__, 'AA')
