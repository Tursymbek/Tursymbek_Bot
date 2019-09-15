from datetime import datetime
from glob import glob
import logging
from random import choice

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton
import ephem
from functools import wraps

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log')


def greet_user(update, context):
    text = 'Вызван /start. Напишите что-нибудь.'
    
    update.message.reply_text(text, reply_markup = get_keyboard())

def planets(update, context):      
    user_planet = update.message.text.split()
    try:   
        u = getattr(ephem, user_planet[1])
        
        tm = datetime.now()
        star_in = u(tm)
        result = ephem.constellation(star_in)
        
        update.message.reply_text("Этот объект сейчас в созвездии {}.".format(result), reply_markup = get_keyboard())
    except:
        update.message.reply_text("Планету под названием '{}' я не нашел. \nПопробуйте следующие:\nMercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Sun, Moon. \nПисать нужно в таком порядке: /planet название планеты.".format(user_planet[1]), reply_markup = get_keyboard())

def get_contact(update, context):
    print(update.message.contact)
    update.message.reply_text('Мы получили Ваши данные!', reply_markup = get_keyboard())

def get_location(update, context):
    print(update.message.location)
    update.message.reply_text('Мы получили Ваши данные!', reply_markup = get_keyboard())

def send_cat_picture(update, context):
    cat_list = glob('image/cat*.jp*g')
    cat_pic = choice(cat_list)
    update.message.reply_photo(photo=open(cat_pic, 'rb'), reply_markup = get_keyboard())

def talk_to_me(update, context):
    user_text = "Привет {}! Вы написали: {}, но я Вас не понимаю. Я умею делать две вещи: \n1. Оправлять фото котиков (для этого введите /cat). \n2. Писать в каком созвездии находится планета (для этого введите /planet название планеты). \nВы можете найти следующие планеты: \nMercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Sun, Moon.".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text, reply_markup = get_keyboard())

def get_keyboard():
    contact_button = KeyboardButton('Контактные данные', request_contact=True)
    location_button = KeyboardButton('Геолокация', request_location=True)
    
    my_keyboard = ReplyKeyboardMarkup([['Больше котиков'], #['Найти небесные объект'],
    [contact_button, location_button]], resize_keyboard=True)

    return my_keyboard

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

main()