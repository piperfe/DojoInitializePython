import unittest
import Main
from account_parser import AccountParser

class TestStringMethods(unittest.TestCase):

  def test(self):
    self.assertEqual(Main.sum(1,2), 3)

  # def test_upper(self):
  #     self.assertEqual('foo'.upper(), 'FOO')

  # def test_isupper(self):
  #     self.assertTrue('FOO'.isupper())
  #     self.assertFalse('Foo'.isupper())

  
#   def testShouldParseZeros(self):
#     input = " _  _  _  _  _  _  _  _  _ 
# | || || || || || || || || |
# |_||_||_||_||_||_||_||_||_|"
  def testShouldParseSingleZero(self):
    input = (
      " _ \n" +
      "| |\n" +
      "|_|\n" +
      "   \n")
    account_number = AccountParser().parse(input)
    self.assertEqual(account_number, "0")

  def testShouldParseSingleOne(self):
    input = (
      "   \n" +
      "  |\n" +
      "  |\n" +
      "   \n")
    account_number = AccountParser().parse(input)
    self.assertEqual(account_number, "1")

  def testShouldParseSingleTwo(self):
    input = (
      " _ \n" +
      " _|\n" +
      "|_ \n" +
      "   \n")
    account_number = AccountParser().parse(input)
    self.assertEqual(account_number, "2")

  def testShouldParseTwoBinaryDigits(self):
    input = (
      "     _ \n" + 
      "  | | |\n" +
      "  | |_|\n" +
      "       \n"
      )
    account_number = AccountParser().parse(input)
    self.assertEqual(account_number, "10")

  def testShouldParseThreeBinaryDigits(self):
    input = (
      "     _     \n" + 
      "  | | |   |\n" +
      "  | |_|   |\n" +
      "           \n"
      )
    account_number = AccountParser().parse(input)
    self.assertEqual(account_number, "101")

  def testShouldParseFourBinaryDigits(self):
    input = (
      "     _       _ \n" + 
      "  | | |   | | |\n" +
      "  | |_|   | |_|\n" +
      "               \n"
      )
    account_number = AccountParser().parse(input)
    self.assertEqual(account_number, "1010")

if __name__ == '__main__':
    unittest.main()
