#
#
#SID = SK8ecbe11700e3172fe3b77e9b95a31817
#SECRET =ukQMwjROjftv17lt62r7e5PSAdl3JS38
#
# Testing sending emails using python.

from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "AC7eec02201b46e157430d1deb3df6c387"
AUTH_TOKEN = "f4e5af03cec8d85df919db81b02fe522"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

test = input("Input something\n")

if (test == "something"):

    Message = input("sms message\n")

    client.messages.create(
        to="9092731214",
        from_="+19094927006",
        body=Message,
    )

else:
    print("try again")
