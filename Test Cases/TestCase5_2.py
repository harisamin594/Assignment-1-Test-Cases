#Test Case 5 (2)

import unittest

from TestCase5_1 import area

class TestTriangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2,4),5)

unittest.main()
