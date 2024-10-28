import string
import random

# Getting password length

print("Answer 'True' or 'False' based on whether you want or not")

digits_bool = bool(input("Digits? "))
letters_bool = bool(input("Letters? "))
special_bool = bool(input("Special Characters? "))
numbers_bool = bool(input("Numbers? "))


def inititalization():
	PWlength = int(input("Enter password length: "))
	

print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

characterList = ""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		
		# Adding letters to possible characters
		characterList += string.digits
	elif(choice == 2):
		
		# Adding digits to possible characters
		characterList += string.ascii_letters
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(length):

	# Picking a random character from our 
	# character list
	randomchar = random.choice(characterList)
	
	# appending a random character to password
	password.append(randomchar)

# printing password as a string
print("The random password is " + "".join(password))

#klaidas


