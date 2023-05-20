
# Owncast-sound-chat
petit script pour déclenché un sons sur un ordinateur a l'aide d'un webhook
ou sur le chat de votre instance Owncast


# Requirement
playsound, 
flask,
asyncio,
os,
requests,
json,
inquirer,

Python 3.10

# description
sendsound.py est le client qui permet d'envoyer l'ordre de déclenché un sons au webhook il n'est donc pas néssécaire pour l'ordinateur sur lequelle se déclencheras le sons

webhook.py est l'host il est nécéssaire pour que les sons se déclenche et doit être placé sur l'ordinateur cible (sur le quelle vous souhaité déclenché les son)
note : les sons doivent être présent dans un dossier sur se même ordinateur

# sendsound.py
remplacé "yourip:5000/webhook" par votre ip
Exemple : "192.168.1.50:5000/webhook"

remplacé "choices=['!discordping', '!other-sound' ]," par vos sons en enlevant juste le .wav/mp3 a la fin (uniquement dans le code)

Exemple : choices=['discordping', 'second-sound' ],
discorping.wav --> discordping 

# webhook
remplacé "playsound('C:/mysound/'+(content["eventData"]["body"]+('.wav')),)"

C:/mysound/ --> l'emplacement de votre dossié contenent vos sons

.wav --> l'extension de fichier que vous utilisé (mp3/wav/....)

# intégration Onwcast
l'integration Owncast permet au chat de votre instance owncast de déclenché les sons
en envoyant un message correspondant au nom du sons que vous avez ajouté dans notre cas 
"discordping"


dans intégration-->webhook 

cliqué sur create webhook puis entré l'url de votre webhook et coché "when a user sends a chat message"

![](https://i.imgur.com/asImyNk.png)

![](https://i.imgur.com/3E1vBvL.png)


