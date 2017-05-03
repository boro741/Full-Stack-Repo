# 3. Use Twilio web API to send SMS

# from is a keyword
# We use it when to import a class from folders.
# Here /twilio/rest -->  _init_.py ( class Client)
# Link to github -->
# https://github.com/twilio/twilio-python/blob/master/twilio/rest/__init__.py


from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9130df7457b1fc4f065d81d18a8789fa"
# Your Auth Token from twilio.com/console
auth_token  = "08a40f53ae14adf084e9c79deae2b05b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919700332950", 
    from_="+17542273676",
    body="Hello from Pavan. This is another test")

print(message.sid)
