class AccountValidator(object):
	def __init__(self):
		pass

	def is_valid_checksum(self, account_number):

		check_sum = 0
		for ith_digit in reversed(range(9)):
			check_sum = check_sum + int(account_number[ith_digit]) * (9 - ith_digit)		
		return check_sum % 11 == 0

	def validate(self, account_number):
		if self.non_parseable(account_number):
			return account_number + " ILL"
		elif not self.is_valid_checksum(account_number):
			return account_number + " ERR"
		else:
			return account_number

	def non_parseable(self, account_number):
		return account_number.find("?") != -1
		
