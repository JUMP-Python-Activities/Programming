import unittest 
from unittest.mock import patch
from io import StringIO
from sys import stdin

from Programming import programming

class TestUserInput(unittest.TestCase):

    
    def setUp(self):
       # with patch.object(stdin,attribute='Mark\n30\n10\nPython C++ Assembly\nPython Java MySQL') as mock :
        self.first3 = ('Python', 'C++', "Assembly")
        self.fav3 = ['Python', 'Java', 'MySQL']
        self.best = {"Python"}

    @patch('sys.stdin', StringIO('Mark\n30\n10\nPython C++ Assembly\nPython Java MySQL'))
    def test_dict(self):
        data = programming()
        self.assertIsInstance(data, dict)

    @patch('sys.stdin', StringIO('Mark\n30\n10\nPython C++ Assembly\nPython Java MySQL'))
    def test_tuple(self):
        self.data = programming()
        self.assertIsInstance(self.data['first three'], tuple)
    
    @patch('sys.stdin', StringIO('Mark\n30\n10\nPython C++ Assembly\nPython Java MySQL'))
    def test_tuple_content(self):
        self.data = programming()
        self.assertEqual(self.data['first three'], self.first3)

    @patch('sys.stdin', StringIO('Mark\n30\n10\nPython C++ Assembly\nPython Java MySQL'))
    def test_list(self):
        self.data = programming()
        self.assertIsInstance(self.data["fav three"], list)

    @patch('sys.stdin', StringIO('Mark\n30\n10\nPython C++ Assembly\nPython Java MySQL'))
    def test_list_content(self):
        self.data = programming()
        self.assertEqual(self.data['fav three'], self.fav3)

    @patch('sys.stdin', StringIO('Mark\n30\n10\nPython C++ Assembly\nPython Java MySQL'))
    def test_set(self):
        self.data = programming()
        self.assertIsInstance(self.data["best language"], set)

    @patch('sys.stdin', StringIO('Mark\n30\n10\nPython C++ Assembly\nPython Java MySQL'))
    def test_set_content(self):
        self.data = programming()
        self.assertEqual(self.data["best language"], self.best)

    
    
if __name__ == '__main__':
    unittest.main()