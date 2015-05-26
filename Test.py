import unittest
import Main

class TestStringMethods(unittest.TestCase):

  def test(self):
    self.assertEqual(Main.sum(1,2), 2)

  # def test_upper(self):
  #     self.assertEqual('foo'.upper(), 'FOO')

  # def test_isupper(self):
  #     self.assertTrue('FOO'.isupper())
  #     self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()
