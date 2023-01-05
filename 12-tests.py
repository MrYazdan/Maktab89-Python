import unittest
from string import ascii_letters


class AlphabetTesting(unittest.TestCase):
    def setUp(self) -> None:
        print("Setup called !")

    def test_alphabet(self):
        self.assertIn("A", ascii_letters)
        print("Test 1 - Passed !")

    def test_beta(self):
        self.assertNotIn('Milad', ascii_letters)
        print("Test 2 - Passed !")

    @staticmethod
    def division(a, b):
        return a / b

    @staticmethod
    def day_status():
        import datetime
        if datetime.datetime.now().hour < 12:
            return "am"
        return "pm"

    def test_three(self):
        self.assertRaises(ZeroDivisionError, self.division, 3,  0)

    def tearDown(self) -> None:
        print("TearDown Called !")


if __name__ == "__main__":
    unittest.main()
# unittest.main()
