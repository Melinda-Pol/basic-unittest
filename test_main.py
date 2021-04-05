import unittest
import main

#Define a test block
class Testmain(unittest.TestCase):
    #Test the function from main
    def test_print(self):
        result = main.print_hi('there!')
        self.assertEqual(result,'Hi, there!')