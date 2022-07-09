"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test de Calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        result = calc.add(1, 2)

        self.assertEqual(result, 3)

    def test_subtract_numbers(self):
        """Test substracting numbers"""
        result = calc.subtract(5, 2)

        self.assertEqual(result, 3)