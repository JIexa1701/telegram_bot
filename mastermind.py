#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import telebot
TOKEN = '954054131:AAGkj6-Zcjfh3AlVRKbVnMeUPqkyaAuyCps'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_response(message):
    
    if message.text == 'привіт':
        bot.send_message(message.chat.id, 'литыомиы')
    elif message.text == 'пока':
        bot.send_message(message.chat.id, 'Прощавай, Майстер')
    elif message.text == 'путин':
        bot.send_message(message.chat.id, 'ла-ла-ла-ла-ла-ла путін - хуйло')
    else: 
        bot.send_message(message.chat.id, message.text)
    
    return 'ok'

        
bot.polling()

