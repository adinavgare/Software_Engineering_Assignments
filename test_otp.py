# THIS IS MAIN FILE I NAMED AS Send_OTP_Using_Mail_2, this is version 2.
import GetPass #Importing Password,Email From another file.
import random
import smtplib #This library is used for sending message using email.
import time
password = GetPass.pwd
Sender_Mail = GetPass.email
def EmailValidation(Email):
    True_Str1,True_Str2 = "yahoo" in Email,"gmail" in Email # This will store boolean values.
    if (True_Str1 or True_Str2) and( "@" in Email and "." in Email and "com" in Email):
        print("\nNo Error Found in Email!")
    else:
        raise AssertionError("Please enter valid Domain Name!")
def genrateOtp():
    Length = int(input("Enter Length of OTP: "))
    otp = ''.join([str(random.randint(0,9)) for i in range(Length)]) #Generated OTP using
    random.randint()
    return otp
def sendMail(Name,Email,otp):
    server = smtplib.SMTP('smtp.gmail.com',587) #Created gmail's server, and connected to gmail API
    # Adding transfer layered security
    server.starttls()
    server.login(Sender_Mail,password) # Email, App password are inserted.
    if True:
        msg = f"Subject: Sending Mail using Python (smtplib)!\n\nHello +{Name}+, Your OTP is{str(otp)}+\n\n You Have 30 Seconds to enter OTP!" 
    #Inserted Sender email ID, Recevier email ID. 
        server.sendmail(Sender_Mail,Email,msg)
        print("Email Sent!")
        server.quit()
def validateOTP(OT):
# This function will check entered otp is valid or not!
# This function also have Time Limit of 30 Sec
    test_time = 30
    beg_time = time.time()
    now_time = time.time()
    otp = OT
    input_otp = 0
    if input_otp == otp:
        pass
    else:
        while input_otp != otp and int(now_time)-int(beg_time) <= test_time:
            if now_time-beg_time <=test_time:
                input_otp = input("Enter Valid OTP: ")
                now_time = time.time()
                if input_otp == otp:
                    print("OTP IS VALID!")
                else:
                    raise AssertionError("Out Of Time!")
