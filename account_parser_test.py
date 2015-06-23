import unittest
from account_parser import AccountParser, InvalidAccountNumberException

class TestAccountParser(unittest.TestCase):

	def testShouldParseSingleZero(self):
		input = (
			" _ " +
			"| |" +
			"|_|" +
			"   ")
		account_number = AccountParser().parse_digit(input)
		self.assertEqual(account_number, "0")

	def testShouldParseSingleOne(self):
		input = (
			"   " +
			"  |" +
			"  |" +
			"   ")
		account_number = AccountParser().parse_digit(input)
		self.assertEqual(account_number, "1")

	def testShouldParseSingleTwo(self):
		input = (
			" _ " +
			" _|" +
			"|_ " +
			"   ")
		account_number = AccountParser().parse_digit(input)
		self.assertEqual(account_number, "2")


	def testShouldReturnNumberTwo(self):
		input = (
			" _ " +
			" _|" +
			" _ " +
			"   ")
		account_number = AccountParser().parse_digit(input)
		self.assertEqual(account_number, "2")

	def testShouldReturnNumberZero(self):
		input = (
			"   " +
			"| |" +
			"|_|" +
			"   ")
		account_number = AccountParser().parse_digit(input)
		self.assertEqual(account_number, "0")

	def testShouldParseNineDigits(self):
		input = (
			"     _   _       _       _   _   _ \n" + 
			"  |  _|  _| |_| |_  |_    | |_| |_|\n" +
			"  | |_   _|   |  _| |_|   | |_|   |\n" +
			"                                   \n"
			)
		account_number = AccountParser().parse(input)
		self.assertEqual(account_number, "123456789")

	def testShouldThrowAnErrorForAccountNumberWithMoreThanNineDigits(self):
		input = (
			" _       _   _       _       _   _   _ \n" + 
			"| |   |  _|  _| |_| |_  |_    | |_| |_|\n" +
			"|_|   | |_   _|   |  _| |_|   | |_|   |\n" +
			"                                       \n"
			)
		with self.assertRaises(InvalidAccountNumberException):
			AccountParser().parse(input)

	def testShouldThrowAnErrorForAccountNumberWithLessThanNineDigits(self):
		input = (
			" _       _       _   _   _ \n" + 
			" _| |_| |_  |_    | |_| |_|\n" +
			" _|   |  _| |_|   | |_|   |\n" +
			"                           \n"
			)
		with self.assertRaises(InvalidAccountNumberException):
			AccountParser().parse(input)

if __name__ == '__main__':
		unittest.main()
