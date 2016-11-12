from twilio.rest import TwilioRestClient 
  
# put your own credentials here 
ACCOUNT_SID = "AC7eec02201b46e157430d1deb3df6c387" 
AUTH_TOKEN = "f4e5af03cec8d85df919db81b02fe522"
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

Message = "OVO JE TO JE TO"
 
client.messages.create(
	to="9092731214", 
	from_="+19094927006", 
	body=Message,  
) 
