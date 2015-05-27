class AccountParser(object):
	ZERO = (" _ " +
			"| |" +
			"|_|" +
			"   ")
	ONE = (
			"   " +
			"  |" +
			"  |" +
			"   ")
	DIGITS = {ZERO : "0", ONE: "1"}

	def __init__(self):
		pass

	def parse(self, input):
		lines = input.split("\n")
		number_of_digits = ((len(lines[0]) - 3) / 4) + 1
		account_number = ""

		for ith_digit in range(1, number_of_digits+1):
			account_number = account_number + self.parse_digit(self.get_n_digit(lines, ith_digit))
		return account_number
		
	def get_n_digit(self, lines, pos):
		digit = ""
		index = (pos-1)*4
		for line in lines:
			digit = digit + line[index:index + 3]
		return digit

	def parse_digit(self, digit):
		return AccountParser.DIGITS.get(digit,"2")