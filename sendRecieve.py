import parse
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():

    body = request.values.get('Body', None)

    resp = MessagingResponse()
    
    if body == 'Hi':
        resp.message("Hello, please respond with your name!")
    elif body == 'Andrew':
        vab =  parse.getName('Andrew')
        resp.message(vab)
    elif body == 'Gaby':
        resp.message("Do homework so we can go out tonight.")
    elif body == 'Josh':
        resp.message("Good job man.")
    elif body == 'Oscar':
        resp.message("Feel better my dude.")
    elif body == 'Jessica':
        resp.message("I wanna go out tonight.")
    elif body == 'Andres':
        resp.message("Yo, diggin the kicks my dude.")
    elif body == 'Cruz':
        resp.message("Bruh, how can I cop that shirt?")
  
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)



