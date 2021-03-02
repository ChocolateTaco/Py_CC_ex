# This test imports the city_functions to determine if its behaving correctly

import unittest
from city_functions import citycountry

class CityCountryTC(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does 'Santiago, Chile' work?"""
        formatted_city = citycountry('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()