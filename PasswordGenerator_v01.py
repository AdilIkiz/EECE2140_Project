import string
import random

# Getting password length and character selection

def user_preferences():

	print("Answer '1' or '0' based on whether you want or not. 1 being yes and 0 being no")

	letters_bool = bool(int(input("Letters? ")))
	special_bool = bool(int(input("Special Characters? ")))
	numbers_bool = bool(int(input("Numbers? ")))

	return letters_bool, special_bool, numbers_bool



def generate_password():

	letters_bool, special_bool, numbers_bool = user_preferences()
	length = int(input("Enter password length: "))

	password = []
	alphabetChar = "abcdefghijklmnopqrstuvwxyz"
	specialChar = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	numChar = "1234567890"
	validChars = ""
	
	if(letters_bool):
		validChars = validChars + alphabetChar
	if(special_bool):
		validChars = validChars + specialChar
	if(numbers_bool):
		validChars = validChars + numChar

	for i in range(length):
		password.append(random.choice(validChars))

	print("".join(password))



generate_password()

























