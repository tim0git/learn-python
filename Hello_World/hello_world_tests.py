import unittest

from hello_world import hello_world


class TestStringMethods(unittest.TestCase):
    s = hello_world()

    def test_upper(self, test_string=s):
        self.assertEqual(test_string, 'hello world')

    def test_is_not_upper(self, test_string=s):
        self.assertFalse(test_string.isupper())

    def test_is_type_string(self, test_string=s):
        self.assertTrue(isinstance('string', str))

    def test_split(self, test_string=s):
        self.assertEqual(test_string.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            test_string.split(2)


if __name__ == '__main__':
    unittest.main()
