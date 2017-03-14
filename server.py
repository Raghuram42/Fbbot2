from flask import Flask, request
import requests
import aiml
import sys
import commands


kernel= aiml.Kernel()


brainLoaded = False
forceReload = False

app = Flask(__name__)
ACCESS_TOKEN = "EAAZAkkZC0hwegBAIPZBpPAxFq6sp89ofGI35ZBTlwUSFAKblvUpaKTBRxrFGZBN1Y9WBLrHdHk1T0tH2J6WRtu0uiifgADNzwzmQRZBnaVea3lTjxd7ZCSVmOsnOYsa61TIdS43meIqJ9iWjdgZCvTQktxJSEPTz5lNbaAHUQF14mQZDZD"
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
   while not brainLoaded:
           if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):

                kernel.bootstrap(learnFiles="std-startup.xml", commands="LOAD AIML B")
                brainLoaded = True
                kern.saveBrain("standard.brn")
           else:
                try:
                    kernel.bootstrap(brainFile = "standard.brn")
                    brainLoaded = True
                except:
                    forceReload = True

   
   
   #nani = kernel.respond(message)           
   reply(sender, nani)


   return "ok"


if __name__ == '__main__':
       app.run(debug=True,host='0.0.0.0', port=80)

while(True):
  print kern.respond(raw_input("> "))
