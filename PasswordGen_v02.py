import string
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

class PasswordManager:
    def __init__(self):
        self.pw = ""
        self.letters_bool = False
        self.special_bool = False
        self.numbers_bool = False

    # Function for decision making (Letter/Special Char/Number)
    def user_preferences(self):
        # Keeps question loop going until valid response (LETTER)
        while True:
            print("Would you like letters in your password?")
            letters_bool = bool(int(input("1 for YES, 0 for NO>> ")))
            if letters_bool in [0, 1]:
                self.letters_bool = letters_bool
                break
            else:
                print("Input Error")
        
        # Keeps question loop going until valid response (SPECIAL CHARACTER)
        while True:
            print("Would you like any special characters in your password? 1 for YES, 0 for NO.")
            special_bool = bool(int(input("1 for YES, 0 for NO>> ")))
            if special_bool in [0, 1]:
                self.special_bool = special_bool
                break
            else:
                print("Input Error")
        
        # Keeps question loop going until valid response (NUMBERS)
        while True:
            print("Would you like any numbers in your password? 1 for YES, 0 for NO.")
            numbers_bool = bool(int(input("1 for YES, 0 for NO>> ")))
            if numbers_bool in [0, 1]:
                self.numbers_bool = numbers_bool
                break
            else:
                print("Input Error")

    # Password Generation
    def generate_password(self):
        self.user_preferences()  # Calling Decision Making Function

        length = int(input("Enter password length: "))  # Password Length
        password = []  # Initiating empty list as password

        # Character Bank (Boolean values dictate their involvement)
        alphabetChar = "abcdefghijklmnopqrstuvwxyz"
        specialChar = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        numChar = "1234567890"
        validChars = ""

        # Adding Chars into the possible mix given the boolean decision
        if self.letters_bool:
            validChars += alphabetChar
        if self.special_bool:
            validChars += specialChar
        if self.numbers_bool:
            validChars += numChar

        # For a given length, a random character from the mix is chosen and appended into blank password list.
        for _ in range(length):
            password.append(random.choice(validChars))

        self.pw = "".join(password)  # Store password

        return self.pw


class EmailManager:
    def __init__(self, sender_email, sender_password, recipient_email, subject):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.subject = subject
        self.server = None

    def send_email(self, password):
        try:
            # Set up the MIME
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = self.recipient_email
            message['Subject'] = self.subject

            # Accesses the html file
            with open('email_html/email_body.html', 'r') as file:
                html_content = file.read().replace("{PASS}", password)

            # Attach the HTML part
            message.attach(MIMEText(html_content, 'html'))

            # Connect to the Gmail Google server
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.starttls()  # Secure the connection
            self.server.login(self.sender_email, self.sender_password)

            # Sends the email
            self.server.sendmail(self.sender_email, self.recipient_email, message.as_string())
            self.server.quit()

            print("Email sent successfully.")
        
        except Exception as e:  # Error Notification
            print(f"An error occurred: {e}")


class PasswordEmailManager:
    def __init__(self, sender_email, sender_password, recipient_email, subject):
        self.password_manager = PasswordManager()
        self.email_manager = EmailManager(sender_email, sender_password, recipient_email, subject)

    def execute(self):
        # Generate password
        password = self.password_manager.generate_password()

        # Send email with generated password
        self.email_manager.send_email(password)


if __name__ == "__main__":
    # Set up your sender email, password, recipient email, and subject
    sender_email = "klaidaswik@gmail.com"
    sender_password = "wnyn kdeu dwrg rcve"
    recipient_email = input("What's your email to send the password to? ")
    subject = "Secure Generated Password"

    # Create an instance of PasswordEmailManager and run it
    manager = PasswordEmailManager(sender_email, sender_password, recipient_email, subject)
    manager.execute()
