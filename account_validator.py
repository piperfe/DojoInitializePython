class AccountValidator(object):
	def __init__(self):
		pass

	def is_valid_account_number(self, account_number):

		check_sum = 0
		for ith_digit in reversed(range(9)):
			check_sum = check_sum + int(account_number[ith_digit]) * (9 - ith_digit)		
		return check_sum % 11 == 0
		