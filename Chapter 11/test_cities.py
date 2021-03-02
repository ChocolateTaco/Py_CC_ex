# This test imports the city_functions to determine if its behaving correctly

import unittest
from city_functions import citycountry

class CityCountryTC(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does 'Santiago, Chile' work?"""
        formatted_city = citycountry('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does 'Santiago, Chile, 5000000' work?"""
        formatted_city = citycountry('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()