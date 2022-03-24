import unittest
from main import people, shelf, delete, adds
from data import *

class TestSomething(unittest.TestCase):
    def setUp(self):
        print('method setUp')

    def test_people_1(self):
        self.assertEqual(people(documents, '10006'), "Аристарх Павлов")

    def test_people_2(self):
        self.assertEqual(people(documents, '111'), 'Нет такого номера документа')

    def test_shelf_1(self):
        self.assertEqual(shelf(directories, '2207 876234'), '1')

    def test_delete(self):
        delete(documents, directories, '11-2')
        self.assertNotIn('11-2', documents)
        self.assertNotIn('11-2', directories)

    def test_adds(self):
        adds(documents, directories, 'DOC_TYPE', '12345678', 'somebody', '3')
        self.assertIn('12345678', documents and directories['3'])

    def tearDown(self):
        print('method tearDown')

if __name__ == '__main__':
    unittest.main()