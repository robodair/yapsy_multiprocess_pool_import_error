import unittest
from . import main_program

class Test(unittest.TestCase):

    def test_main(self):
        out = main_program.main()
        self.assertEqual(out, "")
