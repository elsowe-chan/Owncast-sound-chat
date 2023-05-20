from flask import Flask, request, abort
import playsound
import asyncio
import os
app = Flask(__name__)

f = open("sound.txt", "w")
f.write("")
f.close()

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        content = request.json
        playsound.playsound('C:/mysound/'+(content["eventData"]["body"]+('.wav')),)
        

    else:
        abort(400)




if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
