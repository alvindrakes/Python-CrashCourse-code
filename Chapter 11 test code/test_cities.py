import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """do values like 'santiago', 'chille' work?"""
        final = city_country('santiago', 'chille')
        self.assertEqual(final, 'Santiago Chille' )

    def test_city_country_population(self):
        """Do values like kajang, malaysia, 5000 work?"""
        final = city_country('kajang', 'malaysia', 5000)
        self.assertEqual(final, 'Kajang Malaysia Population: 5000')

unittest.main()