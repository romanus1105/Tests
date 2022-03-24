import unittest
from getpass import getpass
from main import YaDisk

yd = YaDisk(getpass("Введите Я.Диск-токен: "))

class TestSomething(unittest.TestCase):
    def test_response(self):
        self.assertEqual(str(yd.yd_folder_create('tmp_dir')), '<Response [409]>')

    def test_folder_appearence(self):
        self.assertIn('tmp_dir', yd.checking_avaliability())

if __name__ == '__main__':
    unittest.main()