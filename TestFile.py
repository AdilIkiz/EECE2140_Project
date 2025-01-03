import string
import random
import smtplib

#For Email functionality
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Getting password length and character selection
#Function for decision making (Letter/Special Char/Number)
def user_preferences(): 
	#Keeps question loop going until valid response (LETTER)
	letter_decision_Bool = False 
	while not letter_decision_Bool:
		print("Would you like letters in your password?")
		#Decision Step
		letters_bool = bool(int(input("1 for YES, 0 for NO>>"))) 
		if letters_bool == 1 or letters_bool == 0:
			letter_decision_Bool = True
		else: #Error Handling Step
			print("Input Error") 

	#Keeps question loop going until valid response (SPECIAL CHARACTER)
	special_decision_Bool = False 
	while  not special_decision_Bool:
		print("Would you like any special characters in your password? 1 for YES, 0 for NO.")
		#Decision Step
		special_bool = bool(int(input("1 for YES, 0 for NO>>"))) 
		if special_bool == 1 or special_bool == 0:
			special_decision_Bool = True
		else: #Error Handling Step
			print("Input Error")
	
	#Keeps question loop going until valid response (NUMBERS)
	number_decision_Bool = False 
	while not number_decision_Bool:
		print("Would you like any numbers in your password? 1 for YES, 0 for NO.")
		#Decision Step
		numbers_bool = bool(int(input("1 for YES, 0 for NO>>"))) 
		if numbers_bool == 1 or numbers_bool == 0:
			number_decision_Bool = True
		else: #Error Handling Step
			print("Input Error")
	#returning decision booleans	
	return letters_bool, special_bool, numbers_bool #A TRUE value for a given boolean will mean that relevant characters will be included in the password.

#Password Generation
def generate_password(): 
	letters_bool, special_bool, numbers_bool = user_preferences() #Calling Decision Making Function, Assigning Boolean Values
	length = int(input("Enter password length: ")) #Password Lenght
	
	password = [] #Initiating empty list as password

	#Character Bank (Boolean values dictate their involvement)
	alphabetChar = "abcdefghijklmnopqrstuvwxyz"
	specialChar = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	numChar = "1234567890"
	validChars = ""

	#Adding Chars into the possible mix given the boolean decision
	if(letters_bool):
		validChars = validChars + alphabetChar
	if(special_bool):
		validChars = validChars + specialChar
	if(numbers_bool):
		validChars = validChars + numChar
	
	#For a given lenght, a random characted from the mix is chosen and appended into blank password list.
	for i in range(length):
		password.append(random.choice(validChars))
	
	#Password is returned
	return("Your new Password:\n".join(password))

#Email Functionality
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

	#Feedback in console 
        print("Email sent successfully.")
        
    except Exception as e: #Error Notification
        print(f"An error occurred: {e}")

# sending email to google email
send_email(
    sender_email="klaidaswik@gmail.com",
    sender_password="wnyn kdeu dwrg rcve",
    recipient_email=input("Whats your email to send the password to?"),
    subject="Secure Generated Password",
    body=generate_password()
)



