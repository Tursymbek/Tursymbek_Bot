from datetime import datetime
from glob import glob
import logging
from random import choice

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
from functools import wraps

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log')

def greet_user(update, context):
    text = '/start called'
    print (text)
    update.message.reply_text(text)

def planets(update, context):      
    user_planet = update.message.text.split()
   
    u = getattr(ephem, user_planet[1])
    tm = datetime.now()
    star_in = u(tm)
    result = ephem.constellation(star_in)
    update.message.reply_text("Your planet in {}.".format(result))

def send_cat_picture(update, context):
    cat_list = glob('image/cat*.jp*g')
    cat_pic = choice(cat_list)
    update.message.reply_photo(photo=open(cat_pic, 'rb'))
    #bot.send_photo(chat_id=update.message.chat.id, photo = open(cat_pic, 'rb'))

def talk_to_me(update, context):
    user_text = "Hello {}! You wrote: {}. \nYou can find these planets: \n Mercury, \n Venus, \n Mars, \n Jupiter, \n Saturn, \n Uranus, \n Neptune, \n Pluto, \n Sun, \n Moon.".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():

    updater = Updater(settings.API_KEY, use_context = True)

    logging.info('Bot is started')

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planets))
    dp.add_handler(CommandHandler('cat', send_cat_picture))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
  
    updater.start_polling()
    updater.idle()

main()