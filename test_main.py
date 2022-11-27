#
# Tests for main.py
#
import unittest

import main


class TestAirplaneSeating(unittest.TestCase):
    def test_input(self):

        # Check if the passenger input is not an integer
        with self.assertRaises(TypeError):
            main.AirplaneSeating([1, 2, 3], "volopay")

        # Check if the passenger input is negative integer
        with self.assertRaises(ValueError):
            main.AirplaneSeating([1, 2, 3], -1)

        # Check if the passenger input is empty
        with self.assertRaises(ValueError):
            main.AirplaneSeating([1, 2, 3], None)

        # Check if the array input is empty
        with self.assertRaises(ValueError):
            main.AirplaneSeating([], 20)

        # Check if the array input is a sequence
        with self.assertRaises(TypeError):
            main.AirplaneSeating(10, 20)


if __name__ == "__main__":
    unittest.main()
