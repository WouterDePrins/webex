# Script to update ngrok for WebEx Teams Webhooks (messages and attachements) by Wouter De Prins

import requests
import json

###### Fill in the new ngrok URL #######
######

ngrok_http = ""         # "https://" for example
ngrok_plain = ""        # "cebf5da3.ngrok.io" for example 
ngrok_server_url = "/"  # could be "/postmessage" for example
token = ""              # WebEx Teams Token

webhookId = ""          # Your WebHook ID - first execute the read function to list your Webhooks

########################################################################################################################

ngrok = ngrok_http + ngrok_plain + ngrok_server_url
url = "https://api.ciscospark.com/v1/webhooks/"

headers = {
  'Authorization': 'Bearer ' + token,
  'Content-Type': 'application/json'
}

new_ngrok = {
  "targetUrl": ngrok,
}

def readWebhooks():
    response = requests.request("GET", url, headers=headers)
    webhooks = json.loads(response.text)
    for i in webhooks['items']:
        print('Webhook ID: ' + i["id"])
        print('Webhook Name: ' + i["name"])
        print('Webhook Target Url: ' + i["targetUrl"])
        print('-' * 100)

def changeWebHook():
    response = requests.request("PUT", url + webhookId, json=new_ngrok, headers=headers)
    if response.status_code == 200:
        print('Webhook Updated')
