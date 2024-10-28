import string
import random

# Getting password length and character selection

print("Answer 'True' or 'False' based on whether you want or not")

letters_bool = bool(input("Letters? "))
special_bool = bool(input("Special Characters? "))
numbers_bool = bool(input("Numbers? "))


def generate_password():

	length = int(input("Enter password length: "))

	password = []
	alphabetChar = "abcdefghijklmnopqrstuvwxyz"
	specialChar = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"



	for i in range(length):

		num_iterator = random.randint(1, 3)

		if(numbers_bool & (num_iterator == 1)):
			password.append(str(random.randint(0,9)))

		elif(letters_bool & (num_iterator == 2)):
			password.append(random.choice(alphabetChar))

		elif(special_bool & (num_iterator == 3)):	
			password.append(random.choice(specialChar))
		else:
			print("Something went wrong. Did you give valid inputs?")

	print("".join(password))



generate_password()

























