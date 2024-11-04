import string
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
































