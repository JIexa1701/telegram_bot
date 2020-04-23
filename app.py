#!/usr/bin/env python
# coding: utf-8

# In[3]:


#pip install flask
#!pip install python-telegram-bot
#pip install requests


# In[4]:


#!pip install flask


# In[ ]:


# По статье на https://medium.com/@aliabdelaal/telegram-bot-tutorial-using-python-and-flask-1fc634da9522


# In[ ]:

#import sys, os

#sys.path.append(os.path.join(os.path.dirname(__file__)))

from flask import Flask, request
import telegram
#from credentials import bot_token, bot_user_name, URL
#from mastermind import get_response

#import credentials
#import mastermind

global bot
global TOKEN

#credentials.py
#bot_token = "954054131:AAGkj6-Zcjfh3AlVRKbVnMeUPqkyaAuyCps"
#bot_user_name = "plsapptelegrambot"
#URL = "https://telegrambotplsapp.herokuapp.com/"

TOKEN = '954054131:AAGkj6-Zcjfh3AlVRKbVnMeUPqkyaAuyCps'
bot = telegram.Bot(TOKEN)

app = Flask(__name__)

# mastermind


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)

    response = get_response(text)
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    return 'ok'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)


# In[ ]:


#credentials.py

# bot_token = "954054131:AAGkj6-Zcjfh3AlVRKbVnMeUPqkyaAuyCps"
# bot_user_name = "plsapptelegrambot"
# URL = "https://telegrambotplsapp.herokuapp.com/"


# In[ ]:




