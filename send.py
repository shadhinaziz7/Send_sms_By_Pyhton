from twilio.rest import Client



account_sid = "******************************"
auth_token = "**********************************"
client = Client(account_sid, auth_token)
message = client.api.account.messages.create(to="+15074060406",from_="+18175812331",body="I am Python and i can do everything!")
