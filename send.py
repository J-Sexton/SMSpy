from twilio.rest import Client
import parse
import sys

# Your Account SID from twilio.com/console
account_sid = "AC3d455fc0bc81d140bc53a8153c7e8a42"
# Your Auth Token from twilio.com/console
auth_token  = "0b4411e808c8165d78f02ab319a9d4fd"

client = Client(account_sid, auth_token)

def sendAll(var):
   rentData = parse.getAll()

   for item in rentData:
      message = client.messages.create(
          to=item.phone, 
          from_="+17069792394",
          body= var)

   print(message.sid)

if __name__ == "__main__":
    sendAll(sys.argv[1])
