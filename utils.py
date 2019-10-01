from telegram import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard():
    contact_button = KeyboardButton('Контактные данные', request_contact=True)
    location_button = KeyboardButton('Геолокация', request_location=True)
    
    my_keyboard = ReplyKeyboardMarkup([['Больше котиков'], #['Найти небесные объект'],
    [contact_button, location_button]], resize_keyboard=True)

    return my_keyboard

