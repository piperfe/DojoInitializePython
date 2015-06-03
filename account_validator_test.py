import unittest
from account_validator import AccountValidator

class TestAccountValidator(unittest.TestCase):
	def testShouldBeAValidAccountNumber(self):
		input = "000000000"
		is_valid_account_number = AccountValidator().is_valid_account_number(input)
		self.assertEqual(is_valid_account_number, True)
		input = "000000019"
		is_valid_account_number = AccountValidator().is_valid_account_number(input)
		self.assertEqual(is_valid_account_number, True)
		input = "345882865"
		is_valid_account_number = AccountValidator().is_valid_account_number(input)
		self.assertEqual(is_valid_account_number, True)


	def testShouldBeNotValidAccountNumber(self):
		input = "100000000"
		is_valid_account_number = AccountValidator().is_valid_account_number(input)
		self.assertEqual(is_valid_account_number, False)
		input = "000000012"
		is_valid_account_number = AccountValidator().is_valid_account_number(input)
		self.assertEqual(is_valid_account_number, False)
		input = "342882865"
		is_valid_account_number = AccountValidator().is_valid_account_number(input)
		self.assertEqual(is_valid_account_number, False)
		input = "34882865"
		is_valid_account_number = AccountValidator().is_valid_account_number(input)
		self.assertEqual(is_valid_account_number, False)

if __name__ == '__main__':
	unittest.main()