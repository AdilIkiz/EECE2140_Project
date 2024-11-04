import string
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Getting password length and character selection

def user_preferences():
	letter_decision_Bool = False
	while not letter_decision_Bool:
		print("Would you like letters in your password?")
		letters_bool = bool(int(input("1 for YES, 0 for NO>>")))
		if letters_bool == 1 or letters_bool == 0:
			letter_decision_Bool = True
		else:
			print("Input Error")
	special_decision_Bool = False
	while  not special_decision_Bool:
		print("Would you like special characters in your password? 1 for YES, 0 for NO.")
		special_bool = bool(int(input("1 for YES, 0 for NO>>")))
		if special_bool == 1 or special_bool == 0:
			special_decision_Bool = True
		else:
			print("Input Error")
	number_decision_Bool = False
	while not number_decision_Bool:
		print("Would you like numbers in your password? 1 for YES, 0 for NO.")
		numbers_bool = bool(int(input("1 for YES, 0 for NO>>")))
		if numbers_bool == 1 or numbers_bool == 0:
			number_decision_Bool = True
		else:
			print("Input Error")
		
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

	return("".join(password))


def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connects to the Gmail Google server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Sends the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()

        print("Email sent successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

send_email(
    sender_email="klaidaswik@gmail.com",
    sender_password="wnyn kdeu dwrg rcve",
    recipient_email=input("Whats your email to send the password to?"),
    subject="Secure Generated Password",
    body=generate_password()
)
































