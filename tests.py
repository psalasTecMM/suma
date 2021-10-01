import unittest


class SumaTestCase(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(5, 3), 8)


if __name__ == '__main__':
    unittest.main()
