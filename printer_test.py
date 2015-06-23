import unittest
from account_printer import Printer
from account_parser import AccountParser, InvalidAccountNumberException
from account_validator import AccountValidator


class TestAccountPrinter(unittest.TestCase):
	
	def testShouldPrintNumber(self):
		input = (
                        "     _   _       _       _   _   _ \n" +
                        "  |  _|  _| |_| |_  |_    | |_| |_|\n" +
                        "  | |_   _|   |  _| |_|   | |_|   |\n" +
                        "                                   \n"
                        )

		account_number = AccountParser().parse(input)
		is_valid_account_number = AccountValidator().is_valid_account_number(account_number)




