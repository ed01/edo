#
#
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
