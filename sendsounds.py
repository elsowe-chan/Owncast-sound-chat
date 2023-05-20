import requests
import json
import inquirer

webhook_url = "yourip:5000/webhook"


questions = [
  inquirer.List('sound',
                message="choisiser un son",
                choices=['!discordping', '!other-sound' ],
            ),
]
answers = inquirer.prompt(questions)
    
data = {
    "name": "test",
    "eventData": {
        "body": (answers["sound"]),
    }
}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type' : 'application/json'})

