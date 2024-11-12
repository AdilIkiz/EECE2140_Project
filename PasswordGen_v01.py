import string
import random

# Getting password length

def user_preferences():
	letters_bool = False
	special_bool = False
	numbers_bool = False

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

	while(True):

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
				letters_bool, special_bool, numbers_bool = user_preferences()
				password.clear()
				break
		else:
			break

	print("".join(password))



generate_password()
