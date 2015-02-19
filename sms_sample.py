from tmobileSMS import *
import sys

username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
recipients = ["07XXXXXXXXX", "07XXXXXXXXX"]

# Login
session = tmobileLogin(username, password)
if session:
    for number in recipients:
         # NOTE! You need to retrieve new a token for each sms
        token = tmobileGetSendToken(session)
        if token:
            # send the messge
            if tmobileSendMsg(session, number, "Some message here!", token):
                print "SMS is sent to %s" % number
            else:
                print "Unable to send to %s, I will try next number" % number
        else:
            print "Unable to get sendSMS token, skip number %s and try next number!" % number
else:
    print "Unable to login!"
    sys.exit(0)
