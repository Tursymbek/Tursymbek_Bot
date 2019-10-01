import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler

import settings
from handlers import *

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log')

def main():

    updater = Updater(settings.API_KEY, use_context = True)

    logging.info('Bot is started')

    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('planet', planets, pass_user_data=True))
    dp.add_handler(CommandHandler('cat', send_cat_picture, pass_user_data=True))
    
    dp.add_handler(MessageHandler(Filters.regex('Больше котиков'), send_cat_picture, pass_user_data=True))
    #dp.add_handler(RegexHandler('^(Найти небесные объект)$', planets, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
      
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()