import parse
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():

    body = request.values.get('Body', None)
    print "Recieved: " + body

    resp = MessagingResponse()
    
    if body == 'Hi':
        resp.message("Hello, please respond with your name to find out how much you owe!")
    else:
        vab = parse.getName(body)
        if vab != None:
           resp.message(vab.name + " owes " + vab.total+'\n' + "Rent: " +
                        vab.rent +'\n'+ "Water: " + vab.water +'\n'+ "Internet: " +
                        vab.internet +'\n' +"Power: " + vab.power +'\n'+"Gas: " + vab.gas)
           print resp 
           return str(resp)    
    
if __name__ == "__main__":
    app.run(debug=True)



