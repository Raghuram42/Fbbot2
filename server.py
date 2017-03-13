from flask import Flask, request
import requests
import aiml
import os

kernal= aiml.Kernal()
app = Flask(__name__)
ACCESS_TOKEN = "EAAZAkkZC0hwegBAKdrUtmtOxTpx7fd7TRjfotY83XZATuElHIXOhBZAyeR6NmrNbB8lzaBZCKipjMZCyqUtBAxu3FkonhFlB5oScW6LPyDIHgq0e9FquoXzsIAj4ufDk6Am05yBJoryFNTOMsxuwsbLZA4LKEAjbUMvyMizkXgdigZDZD"
VERIFY_TOKEN = "fbbot"

def reply(user_id, msg):
   data ={
   "recipient":{"id":user_id},
   "message":{"text": msg }
   }
   resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token="+ ACCESS_TOKEN, json=data)
   print(resp.content)



@app.route('/', methods=['GET'])
def handle_verfication():
       if request.args['hub.verify_token'] == VERIFY_TOKEN:
             return request.args['hub.challenge']
       else:
            return "Invalid verification token"
 

@app.route('/', methods=['POST'])
def handle_incoming_messages():
   data =request.json
   sender = data['entry'][0]['messaging'][0]['sender']['id']
   message = data['entry'][0]['messaging'][0]['message']['text']
   if os.path.isfile("joker_brain.brn"):
        kernal.bootstrap(brainFile ="joker_brain.brn")
   else:
        kernal.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
        kernal.saveBrain("joker_brain.brn")

  nani = kernal.respond(message)           
   reply(sender, nani)


   return "ok"


if __name__ == '__main__':
       app.run(debug=True,host='0.0.0.0', port=80)
