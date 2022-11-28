#
# Tests for main.py
#
import unittest

import main


class TestAirplane(unittest.TestCase):
    def test_input(self):

        # Check if the passenger input is not an integer
        with self.assertRaises(TypeError):
            main.Airplane(None, "volopay")

        # Check if dims are in the correct format
        with self.assertRaises(ValueError):
            main.Airplane([1, 2, 3], 3)


        # Check if the passenger input is a number
        with self.assertRaises(TypeError):
            main.Airplane([[1, 2]], None)

        # Check if the passenger input is negative integer
        with self.assertRaises(ValueError):
            main.Airplane([[1, 2]], -3)

        # Check if the array input is empty
        with self.assertRaises(ValueError):
            main.Airplane([], 20)

        # Check if we have enough capacity
        with self.assertRaises(ValueError):
            main.Airplane([[3, 2], [4, 3], [2, 3], [3, 4]], 37)


if __name__ == "__main__":
    unittest.main()
