from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem 
from datetime import date

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log')

def greet_user(update, context):
    text = '/start called'
    print (text)
    update.message.reply_text(text)

def talk_to_me(update, context):
    user_text = "Hello {}! You wrote: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def planets(update, context):      
    if  update.message.text == "Mars":
        u = ephem.Uranus()
        u.compute('1781/3/13')
        rpl = ephem.constellation(u)
        update.message.reply_text(rpl)

def main():

    updater = Updater(settings.API_KEY, use_context = True)

    logging.info('Bot is started')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', planets))

    updater.start_polling()
    updater.idle()

main()