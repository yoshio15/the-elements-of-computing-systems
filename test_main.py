from unittest import TestCase
import main


class TestMain(TestCase):

    def test_nand(self):
        self.assertEqual(True, main.nand(0, 0))
        self.assertEqual(True, main.nand(1, 0))
        self.assertEqual(True, main.nand(0, 1))
        self.assertEqual(False, main.nand(1, 1))

    def test_not_func(self):
        self.assertEqual(True, main.not_func(0))
        self.assertEqual(False, main.not_func(1))

    def test_or_func(self):
        self.assertEqual(False, main.or_func(0, 0))
        self.assertEqual(True, main.or_func(0, 1))
        self.assertEqual(True, main.or_func(1, 0))
        self.assertEqual(True, main.or_func(1, 1))

    def test_xor(self):
        self.assertEqual(False, main.xor(0, 0))
        self.assertEqual(True, main.xor(0, 1))
        self.assertEqual(True, main.xor(1, 0))
        self.assertEqual(False, main.xor(1, 1))
