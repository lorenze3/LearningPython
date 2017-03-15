#! python3
# textSomeone.py -- defines textSomeone function that texts a given number and
# message passed to it as a string

#Twilio values:
accountSID = 'AC90d31b714a818b434e9fdd877cf5fd6b'
authToken = '27ad3bc7fc6eef9fe19f945c6ce35a49'
myTwilioNumber = '+13177898775'

#log in at twilio.com for details -- currently a free trial account
#check for charges 


#bring in twilio python package and twilio command line client
from twilio.rest import TwilioRestClient

#function that calls the Twilio client defined next
def textSomeone(message, toNumber):
    twilioCLI = TwilioRestClient(accountSID, authToken)
    twilioCLI.messages.create(body=message,from_=myTwilioNumber, to=toNumber)

