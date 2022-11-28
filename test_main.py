#
# Tests for main.py
#
import unittest

import main


INITIAL_LAYOUT = """\
Airplane Layout
===============
 0  0  0     0  0  0  0     0  0     0  0  0
 0  0  0     0  0  0  0     0  0     0  0  0
             0  0  0  0     0  0     0  0  0
                                     0  0  0\
"""

FINAL_LAYOUT = """\
Airplane Layout
===============
19 25  1     2 26 27  3     4  5     6 28 20
21 29  7     8 30  0  9    10 11    12  0 22
            13  0  0 14    15 16    17  0 23
                                    18  0 24\
"""


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

    def test_successful_layout(self):
        airplane = main.Airplane([[3, 2], [4, 3], [2, 3], [3, 4]], 30)
        initial_layout = str(airplane)
        self.assertEqual(initial_layout, INITIAL_LAYOUT)
        airplane.fill()
        final_layout = str(airplane)
        self.assertEqual(final_layout, FINAL_LAYOUT)


if __name__ == "__main__":
    unittest.main()
