from dotenv import load_dotenv, find_dotenv
from os import environ as env
import random
from re import fullmatch
import smtplib
load_dotenv(find_dotenv())


class OTPService:
    def __init__(self, email, passwd):
        self._email = email
        self._passwd = passwd
        self._server = smtplib.SMTP('smtp.gmail.com', 587)
        self._OTP = ""

    def sendMail(self, receiver):
        msg = '\n\nThe One Time Password(OTP) is: ' + self._OTP
        self._server.sendmail(self._email, receiver, msg)
        print("\n\tOTP is sent to the given email address")

    def initiateServer(self):
        self._server.starttls()
        self._server.login(self._email, self._passwd)
        print("\nSMTP server is initialized and running....")

    def closeServer(self):
        self._server.quit()
        print("\nSMTP server closed.")

    def generateOTP(self, length):
        if length < 4 or length > 6:
            print("The length of the OTP must be at-least 4 and at-max 6")
            return False

        digits = "0123456789"
        otp = random.sample(digits, length)
        self._OTP = "".join(otp)

    def validateOTP(self, otp):
        if self._OTP != "" and self._OTP == otp:
            print("Given OTP was correct")
        else:
            print("Given OTP was incorrect")
        



if __name__ == "__main__":
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    EMAIL = env.get('EMAIL')
    EMAIL_PASSWD = env.get('PASSWORD')
    LENGTH = int(env.get("OTP_LENGTH"))

    otpSender = OTPService(EMAIL, EMAIL_PASSWD)
    otpSender.initiateServer()


    # Taking Input
    print("Please Enter your Email to receive OTP")
    receiver_email = input("Email: ")

    while fullmatch(regex, receiver_email) == None:
        print("Please enter a valid email address")
        receiver_email = input("Email: ")

    otpSender.generateOTP(LENGTH)
    otpSender.sendMail(receiver_email)

    print("Please enter the OTP to proceed")
    otp = input("OTP: ")
    otpSender.validateOTP(otp)

    otpSender.closeServer()