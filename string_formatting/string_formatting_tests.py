import unittest

from string_formatting import *


class TestReturnString(unittest.TestCase):
    def testReturnsTypeString(self):
        result = return_string()
        self.assertTrue(isinstance(result, str))

    def testReturnsTheStringHelloWorld(self):
        expected = "Hello World"
        result = return_string()
        self.assertEqual(result, expected)


class TestReturnsTheStringPassedIn(unittest.TestCase):
    def testReturnsTypeString(self):
        result = returns_string_passed_in()
        self.assertTrue(isinstance(result, str))

    def testReturnsTheStringPassedIn(self):
        value = "Hello Moon"
        result = returns_string_passed_in(value)
        self.assertEqual(result, value)

    def testReturnsADefaultValue(self):
        value = "default"
        result = returns_string_passed_in()
        self.assertEqual(result, value)


class TestReturnsAStingOfValuesPassedIn(unittest.TestCase):
    def testReturnsTypeString(self):
        value_one = "Hello"
        value_two = "World"
        result = return_a_string_of_values(value_one, value_two)
        self.assertTrue(isinstance(result, str))

    def testReturnsTheStringHelloWorld(self):
        value_one = "Hello"
        value_two = "World"
        expected = "Hello World"
        result = return_a_string_of_values(value_one, value_two)
        self.assertEqual(result, expected)

    def testReturnsTheStringHelloWorldPython(self):
        value_one = "Hello"
        value_two = "World"
        value_three = "Python"
        expected = "Hello World Python"
        result = return_a_string_of_values(value_one, value_two, value_three)
        self.assertEqual(result, expected)


class TestPythonStringFormat(unittest.TestCase):

    def testReturnsTypeString(self):
        result = return_customer_account_balance()
        self.assertTrue(isinstance(result, str))

    def testCustomerAccountBalance(self):
        name = 'Timothy Doolan'
        account_number = 12345678
        account_balance = 253.34789524
        customer_account_balance = return_customer_account_balance(name, account_number, account_balance)
        self.assertEqual(customer_account_balance, "Hi Timothy Doolan of account 12345678 your balance is 253.35")


if __name__ == '__main__':
    unittest.main()
