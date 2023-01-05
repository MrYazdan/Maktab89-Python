import unittest


class BankAccount:
    def __init__(self, username):
        if type(username) != str:
            raise ValueError("Username invalid !")


class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.class_object = BankAccount

    def test_username(self):
        self.assertRaises(ValueError, self.class_object, 9342343)
        self.assertRaises(Exception, self.class_object, True)


if __name__ == "__main__":
    unittest.main()
