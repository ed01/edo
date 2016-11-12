#
#
#SID = SK8ecbe11700e3172fe3b77e9b95a31817
#SECRET =ukQMwjROjftv17lt62r7e5PSAdl3JS38
#
# Testing sending emails using python.

from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "XXXXXX"
AUTH_TOKEN = "XXXXXX"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

test = input("Input something\n")

if (test == "something"):

    Message = input("sms message\n")

    client.messages.create(
        to="XXXXX",
        from_="XXXXXXX",
        body=Message,
    )

else:
    print("try again")
