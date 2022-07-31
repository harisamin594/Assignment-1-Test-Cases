#Test Case 5 (2)

import unittest

from TestCase5_1 import area

class TestTriangle(unittest.TestCase):

    def setUp(self):
       
        print("Setup Executed")

    def testc(self):
       
        self.assertEqual(add(9,9),18)

    def tearDown(self):
            
        print("Teardown Executed")
        
unittest.main()
