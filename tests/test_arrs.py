import unittest

from utils.arrs import get


spisok = ["artem","Edem","Maksim"]
spisok2 = ["Кни́га","один","видов","печатной","продукции"]


class TestArrs(unittest.TestCase):
    
   def test_get(self):
        self.assertEqual(get(spisok,2,0), "Maksim")
        self.assertEqual(get(spisok,0,1), "artem")
    
   def test_my_slice(self):
        self.assertEqual(get(spisok2,0,1), ["Кни́га"])
        self.assertEqual(get(spisok2,0,3), ['Кни́га', 'один', 'видов'])


if __name__ == '__main__':
    unittest.main()