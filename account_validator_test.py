import unittest
from account_validator import AccountValidator

class TestAccountValidator(unittest.TestCase):

	def testShouldBeAValidChecksum(self):
		input = "000000000"
		is_valid_account_number = AccountValidator().is_valid_checksum(input)
		self.assertEqual(is_valid_account_number, True)
		input = "000000019"
		is_valid_account_number = AccountValidator().is_valid_checksum(input)
		self.assertEqual(is_valid_account_number, True)
		input = "345882865"
		is_valid_account_number = AccountValidator().is_valid_checksum(input)
		self.assertEqual(is_valid_account_number, True)


	def testShouldBeNotValidChecksum(self):
		input = "100000000"
		is_valid_account_number = AccountValidator().is_valid_checksum(input)
		self.assertEqual(is_valid_account_number, False)
		input = "000000012"
		is_valid_account_number = AccountValidator().is_valid_checksum(input)
		self.assertEqual(is_valid_account_number, False)
		input = "342882865"
		is_valid_account_number = AccountValidator().is_valid_checksum(input)
		self.assertEqual(is_valid_account_number, False)
		input = "348828695"
		is_valid_account_number = AccountValidator().is_valid_checksum(input)
		self.assertEqual(is_valid_account_number, False)

	def testShouldReturnValidNumber(self):
		input = "000000019"
		self.assertEqual("000000019",AccountValidator().validate(input))

	def testShouldReturnILLForAnNonParseableNumber(self):
		input = "000000?19"
		self.assertEqual("000000?19 ILL",AccountValidator().validate(input))

	def testShouldReturnILLIFNotPossibleToFixAccountNumber(self):
		input = "000000??9"
		self.assertEqual("000000??9 ILL",AccountValidator().validate(input))
	
	def testShouldReturnERRForParseableNumberButInvalidNumber(self):
		input = "100000000"
		self.assertEqual("100000000 ERR",AccountValidator().validate(input))

if __name__ == '__main__':
	unittest.main()
