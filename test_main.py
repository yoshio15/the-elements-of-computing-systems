from unittest import TestCase
import main


class TestMain(TestCase):

    def test_nand(self):
        self.assertEqual(True, main.nand(0, 0))
        self.assertEqual(True, main.nand(1, 0))
        self.assertEqual(True, main.nand(0, 1))
        self.assertEqual(False, main.nand(1, 1))
