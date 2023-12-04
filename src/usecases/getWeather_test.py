import unittest
from ..infra.local.Weather_infra import WeatherRepository

class TestMathFunctions(unittest.TestCase):
    def test_get_last_5_datas(self):
        response = WeatherRepository().getAll(5)
        self.assertEqual(len(response),  5)

if __name__ == '__main__':
    unittest.main()